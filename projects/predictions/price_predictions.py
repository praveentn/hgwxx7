
# coding: utf-8

# In[16]:


# import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression


# In[2]:


df_train = pd.read_csv("train.csv", index_col="Id", na_values="NA")
df_train.head()


# In[3]:


df_train.shape


# In[5]:


df_train.describe(include='all')


# In[6]:


df_train.corr()


# In[7]:


df_test = pd.read_csv("test.csv", index_col="Id", na_values="NA")


# In[8]:


df_test.describe(include='all')


# In[9]:


df = df_train.append(df_test)


# In[10]:


df.drop("SalePrice", axis=1, inplace=True)


# #### Feature Engineering

# In[11]:


# helper method to obtain all numerical/categorical features of a data frame
def get_features(df, feature_type):
    if feature_type == "num":
        return list(df.select_dtypes(include=["float", "int"]).columns)
    elif feature_type == "cat":
        return list(df.select_dtypes(include=["object"]).columns)
    else:
        raise ValueError("feature_type must be 'num' (numerical) or 'cat' (categorical).")


# In[12]:


num_features = get_features(df, "num")
num_features


# In[13]:


columns_with_na_values = df.columns[df.isnull().any()]
columns_with_na_values


# In[14]:


num_features_without_na = [x for x in num_features if x not in columns_with_na_values]

print("Numerical features without missing values in train.csv and test.csv:")
print(num_features_without_na)


# #### Visualization

# In[15]:


sns.regplot(x="GrLivArea", y="SalePrice", data=df_train)


# In[17]:


# helper method to compute the root mean squared error
def root_mean_squared_error(model, X, y_true):
    y_predict = model.predict(X)    
    return np.sqrt(mean_squared_error(y_predict, y_true))


# In[18]:


# Helper method to check performance of a model on 4 different sized training data sets.
def model_eval_helper(features, model):
    X = df_train[features].values
    y = np.ravel(df_train[["SalePrice"]].apply(np.log).values)
    n = len(df_train)

    X_train, X_val, y_train, y_val = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

    for train_size in np.linspace(0.1, 1, num=4):
        last = int(n * train_size)
        model.fit(X_train[:last], y_train[:last])
        score_out = root_mean_squared_error(model, X_val, y_val)
        score_in = root_mean_squared_error(model, X_train[:last], y_train[:last])
        print("")
        print("Using {} samples ({}%) of train.csv for training.".format(last, train_size * 100))
        print("Root mean squared logs error on validation data: {}".format(score_out))
        print("Root mean squared logs error on training data: {}".format(score_in))


# In[19]:


print("Training linear regression model with feature 'GrLivArea'.")
model_eval_helper(["GrLivArea"], LinearRegression())


# In[21]:


# helper function to display correlation matrices
def corr_helper(features=None, min_corr=0, max_corr=1, draw=True):
    if not features:
        features = list(df_train.columns.values)
    
    if "SalePrice" in features:
        features.remove("SalePrice")
    
    corr = pd.DataFrame(df_train[["SalePrice"] + features].corr())
    corr = corr[(corr["SalePrice"].abs() >= min_corr) & (corr["SalePrice"].abs() <= max_corr)]
    selected_features = corr.index.values
    corr = corr[selected_features]

    if draw:
        f, ax = plt.subplots(figsize=(15, 10))
        sns.heatmap(corr, annot=True, fmt=".2f")
        
    selected_features = list(selected_features)
    
    if "SalePrice" in selected_features:
        selected_features.remove("SalePrice")
        
    return selected_features


# In[22]:


selected_features = corr_helper(features=num_features_without_na, min_corr=0.1)


# Only feature 'OverallQual' has a higher correlation to 'SalePrice' than 'GrLivArea'. According to the description, 'OverallQual' rates the overall material and finish of the house. There are other features like '1stFlrSF', '2ndFlrSF' and 'TotRmsAbvGrd' that strongly correlate to the sale price, but they also strongly correlate to 'GrLivArea' - which makes sense.

# In[23]:


sns.regplot(x="OverallQual", y="SalePrice", data=df_train)


# ### Imputation

# In[25]:


columns_with_na_values = df.columns[df.isnull().any()]
columns_with_na_values


