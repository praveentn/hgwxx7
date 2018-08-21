# dict to dataframe
d = {'Sex': ['F', 'F', 'M', 'M'], 
      'Size': ['S', 'L', 'S', 'L'], 
      'Age': [10, 48, 24, 35]}
      
df = pd.DataFrame(d)
df
  Sex Size  Age
0   F    S   10
1   F    L   48
2   M    S   24
3   M    L   35

# get data types
df.dtypes
Sex     object
Size    object
Age      int64
dtype: object

# get categories
pd.Categorical(d['Sex'])
[F, F, M, M]
Categories (2, object): [F, M]

# get categorical indices
pd.CategoricalIndex(df)
CategoricalIndex(['Sex', 'Size', 'Age'], categories=['Age', 'Sex', 'Size'], 
                  ordered=False, dtype='category')

pd.CategoricalIndex(df['Sex'])
CategoricalIndex(['F', 'F', 'M', 'M'], categories=['F', 'M'], ordered=False, 
                  name='Sex', dtype='category')

pd.CategoricalIndex(df['Sex'] == 'M')
CategoricalIndex([False, False, True, True], categories=[False, True], 
                  ordered=False, name='Sex', dtype='category')

type(pd.CategoricalIndex(df['Sex'] == 'M'))
<class 'pandas.core.indexes.category.CategoricalIndex'>

x = pd.CategoricalIndex(df['Sex'] == 'M')
x
CategoricalIndex([False, False, True, True], categories=[False, True], 
                  ordered=False, name='Sex', dtype='category')

x[0]
False

x[2]
True

x.categories
Index([False, True], dtype='object')

len(x.categories)
2


# categorical to continuous
pd.get_dummies(df)
   Age  Sex_F  Sex_M  Size_L  Size_S
0   10      1      0       0       1
1   48      1      0       1       0
2   24      0      1       0       1
3   35      0      1       1       0

# pandas factorize
# categorical to continuous
pandas.factorize(values, sort=False, na_sentinel=-1, size_hint=None)

pd.factorize(df.Sex)
(array([0, 0, 1, 1], dtype=int32), Index(['F', 'M'], dtype='object'))

pd.factorize(df.Size)
(array([0, 1, 0, 1], dtype=int32), Index(['S', 'L'], dtype='object'))

pd.factorize(['b', None, 'a', 'c', 'b', np.nan])
(array([ 0, -1,  1,  2,  0, -1], dtype=int32), array(['b', 'a', 'c'], dtype=object))

pd.factorize(['b', None, 'a', 'c', 'b', np.nan, 0, 1])
(array([ 0, -1,  1,  2,  0, -1,  3,  4], dtype=int32), 
        array(['b', 'a', 'c', 0, 1], dtype=object))
        
pd.factorize(['b', None, 'a', 'c', 'b', np.nan, 0, 1])[0]
array([ 0, -1,  1,  2,  0, -1,  3,  4], dtype=int32)

pd.factorize(['b', None, 'a', 'c', 'b', np.nan, 0, 1])[1]
array(['b', 'a', 'c', 0, 1], dtype=object)


df
           model    type  cost
0  Peter England    coir    20
1         Turtle   linen    30
2         Levi's  cotton    40
3     Van Heusen    coir    50

df[df['model'].str.contains('an')]
           model   type  cost
0  Peter England   coir    20
3     Van Heusen   coir    50

df[df['model'].str.match('an')]
Empty DataFrame
Columns: [model, type, cost]
Index: []







