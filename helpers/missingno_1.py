# missing values

# load libraries
import missingno as msno
import matplotlib.pyplot as plt

train_df.isnull().sum()[train_df.isnull().sum() > 0]
# output of these - columns, are fed to msno matrix

msno.matrix(train_df[['v2a1', 'v18q1', 'rez_esc', 'meaneduc', 'SQBmeaned']], color = (0.211, 0.215, 0.274))

plt.show()
