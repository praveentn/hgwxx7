SMOTE - Oversampling - knn - minority class - in-between

Disadvantage - lack of Jitter - the variation in periodicity of a signal or periodic event from its target or true frequency.

This is an artifact of the SMOTE algorithm, and is problematic because it introduces a feature into the dataset, this "point bridge", which doesn't actually exist in the underlying dataset.

This tendancy of SMOTE to connect inliers and outliers is the algorithm's primary weakness in practice. It limits the algorithm's applicability to datasets with sufficiently few samples and/or sufficiently sparse point clouds. When applying SMOTE to your own data, make sure to take a good hard look at whether or not it's doing what you expect it to be doing.

kind='borderline1' and kind='borderline2' are one class of adaptations. These will classify points are being noise (all nearest neighbors are of a different class), in danger (half or more nearest neighbors are a different class), or safe (all nearest neighbors are of the same class). Only points in danger will be sampled in step one of the algorithm. Then, on step two of the algorithm, instead of selecting a point from n_neighbors belonging to the same class, 
	• borderline1 will select a point from the five nearest points not belonging to the given point's class, 
	• while borderline2 will select a point from the five nearest points of any class.

