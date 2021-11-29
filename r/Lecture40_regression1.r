###################### REGRESSION



#Y can only be numerical continuous and x can be numerical or categorical
names(iris)

#Linear regression- with single X variable
fit1=lm(Petal.Length~Sepal.Length, data=iris)

#look at the model results
summary(fit1)

       
#Multiple regression    
fit2=lm(Petal.Length~., data=iris)#all remaining variables are now X

fit2=lm(Petal.Length~.-Species, data=iris)#remove species from analysis
summary(fit2)

## if we don't want all variables 
names(iris)
#fit2=lm(Petal.Length~Sepal.Width+Petal.Width, data=iris)
 
 
 #amount of variance explained by each predictor
library(hier.part)
x <- iris[,2:4] #response var
HP=hier.part(iris$Sepal.Length, x)
