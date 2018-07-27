# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import nltk
from nltk.corpus import PlaintextCorpusReader

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory


raw_file = 'scripts.csv'
raw_file_na = 'scripts_nonascii.csv'
corpus_root = 'C://Python36//'
fname = 'dialogues_corpus.txt'

'''
# CHECK ENCODING
import codecs
import unicodedata
import chardet
print(chardet.detect(open(raw_file_na, "rb").read()))
# {'confidence': 0.9690625, 'encoding': 'utf-8'}
# {'encoding': None, 'confidence': 0.0, 'language': None}

# lines = codecs.open(raw_file_na, 'r', encoding='utf-8').readlines()
lines = codecs.open(raw_file_na, 'r', encoding='utf-8').readlines()
print(len(lines))
'''

# DATA ANALYSIS
# raw_data = pd.read_csv(raw_file, sep=',')
raw_data = pd.read_csv(raw_file_na, sep=',', encoding='utf-8')

print(raw_data.head())
'''
   Unnamed: 0 Character   ...      SEID  Season
0           0     JERRY   ...    S01E01     1.0
1           1     JERRY   ...    S01E01     1.0
2           2    GEORGE   ...    S01E01     1.0
3           3     JERRY   ...    S01E01     1.0
4           4    GEORGE   ...    S01E01     1.0

[5 rows x 6 columns]
'''

print(raw_data.tail(1))
'''
       Unnamed: 0 Character Dialogue  EpisodeNo    SEID  Season
54616       54616   PRAVEEN     '??'       24.0  S09E23     9.0
'''


print(raw_data.describe())
'''
         Unnamed: 0     EpisodeNo        Season
count  54616.000000  54616.000000  54616.000000
mean   27307.500000     11.360737      5.677732
std    15766.425488      6.757064      2.243955
min        0.000000      1.000000      1.000000
25%    13653.750000      5.000000      4.000000
50%    27307.500000     11.000000      6.000000
75%    40961.250000     17.000000      8.000000
max    54615.000000     24.000000      9.000000
'''

# sample count of George
count = 0
for x in raw_data['Dialogue']:
    if 'George' in str(x).split():
        count+=1
print(count)
# 551

dialogues = raw_data['Dialogue']
print(type(dialogues))
# <class 'pandas.core.series.Series'>


# Create Corpus!
with open(fname, 'w', encoding='utf-8') as f:
    for d in dialogues:
        f.write(str(d)+'\n')

filelist = PlaintextCorpusReader(corpus_root, fname)

print(filelist.fileids())
# ['dialogues_corpus.txt']

d_words = filelist.words(fname)

print(d_words)
# ['0', 'Do', 'you', 'know', 'what', 'this', 'is', 'all', ...]

print(type(d_words))
# <class 'nltk.corpus.reader.util.StreamBackedCorpusView'>

from nltk import word_tokenize as wt

def freq_words(file, min=1, num=10):
    text = open(file).read()
    tokens = wt(text)
    print(len(tokens))
    # 734989
    print(len(set(tokens)))
    freqdist = nltk.FreqDist(t for t in tokens if len(t) <= min)
    print(len(freqdist))
    # 4540
    # freqdist.plot()
    return freqdist.keys()

# fw = freq_words(fname, 4, 10)

# print(fw)

d_words = open(fname).read()
tokens = wt(d_words)

print(tokens[100:113])
# ['on', 'an', 'imaginary', 'phone', ')', 'Did', 'you', 'ring', '?', ',', 'I', 'cant', 'find-']

text = nltk.Text(tokens)
print(text)
# <Text: Do you know what this is all about...>

print(type(text))
# <class 'nltk.text.Text'>

print(text.collocations())
'''
n't know; n't want; 've got; New York; n't even; last night; n't
believe; would n't; 'll tell; 're gon; n't think; 'll see; Jerry
Seinfeld; could n't; whole thing; 're going; Uncle Leo; years ago; 've
never; Mr. Pitt
None
'''

# FREQUENCY DISTRIBUTION 
from nltk import FreqDist
fd1 = FreqDist(text)
# fd1.plot(10, cumulative=True)

# TAGGING
default_tagger = nltk.DefaultTagger('NN')
dtags = default_tagger.tag(tokens)

for item in dtags:
    if item[1] != 'NN':
        print(item)

'''
# REGULAR EXPRESSION PATTERNS

patterns = [
... (r'.*ing$', 'VBG'), # gerunds
... (r'.*ed$', 'VBD'), # simple past
... (r'.*es$', 'VBZ'), # 3rd singular present
... (r'.*ould$', 'MD'), # modals
... (r'.*\'s$', 'NN$'), # possessive nouns
... (r'.*s$', 'NNS'), # plural nouns
... (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
... (r'.*', 'NN') # nouns (default)
... ]
'''