# In[26]:


print("{} of {} features have missing values.".format(len(columns_with_na_values), len(df.columns)))
print(df[columns_with_na_values].isnull().sum())


# In[27]:


cat_features = get_features(df, "cat")
cat_features


# In[28]:


none_values = ["Alley", "BsmtQual", "BsmtCond", "FireplaceQu", "Utilities", "BsmtExposure", "BsmtFinType1", "BsmtFinType2", "GarageType", "GarageFinish", 
               "Fence", "MiscFeature", "PoolQC", "GarageCond", "GarageQual", "KitchenQual", "MasVnrType"]
none_values


# In[29]:


df[none_values] = df[none_values].fillna("None")


# In[30]:


cat_features_with_na_values = df[cat_features].columns[df[cat_features].isnull().any()]
cat_features_with_na_values


# In[31]:


print("Remaining categorical features with missing values:")
print(df[cat_features_with_na_values].isnull().sum())


# In[32]:


average_value_map = {"Electrical": "Mix", "Exterior1st": "Other", "Exterior2nd": "Other", "Functional": "Mod", 
                     "MSZoning": "Oth", "SaleType": "Oth"}
average_value_map


# In[33]:


for col, value in average_value_map.items():
    df_train[col] = df_train[col].fillna(value)
    df_test[col] = df_test[col].fillna(value)
    df[col] = df[col].fillna(value)


# In[34]:


cat_features_with_na_values = df[cat_features].columns[df[cat_features].isnull().any()]
print("Number of categorical features with missing values: {}".format(len(cat_features_with_na_values)))


# In[35]:


num_features = get_features(df, "num")
num_features


# In[36]:


num_features_with_na_values = df[num_features].columns[df[num_features].isnull().any()].values
num_features_with_na_values


# In[37]:


print("{} of {} numerical features have missing values:".format(len(num_features_with_na_values), len(num_features)))
print(df[num_features_with_na_values].isnull().sum())


# In[38]:


none_values = ["BsmtFinSF1", "BsmtFinSF2", "BsmtFullBath", "BsmtHalfBath", "BsmtUnfSF", "GarageArea", "GarageCars", 
               "LotFrontage", "MasVnrArea", "TotalBsmtSF"]
none_values


# In[39]:


df[none_values] = df[none_values].fillna(0)


# In[41]:


df[none_values].head()


# In[42]:


num_features_with_na_values = df.columns[df.isnull().any()].values
num_features_with_na_values


# In[43]:


print("Columns with missing values:")
print(num_features_with_na_values)


# In[44]:


df.drop("GarageYrBlt", axis=1, inplace=True)
print("Removed feature 'GarageYrBlt'.")


# In[45]:


features_with_na_values = df.columns[df.isnull().any()]
print("Number of features with missing values: {}".format(len(features_with_na_values)))


# In[48]:


train_size = len(df_train)
train_size


# In[49]:


# helper method to update df_train and df_test according to df.
def update_dfs(df, features=None):
    global df_train, df_test
    if not features:
        features = df.columns
    
    targets = df_train["SalePrice"]
    df_train = df[:train_size][features]
    df_train["SalePrice"] = targets
    df_test = df[train_size:][features]


# In[50]:


update_dfs(df)

print("There are {} rows in df_train.".format(len(df_train)))
print("There are {} rows in df_test.".format(len(df_test)))


# ### III. Converting Categorical Features to Numerical Features

# #### Categorical Features with a Natural Order
# 

# In[51]:


# helper function to convert a categorical feature into a numerical one.
def make_numerical(features, transform):
    if not isinstance(features, list):
        features = [features]
        
    features = list(df[features].select_dtypes(include=["object"]).columns)
    df[features] = df[features].replace(transform)


# In[54]:


condition_rated_features = ["ExterQual", "ExterCond", "BsmtQual", "BsmtCond", "HeatingQC", "KitchenQual", 
                            "FireplaceQu", "GarageQual", "GarageCond", "PoolQC"]

print("Example row before transformation:")
print(df[condition_rated_features].head())


# In[55]:


