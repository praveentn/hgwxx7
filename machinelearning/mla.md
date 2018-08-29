# Machine Learning Algorithm (MLA) 
## Selection and Initialization

### list
    #mla
    mla = [ 
      #Ensemble Methods
      ensemble.AdaBoostClassifier(),
      ensemble.BaggingClassifier(),
      ensemble.ExtraTreesClassifier(),
      ensemble.GradientBoostingClassifier(),
      ensemble.RandomForestClassifier(),
  
      #Gaussian Processes
      gaussian_process.GaussianProcessClassifier(),
      
      #GLM
      linear_model.LogisticRegressionCV(),
      linear_model.PassiveAggressiveClassifier(),
      linear_model.RidgeClassifierCV(),
      linear_model.SGDClassifier(),
      linear_model.Perceptron(),
      
      #Navies Bayes
      naive_bayes.BernoulliNB(),
      naive_bayes.GaussianNB(),
      
      #Nearest Neighbor
      neighbors.KNeighborsClassifier(),
      
      #SVM
      svm.SVC(probability=True),
      svm.NuSVC(probability=True),
      svm.LinearSVC(),
      
      #Trees    
      tree.DecisionTreeClassifier(),
      tree.ExtraTreeClassifier(),
      
      #Discriminant Analysis
      discriminant_analysis.LinearDiscriminantAnalysis(),
      discriminant_analysis.QuadraticDiscriminantAnalysis(),
  
      
      #xgboost: http://xgboost.readthedocs.io/en/latest/model.html
      XGBClassifier()    
    ]
