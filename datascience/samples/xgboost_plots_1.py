# xgboost

import xgboost
from xgboost import plot_tree
from xgboost import XGBClassifier
import matplotlib.pyplot as plt

# fit model no training data
# assuming you've X and y
model = XGBClassifier()
model.fit(X, y)

# plot single tree
plot_tree(model)

# plot_importance
h,w = 13
fig, ax = plt.subplots(figsize=(h, w))
xgboost.plot_importance(model, ax=ax)
plt.show()