make_numerical(condition_rated_features, {"None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5})

print("")
print("After feature transformation:")
print(df[condition_rated_features].head())


# In[56]:


remaining_cat_features = get_features(df, "cat")
print("Remaining categorical features:")
print(remaining_cat_features)


# In[57]:


make_numerical("Utilities", {"None": 0, "ELO": 1, "NoSeWa": 2, "NoSewr": 3, "AllPub": 4})
make_numerical("LandSlope", {"Gtl": 1, "Mod": 2, "Sev": 3})
make_numerical("LotShape", {"Reg": 0, "IR1": 1, "IR2": 2, "IR3": 3})
make_numerical("BsmtExposure", {"None": 0, "No": 1, "Mn": 2, "Av": 3, "Gd": 4})
make_numerical("BsmtFinType1", {"None": 0, "Unf": 1, "LwQ": 2, "Rec": 3, "BLQ": 4, "ALQ": 5, "GLQ": 6})
make_numerical("BsmtFinType2", {"None": 0, "Unf": 1, "LwQ": 2, "Rec": 3, "BLQ": 4, "ALQ": 5, "GLQ": 6})
make_numerical("CentralAir", {"N": 0, "Y": 1})
make_numerical("Functional", {"Typ": 7, "Min1": 6, "Min2": 5, "Mod": 4, "Maj1": 3, "Maj2": 2, "Sev": 1, "Sal": 0})
make_numerical("GarageFinish", {"None": 0, "Unf": 1, "RFn": 2, "Fin": 3})
make_numerical("PavedDrive", {"N": 0, "P": 1, "Y": 2})


# In[60]:


update_dfs(df)
df.describe(include='all')


# In[61]:


new_num_features = list(set(cat_features) - set(remaining_cat_features))
new_num_features


# In[62]:


selected_features = corr_helper(features=new_num_features)


# #### Categorical Features without a Natural Order

# In[64]:


remaining_cat_features = get_features(df, "cat")
print("Remaining categorical features:")

remaining_cat_features


# ##### sale price distribution for a few neighborhoods

# In[65]:


def plot_helper(df, feature, limit=None, y_max=0.00002, height=4):
    labels = df[feature].unique()
    f, ax = plt.subplots(figsize=(15, height))
    
    if not limit:
        limit = len(labels)
        
    for label in labels[:limit]:
        sns.kdeplot(df[df_train[feature] == label]["SalePrice"], label=str(label))

    plt.yticks([0, y_max])


# In[66]:


plot_helper(df_train, "Neighborhood", limit=5)


# Prices in North Ridge are significantly higher on average than in Mitchell for example.

# list of all neighborhoods and the average sale price for a house in this neighborhood.

# In[67]:


# helper method to display the average price for the different values of a feature
def avg_price(feature):
    df_avg_price = df_train[[feature, "SalePrice"]].groupby(feature).mean().sort_values("SalePrice")
    df_avg_price["NumberOfHouses"] = df_train[[feature]].groupby(feature).size()
    return df_avg_price


# In[68]:


avg_price_neighborhood = avg_price("Neighborhood")
print(avg_price_neighborhood)


# Northridge actually has the highest prices on average compared to all other neighborhoods.
# 
# If we want to use feature "Neighborhood" for a future model, it would make sense to group some of the neighborhoods before generating one-hot-encodings for this feature in order to reduce the dimensionality. Another way would be to assume an order on the neighborhoods based on the average sale price. This way, we can convert this feature the same way we did in the previous section.

# In[69]:


neighborhood_dict = {}
for num, name in enumerate(avg_price_neighborhood.index):
    neighborhood_dict[name] = num
    
neighborhood_dict


# In[70]:


make_numerical("Neighborhood", neighborhood_dict)


# In[71]:


df["FencePrivacy"] = df["Fence"]
df["FenceWood"] = df["Fence"]

df.drop("Fence", axis=1, inplace=True)

make_numerical("FencePrivacy", {"GdPrv": 2, "MnPrv": 1, "GdWo": 0, "MnWw": 0, "None": 0})
make_numerical("FenceWood", {"GdPrv": 0, "MnPrv": 0, "GdWo": 2, "MnWw": 1, "None": 0})
print("Created features 'FencePrivacy' and 'FenceWood' and removed feature 'Fence'.")


# In[72]:


print("We currently have {} numerical features.".format(len(get_features(df, "num"))))


# In[73]:


remaining_cat_features = get_features(df, "cat")
print("We have {} unused features that can be one-hot-encoded:".format(len(remaining_cat_features)))

remaining_cat_features


# In[75]:


# We will keep track of all one-hot-encoded features in a list so that we can remove them at the end.

encoded_features = set()


# In[76]:


count = 0

for f in remaining_cat_features:
    len_uniques = len(pd.get_dummies(df[f]).columns)
    count += len_uniques
    print("One-hot-encoding of feature '{}' would generate {} new features".format(f, len_uniques))
    
print("")
print("Total number of potentially generated features: {}".format(count))


# We can actually bring this number down a bit. In my opinion, it makes sense to create combined one-hot-encodings for the feature pairs ('Condition1', 'Condition2') and ('Exterior1st', 'Exterior2nd').
# 
# There are some misspellings in 'Exterior1st' and 'Exterior2nd'. We should correct those before encoding the features.

# In[77]:


print(df["Exterior1st"].unique())
print(df["Exterior2nd"].unique())

df[["Exterior1st", "Exterior2nd"]] = df[["Exterior1st", "Exterior2nd"]].replace("Wd Shng", "WdShing")
df[["Exterior1st", "Exterior2nd"]] = df[["Exterior1st", "Exterior2nd"]].replace("Brk Cmn", "BrkComm")
df[["Exterior1st", "Exterior2nd"]] = df[["Exterior1st", "Exterior2nd"]].replace("CemntBd", "CmentBd")

print("")
print("Corrected misspellings.")
same_values = set(df["Exterior1st"].unique()) == set(df["Exterior2nd"].unique())
print("'Exterior1st' and 'Exterior2nd' have the same values: {}".format(same_values))


# In[78]:


# helper method to create one-hot-encodings of features.
def one_hot_encode(df, features, prefix=None):   
    global encoded_features
    if not isinstance(features, list):
        features = [features]
    
    if not set(features) <= set(df.columns.values):
        print("Not all features are columns in data frame.")
        return None
    
    dummies = pd.get_dummies(df[features[0]], prefix=prefix).columns.values
    df_dummies = pd.DataFrame(0, index=df.index, columns=dummies)
    df[dummies] = df_dummies
    
    for f in features:
        df[dummies] = df[dummies] + pd.get_dummies(df[f], prefix=prefix)
        
    df[dummies] = df[dummies].apply(lambda x: x > 0).astype(int)
    encoded_features = encoded_features | set(features)
    return list(dummies)


# In[79]:


print("Created combined one-hot-encoding for 'Condition1' and 'Condition2'. New features:")
print(one_hot_encode(df, ["Condition1", "Condition2"], "Condition"))


# In[80]:


print("Created combined one-hot-encoding for 'Exterior1st' and 'Exterior2nd'. New features:")
print(one_hot_encode(df, ["Exterior1st", "Exterior2nd"], "Exterior"))


# In[81]:


remaining_cat_features = [x for x in remaining_cat_features if x not in encoded_features]
remaining_cat_features


# In[82]:


new_features = []

for feature in remaining_cat_features:
    features = one_hot_encode(df, feature, prefix=feature)        
    new_features = new_features + features
    
print("Generated {} new features.".format(len(new_features)))


# Here is another correlation matrix of the newly generated features that have an absolute correlation of at least 0.2 to 'SalePrice'.

# In[83]:


update_dfs(df)


# In[84]:


one_hot_enc_20_percent_corr = corr_helper(new_features, min_corr=0.2)


# ##### Adding new features
# 
# Let's try to come up with completely new features by combining some of the available features. 
# 
# I can imagine that the average room size of a house might have an impact on its sale price.

# In[85]:


df["AvgRoomSize"] = df["GrLivArea"] / df["TotRmsAbvGrd"]
print("Created feature 'AvgRoomSize'.")


# In[86]:


# Another feature that might be interesting are the sums of all condition and quality ratings.

ratings_qual = ["OverallQual", "ExterQual", "BsmtQual", "HeatingQC", "KitchenQual", "FireplaceQu", "GarageQual",
               "PoolQC"]
ratings_cond = ["OverallCond", "ExterCond", "BsmtCond", "HeatingQC", "GarageCond"]

df["SumQualCond"] = 0

for item in ratings_qual + ratings_cond:
    df["SumQualCond"] = df["SumQualCond"] + df[item]


# In[87]:


final_features = get_features(df, "num")
print("There are {} numerical features.".format(len(final_features)))

# we only want the final features in the data for our final model
update_dfs(df, final_features)

print("There are {} rows in df_train.".format(len(df_train)))
print("There are {} rows in df_test.".format(len(df_test)))


# In[88]:


features_40_percent_sale_price_corr = corr_helper(min_corr=0.4)


# ## V. Developing a Sophisticated Regression Model
# 
# Just for comparison, let's see how a simple linear regression model performs with the features that we created in the previous sections.

# In[89]:


model_eval_helper(final_features, model=LinearRegression())


# In[90]:


print("Training linear regression model with features:")
print(features_40_percent_sale_price_corr)
model_eval_helper(features_40_percent_sale_price_corr, LinearRegression())


# Again, we should have scaled our data before we trained our linear regression model. But since we won't use linear regression models from now on, we will skip scaling the data.

# ### GradientBoostingRegressor
# 
# Now we'll use a more GradientBoostingRegressor as a more sophisticated model. Ensemble methods like GradientBoostingRegressor usually perform extremely good in Kaggle competitions. Further, we don't have to worry about feature scaling and having too many features.

# In[92]:


from sklearn.ensemble import GradientBoostingRegressor


# In[93]:


reg = GradientBoostingRegressor(n_estimators=200, max_depth=2)
reg


# In[94]:


model_eval_helper(final_features, model=reg)


# In[95]:


df_importances = pd.DataFrame(reg.feature_importances_, index=final_features, columns=["Importance"])
df_importances.sort_values("Importance", ascending=False, inplace=True)

print(df_importances)


# Both in and out of sample error went down dramatically. And interestingly, 'GrLivArea' actually seems to be the most important feature for predicting the sale price. 
# 
# There are a few features that are completely useless for our model.

# In[96]:


useful_features = df_importances[df_importances["Importance"] > 0].index.values
print("{} of {} features had an importance greater than 0.0 for GradientBoostingRegressor:".format(
    len(useful_features), len(df_train.columns)))
print(useful_features)


# In[97]:


print("")
useless_features = df_importances[df_importances["Importance"] == 0].index.values
print("The following features had importance 0.0 for GradientBoostingRegressor:")
print(useless_features)


# ### Parameter Tuning

# In[98]:


from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import ShuffleSplit


# In[99]:


param_grid = [{"max_depth": [2, 3],
               "n_estimators": [300, 500, 750],
               "max_features": ["sqrt", "auto"]}]
param_grid


# In[100]:


cv = ShuffleSplit(n_splits=3, test_size=0.1, random_state=0)
cv


# In[101]:


model = GradientBoostingRegressor(random_state=0)
model


# In[102]:


grid_search = GridSearchCV(model, param_grid, cv=cv, scoring="neg_mean_squared_error", n_jobs=-1)
grid_search


# In[103]:


X_train = df_train.drop("SalePrice", axis=1).values
y_train = np.ravel(df_train[["SalePrice"]].apply(np.log).values)

X_train, y_train


# In[104]:


print("Training models...")
grid_search.fit(X_train, y_train)
print("Finished training models.")


# In[105]:


print("Best estimator:")
print(grid_search.best_estimator_)

rmse = np.sqrt(np.abs(grid_search.best_score_))
print("Best estimator score: {}".format(rmse))


# ### Predictions

# In[106]:


best_model = grid_search.best_estimator_
best_model


# In[109]:


X_predict = df_test.values
X_predict


# In[110]:


y_predict = best_model.predict(X_predict)
y_predict


# In[111]:


# rescale back from logarithmic price range.
y_predict = np.exp(y_predict)
y_predict


# In[112]:


df_pred = pd.DataFrame(y_predict, index=df_test.index, columns=["SalePrice"])
df_pred.to_csv("predictions.csv")

print("Created predictions. Showing five sample rows of 'predictions.csv':")
print(df_pred.head())

