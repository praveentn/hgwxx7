# pandas change order of columns
# last column as first column

# assuming you've a pandas dataframe df

cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]

df = df[cols]

# alternate way is by explicitly setting the order in cols

cols = [1,2,3,4]
df = df[cols]
