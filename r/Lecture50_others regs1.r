### When conditions of ols are not met
######## 

###Robust & Resistant regression
## use in any situation you would use OLS and have outliers
data(faithful)
head(faithful)

fit1=lm(eruptions ~ waiting, data=faithful)

par(mfrow = c(2, 2))
plot(fit1)


num= faithful[, 'waiting', drop=FALSE]
head(num)

p1=predict(fit1, num) #produce estimates of eruptions from fit1
p1=as.data.frame(p1)

library(Metrics)
rmse(faithful$eruptions,p1)

library(MASS)

##ROBUST REGRESSION
## Reduce the influence of outliers
## Downweight outliers-reduce their influence on fitted regression line
rob<- rlm(eruptions ~ waiting, data=faithful,psi = psi.bisquare)
#re-weighing outliers 
#can take psi.huber, psi.hampel and psi.bisquare values.

summary(rob)
p2=predict(rob, num)
head(p2)
p2=as.data.frame(p2)
rmse(faithful$eruptions,p2)


##RESISTANT REGRESSION
## heavy tailed distribution- outlying points at end of QQ
## neutralises the effect of outliers 
qqnorm(residuals(fit1))
qqline(residuals(fit1))

resis <- lqs(eruptions ~ waiting, data=faithful)
.

summary(resis)
p2=predict(resis, num)
head(p2)
p2=as.data.frame(p2)
rmse(faithful$eruptions,p2)

plot(faithful$waiting,faithful$eruptions)

abline(fit1, lty="dashed")
abline(rob, col="red")
abline(resis, col="blue")

legend("bottomright", inset=0.05, bty="n",
       legend = c("linear reg", "robust", "resistant"),
       lty = c(2, 1, 1),      # 1 = "solid" ; 2 = "dashed"
       col = c("black", "red", "blue")
)

##non constant variance or heteroskedasticity
#quantile regression
require(quantreg)
Q25=rq(eruptions ~ waiting, data=faithful, tau=0.25)

Q75=rq(eruptions ~ waiting, data=faithful, tau=0.75)

anova(Q25, Q75) #H0: regression coeff are same for both
plot(faithful$waiting,faithful$eruptions)
abline(Q25,lty=3,col="red")
abline(Q75,lty=3,col="blue")


print(rq(eruptions ~ waiting, data=faithful, tau=seq(from=0.05, to=0.95, by=0.05)))
plot(summary(rq(eruptions ~ waiting, data=faithful, tau=seq(from=0.05, to=0.95, by=0.05))))

#################################################