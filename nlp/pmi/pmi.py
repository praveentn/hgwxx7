
# coding: utf-8

# # Comparables 

# In[1]:


'''

'''

# load libraries
import numpy as np
import pandas as pd

from scipy import sparse
from scipy.sparse import linalg 
from collections import Counter
from sklearn.preprocessing import normalize
from sklearn.metrics.pairwise import cosine_similarity

from nltk.corpus import stopwords


# ### Subject Company Data

# In[2]:


# Subject Company Description
sub_com_keywords = ["railway services", "rail parts", "rail supplies", "rail maintenance", "rail traffic", "railway service", 
                    "rail infrastructure", "electricity", "high speed rail", "mono rail", "electric train", "railways",
                    "tunnel", "maglev", "station", "rail industry", "train", "metro", "platform", "service"]
print(sub_com_keywords)


# ### Comparable Company Data

# In[3]:


# loading data

#fname = 'Sample_Comparables.csv'
#df = pd.read_csv(fname)

fname1 = 'classes.csv'
fname2 = 'keys.xlsx'

df1 = pd.read_csv(fname1, index_col='ID').reset_index()
df2 = pd.read_excel(fname2)

df2.head()


# In[4]:


#keywords = df2['Keywords-manual'].tolist()

df3 = df2.groupby('ID', as_index=False).agg(lambda x: list(x))
df3.head()


# In[5]:


keywords = df3['Keywords-manual'].tolist()
keywords[3]


# In[6]:


# using keywords as words for PMI

descriptions = keywords

print("total: ", len(descriptions))

# remove single word headlines
descriptions = [d for d in descriptions if len(d) > 1]
# show results
descriptions[0:1]


# In[7]:


# treating whole set of keywords as input
descriptions.append(sub_com_keywords)


# ### Unigrams

# In[8]:


# Comparable Company Unigrams
tok2indx = dict()
unigram_counts = Counter()
for ii, description in enumerate(descriptions):
    if ii % 5 == 0:
        print(f'finished {ii/len(descriptions):.2%} of descriptions')
    for token in description:
        unigram_counts[token] += 1
        if token not in tok2indx:
            tok2indx[token] = len(tok2indx)
indx2tok = {indx:tok for tok,indx in tok2indx.items()}
print('done')
print('vocabulary size: {}'.format(len(unigram_counts)))
print('most common: {}'.format(unigram_counts.most_common(10)))


# ### Skipgrams

# In[9]:


# Comparable Company Skipgrams
# note add dynammic window hyperparameter
back_window = 2
front_window = 2
skipgram_counts = Counter()
for idescription, description in enumerate(descriptions):
    for ifw, fw in enumerate(description):
        icw_min = max(0, ifw - back_window)
        icw_max = min(len(description) - 1, ifw + front_window)
        icws = [ii for ii in range(icw_min, icw_max + 1) if ii != ifw]
        for icw in icws:
            skipgram = (description[ifw], description[icw])
            skipgram_counts[skipgram] += 1    
    if idescription % 500 == 0:
        print(f'finished {idescription/len(descriptions):.2%} of descriptions')
        
print('done')
print('number of skipgrams: {}'.format(len(skipgram_counts)))
print('most common: {}'.format(skipgram_counts.most_common(30)))


# In[10]:


# 10 most common skip-grams
print(skipgram_counts.most_common(10))


# In[11]:


print("Number of Skipgrams: ", len(skipgram_counts))


# ### Word-Count Matrix

# In[12]:


row_indxs = []
col_indxs = []
dat_values = []
ii = 0
for (tok1, tok2), sg_count in skipgram_counts.items():
    ii += 1
    if ii % 500 == 0:
        print(f'finished {ii/len(skipgram_counts):.2%} of skipgrams')
    tok1_indx = tok2indx[tok1]
    tok2_indx = tok2indx[tok2]
        
    row_indxs.append(tok1_indx)
    col_indxs.append(tok2_indx)
    dat_values.append(sg_count)
    
wwcnt_mat = sparse.csr_matrix((dat_values, (row_indxs, col_indxs)))
print('done')


# In[13]:


# normalize word-count matrix
wwcnt_norm_mat = normalize(wwcnt_mat, norm='l2', axis=1)
#wwcnt_norm_mat


# ### Cosine Similarity

# In[14]:


def ww_sim(word, mat, topn=10):
    """find topn most similar words to word"""
    indx = tok2indx[word]
    
    # check type of 'mat'
    if isinstance(mat, sparse.csr_matrix):
        v1 = mat.getrow(indx)
    else:
        print("not sparse")
        v1 = mat[indx:indx+1, :]
    
    # using sklearn cosine similarity
    sims = cosine_similarity(mat, v1).flatten()
    sindxs = np.argsort(-sims)
    sim_word_scores = [(indx2tok[sindx], sims[sindx]) for sindx in sindxs[0:topn]]
    
    return sim_word_scores