# patterns = [(r'.*ing$', 'VBG'), (r'.*ed$', 'VBD'), (r'.*es$', 'VBZ'), (r'.*ould$', 'MD'), \
# (r'.*\'s$', 'NN$'), (r'.*s$', 'NNS'), (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), (r'.*', 'NN')]

patterns = [
    (r'.*ing$', 'VBG'),               # gerunds
    (r'.*ed$', 'VBD'),                # simple past
    (r'.*es$', 'VBZ'),                # 3rd singular present
    (r'.*ould$', 'MD'),               # modals
    (r'.*\'s$', 'NN$'),               # possessive nouns
    (r'.*s$', 'NNS'),                 # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'(The|the|A|a|An|an)$', 'AT'),   # articles 
    (r'.*able$', 'JJ'),                # adjectives 
    (r'.*ness$', 'NN'),                # nouns formed from adjectives
    (r'.*ly$', 'RB'),                  # adverbs
    (r'(He|he|She|she|It|it|I|me|Me|You|you)$', 'PRP'), # pronouns
    (r'(His|his|Her|her|Its|its)$', 'PRP$'),    # possesive
    (r'(my|Your|your|Yours|yours)$', 'PRP$'),   # possesive
    (r'(on|On|in|In|at|At|since|Since)$', 'IN'),# time prepopsitions
    (r'(for|For|ago|Ago|before|Before)$', 'IN'),# time prepopsitions
    (r'(till|Till|until|Until)$', 'IN'),        # time prepopsitions
    (r'(by|By|beside|Beside)$', 'IN'),          # space prepopsitions
    (r'(under|Under|below|Below)$', 'IN'),      # space prepopsitions
    (r'(over|Over|above|Above)$', 'IN'),        # space prepopsitions
    (r'(across|Across|through|Through)$', 'IN'),# space prepopsitions
    (r'(into|Into|towards|Towards)$', 'IN'),    # space prepopsitions
    (r'(onto|Onto|from|From)$', 'IN'),          # space prepopsitions    
    (r'\.$','.'), (r'\,$',','), (r'\?$','?'),    # fullstop, comma, Qmark
    (r'\($','('), (r'\)$',')'),             # round brackets
    (r'\[$','['), (r'\]$',']'),             # square brackets
    (r'(Sam)$', 'NAM'),
    # WARNING : Put the default value in the end
    (r'.*', 'NN')                      # nouns (default)
    ]

regexp_tagger = nltk.RegexpTagger(patterns)

rtags = regexp_tagger.tag(tokens[:1000])
print(rtags)

'''
# tokens[:100]
[('Do', 'NN'), ('you', 'NN'), ('know', 'NN'), ('what', 'NN'), ('this', 'NNS'), ('is', 'NNS
'), ('all', 'NN'), ('about', 'NN'), ('?', 'NN'), ('Do', 'NN'), ('you', 'NN'), ('know', 'NN
'), (',', 'NN'), ('why', 'NN'), ('were', 'NN'), ('here', 'NN'), ('?', 'NN'), ('To', 'NN'),
 ('be', 'NN'), ('out', 'NN'), (',', 'NN'), ('this', 'NNS'), ('is', 'NNS'), ('out', 'NN'),
('...', 'NN'), ('and', 'NN'), ('out', 'NN'), ('is', 'NNS'), ('one', 'NN'), ('of', 'NN'), (
'the', 'NN'), ('single', 'NN'), ('most', 'NN'), ('enjoyable', 'NN'), ('experiences', 'VBZ'
), ('of', 'NN'), ('life', 'NN'), ('.', 'NN'), ('People', 'NN'), ('...', 'NN'), ('did', 'NN
'), ('you', 'NN'), ('ever', 'NN'), ('hear', 'NN'), ('people', 'NN'), ('talking', 'VBG'), (
'about', 'NN'), ('We', 'NN'), ('should', 'MD'), ('go', 'NN'), ('out', 'NN'), ('?', 'NN'),
('This', 'NNS'), ('is', 'NNS'), ('what', 'NN'), ('theyre', 'NN'), ('talking', 'VBG'), ('ab
out', 'NN'), ('...', 'NN'), ('this', 'NNS'), ('whole', 'NN'), ('thing', 'VBG'), (',', 'NN'
), ('were', 'NN'), ('all', 'NN'), ('out', 'NN'), ('now', 'NN'), (',', 'NN'), ('no', 'NN'),
 ('one', 'NN'), ('is', 'NNS'), ('home', 'NN'), ('.', 'NN'), ('Not', 'NN'), ('one', 'NN'),
('person', 'NN'), ('here', 'NN'), ('is', 'NNS'), ('home', 'NN'), (',', 'NN'), ('were', 'NN
'), ('all', 'NN'), ('out', 'NN'), ('!', 'NN'), ('There', 'NN'), ('are', 'NN'), ('people',
'NN'), ('tryin', 'NN'), ('to', 'NN'), ('find', 'NN'), ('us', 'NNS'), (',', 'NN'), ('they',
 'NN'), ('dont', 'NN'), ('know', 'NN'), ('where', 'NN'), ('we', 'NN'), ('are', 'NN'), ('.'
, 'NN'), ('(', 'NN')]
'''

