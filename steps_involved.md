# Data Science | Machine Learning

## Summary of steps
	1) Understand the problem, type etc.
	2) Handling data
	3) Exploratory Data Analysis
	4) Statistical Modeling + Hypothesis Testing
	5) Feature engineering to create a dataset for machine learning
	6) Compare several baseline machine learning models
	7) Try more complex machine learning models
	8) Optimize the selected model
	9) Investigate model predictions in context of problem
	10) Draw conclusions and lay out next steps
---
#### Note: report findings and observations at each stage, textually or visually
---

1) Understand the problem, type etc.
	- problem statement
	- type of problem
		- by examining the features and target(s)
		- Whether regression, classification, clustering etc.
		- supervised, unsupervised, reinforcement etc.
		- one class, multi-class classification
		- novelty detection
		- continuous variable prediction
	- model types
		- logical, geometric or probabilistic
	- study the data
	- prepare data dictionary
	- create a spreadsheet (for quick reference)
		- Variable: name
		- Type: num or cat
		- Relation: any relation with other columns
		- Target: variable to predict
			- measure skewness
			- kurtosis
			- fill df.describe(inc all)
			- correlations
			- 
		- Comment: things to keep track of going forward
		- 
	- whether adequate data is available
	- metrics
		- <i>list the questions that needs to be answered</i>
		- <i>what needs to be measured?</i>
		- f1 score
		- ROC curve
		- precision
		- recall
		- accuracy
		- R2 score
		- 
	
2) Handling data
	- memory
	- cpu requirements
	- import required libraries
	- load data -> pandas + dataframe
		- csv, excel, hdfs, stata etc.
		- chunksize, nrows, low_memory
		- missing value treatment while loading (na_values)
		- missingno
		- 
		
	- 4C's
		- cleaning (anomalies, outliers)
		- completing (missing)
		- converting (data types)
		- creating (featur engg.)
		
	- missing values
		- imputation
		- check the importance of outliers/anomalies
		- strategy for treating missing values
			- use Imputer from sklearn.preprocessing
			- ffill, bfill, mean, map(key:value)
			- df = df.groupby(df.columns, axis = 1).transform(lambda x: x.fillna(x.mean()))
	- strategy for handling outliers
		- cause of outliers
		- uni/bi variate outliers
		- 2-3 times less or more than S.Dev
		- 1.5-2 times IQR
		- exclude points below 5th percentiles & above 95th 
		- 
        
3) Exploratory Data Analysis
	- to learn what data can tell us
	- Data mining to gain unknown insights
	- analyzing data sets to summarize their main characteristics, often with visual methods
		- central tendency
		- standard deviation
		- measure of dispersion
		- measure of spread (variance)
	- heatmap of correlation
	- univariate analysis
	- bivariate analysis
	- multivariate analysis
	- find the skewness
		- might be required to transform
	- data cleaning and wrangling (tidying)
	- correlation
		- df.corr() or seaborn heatmap
		- Pearson's
		- Spearman's
		- Kendall's rank (tau)
		- 
	- distribution
		- df.hist()
	- density dist
		- df.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
	- scatter matrix of df
	- summarization
	- visualization
		- bar, hist, box, scatter, pair, facetgrid, 
		- kdeplot, heatmap, line, area, dispersion,
		- lmplot, regplot, jointplot, catplot, gridspecs
		- 
		
	- identifying errors in data
		- finding the relation between columns is key to identify errors
		- eg. age, gender, dates, year, height, weight and so on
		- check whether the values are appropriate
		- whether common data is same for a particular set of rows (grouped by id for ex.)
		- also, similar columns -> age is null but dob is available!
		- state is present but country is not
		- income of individual members in a household are present but net income is missing
		- 
		
	- encoding
		- note label encoded data
		- check the MSE and other errors before and after encoding
		- for different random_state's
		- before encoding, ensure that missing values are handled
	- get_dummies(<pandas dataframe>)
	- factorize columns (<pd.factorize(df['Gender'])>)
	- label encoding
	- arbitrary ordering
	- one hot encoding
	- non-arbitrary encoding
	- DictVectorizer
	- binary encoder
	- judicious combination of OHE with PCA for dim. red. can seldom be beat by other encoding schemes 
	- inverse_transform 
		- going back from numerical to string

