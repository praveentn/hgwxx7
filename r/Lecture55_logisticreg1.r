############## Logistic regression
#sinosuidal shaped data- variance decreases towards 0 and 1
#binomial 

library(ggplot2)
ggplot(mtcars, aes(x=wt, y=am)) + geom_point() + 
  stat_smooth(method="glm", method.args=list(family="binomial"), se=FALSE)

fitglm= glm(am~hp+wt, data=mtcars,family=binomial(link='logit'))
#specify binomial distribution for logistic regression


exp(coef(fitglm)) #odss of succes/ Y=1

summary(fitglm)

#The null deviance shows how well the response variable is 
#predicted by a model that includes only the intercept (grand mean).
#DF number of observations-1

#The residual deviance shows how well the response variable is 
#predicted by a model that includes both predictor vars (DF declines by 2 more)

#residual deviance for a well-fitting model 
#should be approximately equal to its degrees of freedom

#-----------------------------------

# how well does the model fit the data
#Hosmer and Lemeshow goodness of fit (GOF) test
library(ResourceSelection)
hoslem.test(mtcars$am, fitted(fitglm))

#model appears to fit well 
#we have no significant difference between the model and the observed data (i.e. the p-value is above 0.05)

## for predicting values of unseen data
newdata = data.frame(hp=120, wt=2.8)

predict(fitglm, newdata, type="response") 

#Overdispersion means that the data show 
# discrepancies between the observed responses yi and their predicted values 
#larger than what the binomial model would predict
#overdispersion is present in a dataset, the estimated standard errors and test statistics 
#the overall goodness-of-fit will be distorted

library(arm)

x=predict(fitglm)
y=resid(fitglm)

binnedplot(x,y) #most of the data fall in -2 to 2 standard error
# no overdispersion

########## binomial count data
#### logistic data for other cases with sinosuidal shape
### variance decreases towards 0 and 1
### binomial distribution

library(AICcmodavg)

data(beetle)
head(beetle)
b=beetle

head(b)

qplot(Dose,Mortality_rate,data=beetle)

b$survive=b$Number_tested-b$Number_killed

fitglm2= glm(cbind(Number_killed,survive)~Dose,data=b,family=binomial)
 #logistic transformation converts proportions to logits

summary(fitglm2)
#robust fit  residual deviance/redsidual df are almost 1:1
 
#check overdispersion
x=predict(fitglm2)
y=resid(fitglm2)

binnedplot(x,y)