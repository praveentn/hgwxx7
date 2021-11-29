#################################################
############MANOVA
###multiple response variables are tested simultaneously 
#using a multivariate analysis of variance (MANOVA)

## Do Sepal Length & Petal Length vary significantly between iris species?

data(iris)
head(iris)


# MANOVA test
#works with highly coorelated variables 
res.man <- manova(cbind(Sepal.Length, Petal.Length) ~ Species, data = iris)
summary(res.man)


# Look to see which differ
summary.aov(res.man)

summary.aov(res.man, test = "Wilks") #specify different tests like
#Wilks, Pillai 

library(mvnormtest) #multivariate normality

#ho
#null-hypothesis of this test is that the population is normally distributed. 
num=iris[,1:4]
head(num)

str(num)
head(t(num))

mshapiro.test(t(num))