# ### Pointwise Mutual Information Matrices
# 
# The pointwise mutual information (PMI) for a (word, context) pair in our corpus is defined as the probability of their co-occurrence divided by the probabilities of them appearing individually, 
# $$
# {\rm pmi}(w, c) = \log \frac{p(w, c)}{p(w) p(c)}
# $$
# 
# $$
# p(w, c) = \frac{
# f_{i,j}
# }{
# \sum_{i=1}^N \sum_{j=1}^N f_{i,j}
# }, \quad 
# p(w) = \frac{
# \sum_{j=1}^N f_{i,j}
# }{
# \sum_{i=1}^N \sum_{j=1}^N f_{i,j}
# }, \quad
# p(c) = \frac{
# \sum_{i=1}^N f_{i,j}
# }{
# \sum_{i=1}^N \sum_{j=1}^N f_{i,j}
# }
# $$
# where $f_{i,j}$ is the word-word count matrix we defined above.
# In addition we can define the positive pointwise mutual information as, 
# $$
# {\rm ppmi}(w, c) = {\rm max}\left[{\rm pmi(w,c)}, 0 \right]
# $$
# 
# Note that the definition of PMI above implies that ${\rm pmi}(w, c) = {\rm pmi}(w, c)$ and so this matrix will be symmetric.  
# 
# 
# <b>In the Datafox approach, they find (p(w,v)) by counting co-occurrences of words (w) and (v) in a <u>company’s keywords set</u>, while (p(w)) and (p(v)) are found from <u>total occurrences across all companies’ keywords.</u></b>
# 

# In[15]:


# using skip-grams of 2 window

num_skipgrams = wwcnt_mat.sum()
assert(sum(skipgram_counts.values())==num_skipgrams)

sum_over_words = np.array(wwcnt_mat.sum(axis=0)).flatten()
sum_over_contexts = np.array(wwcnt_mat.sum(axis=1)).flatten()

print(wwcnt_mat.sum(axis=0).shape)


# for creating sparce matrices
row_indxs = []
col_indxs = []

pmi_values = []
ppmi_values = []
spmi_values = []
sppmi_values = []


# In[16]:


ii = 0
# looping through all skip-grams of Comparables + Subject Company
for (w, v), sg_count in skipgram_counts.items():
    
    ii += 1
    if ii % 1000 == 0:
        print(f'finished {ii/len(skipgram_counts):.2%} of skipgrams')
    w_indx = tok2indx[w]
    v_indx = tok2indx[v]
    
    nwv = sg_count
    pwv = nwv / num_skipgrams
    
    nw = sum_over_contexts[w_indx]
    pw = nw / num_skipgrams
    
    nv = sum_over_words[v_indx]
    pv = nv / num_skipgrams

    pmi = np.log2(pwv/(pw*pv))
    ppmi = max(pmi, 0)
    
    row_indxs.append(w_indx)
    col_indxs.append(v_indx)

    pmi_values.append(pmi)
    ppmi_values.append(ppmi)
    
pmi_mat = sparse.csr_matrix((pmi_values, (row_indxs, col_indxs)))
ppmi_mat = sparse.csr_matrix((ppmi_values, (row_indxs, col_indxs)))


print('done')


# In[17]:


# dicts mapping of words and indices
w = 'France'
w_indx = tok2indx[w]
sum_over_contexts[w_indx], w_indx, indx2tok[w_indx]


# In[18]:


#print(pmi_mat)


# In[19]:


ww_sim('natural gas', pmi_mat)


# In[20]:


ww_sim('railway services', pmi_mat)


# ### Singular Value Decomposition (SVD)
# 
# With the PMI and PPMI matrices in hand, we can apply a singular value decomposition to create dense word vectors from the sparse ones we've been using. 

# In[21]:


# svd    
embedding_size = 25
uu, ss, vv = linalg.svds(pmi_mat, embedding_size) 

print('vocab size: {}'.format(len(unigram_counts)))
print('embedding size: {}'.format(embedding_size))
print('uu.shape: {}'.format(uu.shape))
print('ss.shape: {}'.format(ss.shape))
print('vv.shape: {}'.format(vv.shape))

unorm = uu / np.sqrt(np.sum(uu*uu, axis=1, keepdims=True))
vnorm = vv / np.sqrt(np.sum(vv*vv, axis=0, keepdims=True))

word_vecs = uu + vv.T
word_vecs_norm = word_vecs / np.sqrt(np.sum(word_vecs*word_vecs, axis=1, keepdims=True))


# In[22]:


ww_sim('natural gas', word_vecs_norm)


# In[23]:


ww_sim('railway services', word_vecs_norm, 50)


# ---
