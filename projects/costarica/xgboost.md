A number of configuration heuristics were published in the original gradient boosting papers. They can be summarized as:

    Learning rate or shrinkage (learning_rate in XGBoost) should be set to 0.1 or lower, and smaller values will require the addition of more trees.
    
    The depth of trees (tree_depth in XGBoost) should be configured in the range of 2-to-8, where not much benefit is seen with deeper trees.
    
    Row sampling (subsample in XGBoost) should be configured in the range of 30% to 80% of the training dataset, and compared to a value of 100% for no sampling.

These are a good starting point when configuring your model.

A good general configuration strategy is as follows:

    Run the default configuration and review plots of the learning curves on the training and validation datasets.
    
    If the system is overlearning, decrease the learning rate and/or increase the number of trees.
    
    If the system is underlearning, speed the learning up to be more aggressive by increasing the learning rate and/or decreasing the number of trees.

Credits: Jason @ ML Mastery jason@machinelearningmastery.com