4) Statistical Modeling + Hypothesis Testing
	- perform required statistical tests
	- to reach valid conclusions (rather than predictions ~ ML)
	- chi-squared
		- test whether two categorical variables are related or independent
	- t-test
		- whether the means of 2 independent samples are significantly different
	- ANOVA
		- whether the means of 3 or more independent samples are significantly different
	- multi-colinearity
		- Condition number in statsmodels.api OLS summary
	- OLS summary
		- sm.OLS(y, X).fit(), summary

	##### 1st table
		- Dependent variable
		- Number of observations
		- Degrees of freedom
		- R-squared
			- percentage of variance, ie., if R²=93.5% then the
		  		model explains 93.5% of the variance in our dependent variable
			- adding variables to a regression model, in turn increases R²
			- 
		
	##### 2nd table
		- coef of Independent variables ()
    			- as IV's inc by 1, DV reduces by the corresponding value
		- Standard error
			- standard deviation of test statistic (eg. mean)
		- t-score
			- significance for hypothesis test
		- p-values
			- significance for hypothesis test
		- confidence intervals
			- with 95% confidence we predict 
				that IV's lies between the two values for 0.025 and 0.975
	
	##### 3rd table
		- Condition number
			- larger value indicates multicolinearity
			- values over 20 are to be concerned of
		- 
		
5) Feature engineering
	- make sure data is as relevant to the task as possible
	- different types
	- identifying relevant features
	- creating new features
	- polynomial features
	- degree of the polynomial
		- as degree increases, so does overfitting
	- interaction terms (eg. features x1, x2 -> x1*x2^2)
	- domain knowledge features
	
	- Standardization
		- StandardScaler
	- Normalization
		- MinMaxScaler
	- PCA
		- finds dimensions of greatest variation
	- ICA
		- separate a mutltivariate signal into independent signals
	- Linear Discriminant Analysis
		- supervised dimensionality reduction technique
		- similar to PCA, +advantage of tackling overfitting
	- SelectPercentile
	- Combine features 
	- Collinear features
	- Ignore unwanted features
	- Data with low variance can't help in prediction
	- Dimensionality reduction with t-SNE
		- t-Distributed Stochastic Neighbor Embedding (t-SNE)
	- UMAP
		- maps data to a low-dimensional manifold but tries to preserve more global structure than t-SNE

    	
6) Comapre Models
    - choice of algorithms
    - advantages
    - disadvantages
    
    Train test split
    	- random state
    	- test size
    	- cross validation cv
        	- shuffle split
        	- GridSearchCV
        	- cross_val_score
        	- 
    - calibration
    - plot feature importances
    	- RandomForestClassifier().feature_importances_
    - 

7) Complex Models
	- Train and test
	- Predict
	- Measure Accuracy
		- mean_squared_error
		- r2_score
		- confusion_matrix
		- 
	- baseline model
	- improved model
	- model interpretations
	- feature importances
		- xgboost
		- random forest
		- 
	- Cost function
		- Gradient Descent

8) Optimization
    - extracting the best performance from a machine learning model 
    - by tuning the hyperparameters through cross-validation
    - Manual
    - GridSearch
    - Random Search
    - Automated optimization
    	- hyperopt
	- 
    - Retrain
    - Overfitting/underfitting
	- underfitting - a decision boundary that hasn't latched onto the true border enough, 
		 ie., when it doesn't take into consideration enough information to accurately model the actual data
	- overfitting - as opposed to being too tightly wrapped against individual points
    		- it's observed numerically when the testing error does not reflect the training error
		- model has too many parameters, it is susceptible to overfitting
		- avoid overfitting by adding more iterations/more parameters
    - 

9) Investigate model predictions in context of problem

   a) Reducing Variance in final model
	- sources of variance
		- noise in training data
		- randomness of ML algorithm
	- measure Variance introduced by algorithm
		- repeated runs
	- measure Variance introduced by training data
		- train on different samples
	- ensemble models
	- sensitivity analysis
	- more training data
	- 

    Also, note 
    
    *  Optimizing errors/loss functions
	- cross entropy
	- MSE
	- 

    *  ROC curve - FP vs TP
	- guessing model will have ROC of 0.5
	- 
	
    *  Precision = TP / (TP + FP)
    *  Recall    = TP / (TP + FN)
    *  Confusion matrix 
	    PY   PN
	AY  [TP, FP]
	AN  [FN, TN]
 
    *  True +ve, False +ve
 
    *  Model fit and transform
 
    *  Variable transformation
    	- scale data
    	- symmetric distribution
    	- complex non-linear relationships into linear relationships
    	- 

    * tuning classifiers - stacking
		- n_estimators: Number of classification trees in your learning model ( set to 10 per default)
		- max_depth: Maximum depth of tree, or how much a node should be expanded. Beware if set to too high a number would run the risk of overfitting as one would be growing the tree too deep
		- verbose: Controls whether you want to output any text during the learning process. A value of 0 suppresses all text while a value of 3 outputs the tree learning process at every iteration.
    
    * Relation between RMSE and MAE
		- Mean Square Error or RMSE & Mean Absolute Error
		- MSE has more statistical grounding with variance
		- MAE is more intuitive and less sensitive to outliers
		- In regression, if the RMSE is close to the MAE, the model makes many relatively small errors
		- If the RMSE is close to the MAE^2, the model makes a few but large errors
		- Compute NMSE and NMAE
		- 

10) Draw conclusions and lay out next steps


