# viewing a random sample of the dataframe

# import libraries
import pandas as pd

# load dataframe
df = pd.read_csv('file')

# to display all columns in IDE's
pd.options.display.max_columns = len(df.columns)

# random sample of 15 rows
df.sample(15)
