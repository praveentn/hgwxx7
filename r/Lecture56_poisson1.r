############# Poisson
#### for count data
#### 1) being discrete, and 2) having variance that generally increases with the mean 

setwd("F:\\Basic to Advanced Linear Modelling\\Data")

c=read.csv("canopycvr1.csv")
attach(c)
head(c)

mean(c$cover)
var(c$cover)

#data mean and data variance are roughly similar- meets consitions of Poisson

#predict variation in canopy cover as a function of elevation
fit= glm(cover~elev,data=c, family=poisson(link=log))
summary(fit)

cf=coef(fit)
cf

#for a unit increase in elevation the increase in cover is e^b

exp(cf[2]) #with every unit increase in elevation
#cover increases by a factor of 1.002
#inverse of the link function


#model selection

fit2= glm(cover~elev+tci,data=c, family=poisson)
summary(fit2)

## compare models

anova(fit,fit2,test="Chisq")
 #adding the new term, tci has not improved model performance

## categorical qualitative variable

fit3 = glm(cover~disturb*elev,data=c,family=poisson)
summary(fit3)
#disturbance is a significant ineraction

#higher cover in undisturbed forest

## in case of overdispersed data use negative binomial regression

library(MASS)
#glm.nb

fit= glm.nb(cover~elev,data=c)
summary(fit)
