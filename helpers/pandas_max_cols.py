# how to display all columns by default
# when you're using Jupyter QtConsole or Notebook or any other IDE's

import pandas as pd

df = pd.read_csc('file')

# set the max_columns equal to the number of columns
pd.options.display.max_columns = len(df.columns)

# you'll be able to see all columns now
df.head()
