######################################################
################## ANCOVA: Analysis of Co-Variance

#including categorical factor splits the relationship between x-var and y-var 
#into several linear equations, one for each level of the categorical factor. 

# ANCOVA is used to compare two or more regression lines by testing 
#the effect of a categorical factor on a dependent variable (y-var) 
#while controlling for the effect of a continuous co-variable (x-var).

##Condn :1)linear scatter (2) normal residuls

library(smatr)
data(leaflife)
head(leaflife)
summary(leaflife)

plot(leaflife$lma,leaflife$longev)

mod1=lm(longev ~ lma*rain,data=leaflife)
summary(mod1)
abline(mod1)
#interaction not significant


mod2=lm(longev ~ lma+rain,data=leaflife)
summary(mod2)
#categorical variable is different
#slope across different groups is different

# rain has a significant effect on the dependent variable(longev)
#significant difference in ‘intercepts’ between the regression lines 
#of low and high rain

anova(mod1,mod2)
#Removing the interaction does not significantly affect the fit of the model
#most parsimonious model- model2

highR=subset(leaflife, rain=="high")
lowR=subset(leaflife,rain=='low')

head(highR)
#H0: slopes don't overlap
#if the confidence intervals of slope overlap, the slopes overlap

#regression for high rain
reg1=lm(longev~lma, data=highR)
summary(reg1)
confint(reg1)

#regression for low rain
reg2=lm(longev~lma, data=lowR)
summary(reg2)
confint(reg2)