'''
# tokens[:1000] 
[('Do', 'NN'), ('you', 'PRP'), ('know', 'NN'), ('what', 'NN'), ('this', 'NNS'), ('is', 'NN
S'), ('all', 'NN'), ('about', 'NN'), ('?', '?'), ('Do', 'NN'), ('you', 'PRP'), ('know', 'N
N'), (',', ','), ('why', 'NN'), ('were', 'NN'), ('here', 'NN'), ('?', '?'), ('To', 'NN'),
('be', 'NN'), ('out', 'NN'), (',', ','), ('this', 'NNS'), ('is', 'NNS'), ('out', 'NN'), ('
...', 'NN'), ('and', 'NN'), ('out', 'NN'), ('is', 'NNS'), ('one', 'NN'), ('of', 'NN'), ('t
he', 'AT'), ('single', 'NN'), ('most', 'NN'), ('enjoyable', 'JJ'), ('experiences', 'VBZ'),
 ('of', 'NN'), ('life', 'NN'), ('.', '.'), ('People', 'NN'), ('...', 'NN'), ('did', 'NN'),
 ('you', 'PRP'), ('ever', 'NN'), ('hear', 'NN'), ('people', 'NN'), ('talking', 'VBG'), ('a
bout', 'NN'), ('We', 'NN'), ('should', 'MD'), ('go', 'NN'), ('out', 'NN'), ('?', '?'), ('T
his', 'NNS'), ('is', 'NNS'), ('what', 'NN'), ('theyre', 'NN'), ('talking', 'VBG'), ('about
....
('you', 'PRP'), ('to', 'NN'), ('analyze', 'NN'), ('a', 'AT'), ('hypothetical', 'NN'), ('ph
one', 'NN'), ('call', 'NN'), (',', ','), ('you', 'PRP'), ('know', 'NN'), (',', ','), ('fro
m', 'IN'), ('a', 'AT'), ('female', 'NN'), ('point', 'NN'), ('of', 'NN'), ('view', 'NN'), (
'.', '.'), ('(', '('), ('to', 'NN'), ('Claire', 'NN'), (')', ')'), ('Now', 'NN'), (',', ',
'), ('a', 'AT'), ('woman', 'NN'), ('calls', 'NNS'), ('me', 'PRP'), (',', ','), ('all', 'NN
'), ('right', 'NN'), ('?', '?'), ('Uh', 'NN'), ('huh', 'NN'), ('.', '.'), ('She', 'PRP'),
('says', 'NNS'), ('she', 'PRP'), ('has', 'NNS'), ('to', 'NN'), ('come', 'NN'), ('to', 'NN'
), ('New', 'NN'), ('York', 'NN'), ('on', 'IN'), ('business', 'NNS'), ('...', 'NN'), ('Oh',
 'NN'), ('you', 'PRP'), ('are', 'NN'), ('beautiful', 'NN'), ('!', 'NN'), ('...', 'NN'), ('
and', 'NN'), (',', ','), ('and', 'NN'), ('maybe', 'NN'), ('shell', 'NN'), ('see', 'NN'), (
'me', 'PRP'), ('when', 'NN'), ('she', 'PRP'), ('gets', 'NNS'), ('there', 'NN'), (',', ',')
, ('does', 'VBZ'), ('this', 'NNS'), ('woman', 'NN'), ('intend', 'NN'), ('to', 'NN'), ('spe
nd', 'NN'), ('time', 'NN'), ('with', 'NN'), ('me', 'PRP'), ('?', '?'), ('Id', 'NN'), ('hav
e', 'NN'), ('to', 'NN'), ('say', 'NN'), (',', ','), ('uuhh', 'NN'), (',', ','), ('no', 'NN
'), ('.', '.'), ('NO', 'NN'), ('.', '.'), (')', ')'), ('To', 'NN')]
'''


