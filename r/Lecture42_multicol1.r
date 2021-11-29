library(mlbench)
library(help = "mlbench")

data(BostonHousing)
str(BostonHousing)

summary(BostonHousing)
head(BostonHousing)

##Predict the variation in medv house price- median house price
## medv, our target variable (Y) is a continuous numerical entity
##Regression problem

library(ggplot2)
library(car)
library(caret)
library(corrplot)



#(1) Tackle multi-collineraity, i.e. presence of highly correlated
#predictors (X)
#we remove numerical Xs with correlation>0.7

#Dropping response variable (Y) for calculating Multicollinearity
mat_a = subset(BostonHousing, select = -c(medv))

# we only want numerical variables for computing correlation
numeric <- mat_a[sapply(mat_a, is.numeric)]

#Calculating Correlation- strength of association between two variables
descrCor <- cor(numeric)
print(descrCor)

corrplot(descrCor)

#remove highly correlated variables
# if x1 and x2 are highly correlated,which one to remove depends on 
#your own understanding of the data
require(caret)
# Checking Variables that are highly correlated
highlyCorrelated = findCorrelation(descrCor, cutoff=0.7)

#Identifying Variable Names of Highly Correlated Variables
highlyCorCol = colnames(numeric)[highlyCorrelated]
highlyCorCol


#Remove highly correlated variables from the original dataset and create a new dataset

data3 = BostonHousing[, -which(colnames(BostonHousing) %in% highlyCorCol)]
dim(data3)

names(data3)


##########vif

# Choose a VIF cutoff under which a variable is retained (Zuur et al. 2010 
# vif>10  multi-collinearity
#can also reject predictors with vf 5-10
#car package

fit=lm(medv~.,data=BostonHousing)
summary(fit)

vif(fit) 

##check

df=cbind(BostonHousing$medv,data3)
df=as.data.frame(df)
fit2=lm(medv~.,data=df)
vif(fit2)