rtags_eval = regexp_tagger.evaluate([rtags])
print(rtags_eval)
# 1.0


from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
print(type(brown_tagged_sents))
# <class 'nltk.corpus.reader.util.ConcatenatedCorpusView'>

print(brown_tagged_sents)
'''
[[('The', 'AT'), ('Fulton', 'NP-TL'), ('County', 'NN-TL'), ('Grand', 'JJ-TL'), ('Jury', 'N
N-TL'), ('said', 'VBD'), ('Friday', 'NR'), ('an', 'AT'), ('investigation', 'NN'), ('of', '
IN'), ("Atlanta's", 'NP$'), ('recent', 'JJ'), ('primary', 'NN'), ('election', 'NN'), ('pro
duced', 'VBD'), ('``', '``'), ('no', 'AT'), ('evidence', 'NN'), ("''", "''"), ('that', 'CS
'), ('any', 'DTI'), ('irregularities', 'NNS'), ('took', 'VBD'), ('place', 'NN'), ('.', '.'
)], [('The', 'AT'), ('jury', 'NN'), ('further', 'RBR'), ('said', 'VBD'), ('in', 'IN'), ('t
erm-end', 'NN'), ('presentments', 'NNS'), ('that', 'CS'), ('the', 'AT'), ('City', 'NN-TL')
, ('Executive', 'JJ-TL'), ('Committee', 'NN-TL'), (',', ','), ('which', 'WDT'), ('had', 'H
VD'), ('over-all', 'JJ'), ('charge', 'NN'), ('of', 'IN'), ('the', 'AT'), ('election', 'NN'
), (',', ','), ('``', '``'), ('deserves', 'VBZ'), ('the', 'AT'), ('praise', 'NN'), ('and',
 'CC'), ('thanks', 'NNS'), ('of', 'IN'), ('the', 'AT'), ('City', 'NN-TL'), ('of', 'IN-TL')
, ('Atlanta', 'NP-TL'), ("''", "''"), ('for', 'IN'), ('the', 'AT'), ('manner', 'NN'), ('in
', 'IN'), ('which', 'WDT'), ('the', 'AT'), ('election', 'NN'), ('was', 'BEDZ'), ('conducte
d', 'VBN'), ('.', '.')], ...]
'''

brown_sents = brown.sents(categories='news')
print(type(brown_sents))
# <class 'nltk.corpus.reader.util.ConcatenatedCorpusView'>

rtags = regexp_tagger.tag(brown_sents[3])
print(rtags)
'''
[('``', 'NN'), ('Only', 'NN'), ('a', 'NN'), ('relative', 'NN'), ('handful', 'NN'), ('of',
'NN'), ('such', 'NN'), ('reports', 'NNS'), ('was', 'NNS'), ('received', 'VBD'), ("''", 'NN
'), (',', 'NN'), ('the', 'NN'), ('jury', 'NN'), ('said', 'NN'), (',', 'NN'), ('``', 'NN'),
 ('considering', 'VBG'), ('the', 'NN'), ('widespread', 'NN'), ('interest', 'NN'), ('in', '
NN'), ('the', 'NN'), ('election', 'NN'), (',', 'NN'), ('the', 'NN'), ('number', 'NN'), ('o
f', 'NN'), ('voters', 'NNS'), ('and', 'NN'), ('the', 'NN'), ('size', 'NN'), ('of', 'NN'),
('this', 'NNS'), ('city', 'NN'), ("''", 'NN'), ('.', 'NN')]
'''

# AFTER UPDATING PATTERNS
'''
[('``', 'NN'), ('Only', 'RB'), ('a', 'AT'), ('relative', 'NN'), ('handful', 'NN'), ('of',
'NN'), ('such', 'NN'), ('reports', 'NNS'), ('was', 'NNS'), ('received', 'VBD'), ("''", 'NN
'), (',', ','), ('the', 'AT'), ('jury', 'NN'), ('said', 'NN'), (',', ','), ('``', 'NN'), (
'considering', 'VBG'), ('the', 'AT'), ('widespread', 'NN'), ('interest', 'NN'), ('in', 'IN
'), ('the', 'AT'), ('election', 'NN'), (',', ','), ('the', 'AT'), ('number', 'NN'), ('of',
 'NN'), ('voters', 'NNS'), ('and', 'NN'), ('the', 'AT'), ('size', 'NN'), ('of', 'NN'), ('t
his', 'NNS'), ('city', 'NN'), ("''", 'NN'), ('.', '.')]
'''

rtags_eval = regexp_tagger.evaluate(brown_tagged_sents)
print(rtags_eval)
# 0.20326391789486245
# 0.4461085585854367














