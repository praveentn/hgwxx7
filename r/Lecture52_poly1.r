#####################################################
###########################################################
############### Polynomial & Non-linear
##To fit models that can not be fitted using linear models
## e.g. relationship bw x and y is non-linear- curvilinear
# linear in the coefficients b1, b2
#though it may contain terms that are non-linear in the X’s (such as squared terms of X)

q=seq(0,100,1)
p =0.6
y=500 + p*(q-10)^3
plot(q,y,type='l',col='red',main='Nonlinear relationship',lwd=5)

data("ChickWeight")
head(ChickWeight)

cw1 <- subset(ChickWeight,Diet=='1')
head(cw1)
plot(weight ~ Time, data = cw1)

#wts <- cw1$weight
#times <- cw1$Time
#times2 <- times*times
#times3 <- times*times2

fit1= lm(weight ~ Time, data = cw1)
summary(fit1)
AIC(fit1)

fit2= lm(weight ~ Time+ I(Time*Time), data = cw1)
summary(fit2)
AIC(fit2)

fit3=lm(weight ~ Time+ I(Time*Time)+I(Time*Time*Time), data = cw1)
summary(fit3)
AIC(fit3)

#variables inside I are correlated and that can be a problem
# produce orthogonal polynomials using poly()

fit2a= lm(weight ~ poly(Time,2), data = cw1)
summary(fit2a)
AIC(fit2a)

fit3a= lm(weight ~ poly(Time,3), data = cw1)
summary(fit3a)
AIC(fit3a)

##Non linear regression
##Linear models cannot be used, e.g.in case of growth equations or radiocative decay

library(nls2) #earlier version nls

data("Loblolly")
str(Loblolly)
head(Loblolly)

plot(Loblolly$age,Loblolly$height)

x = Loblolly$age
y =Loblolly$height

m <- nls(y ~ a + b * I(x^z), start = list(a = 1, b = 1, z = 1))
m
#nls needs strating values of a b z
#a=Asym, b=xmid, z=scal
#Asym:  numeric parameter representing the asymptote
#xmid: x value at inflection
#scal : scale parameter

lines(x, fitted(m), lty = 2, col = "red", lwd = 2)

qqnorm(residuals(m))
qqline(residuals(m)) #residuals need to be normally distributed

#compute R2

RSS=sum(residuals(m)^2) #residual sum of squares
TSS=sum((y - mean(y))^2) # total sum of sqaures
R.square=1 - (RSS/TSS)
R.square


######### In case when we don't know the starting values
# we can use a self-starter function
# SSlogis: helps create the initial estimates of parameters
getInitial(height ~ SSlogis(age,  Asym, xmid, scal), data = Loblolly)
#Asym:  numeric parameter representing the asymptote
#xmid: x value at inflection
#scal : scale parameter

y.ss <- nls(height ~ SSlogis(age, Asym, xmid, scal), data = Loblolly)
summary(y.ss)

alpha <- coef(y.ss)  #extracting coefficients
plot(height ~ age, data = Loblolly, main = "Logistic Growth Model of Trees", 
     xlab = "Age", ylab = "Height")  # Census data

curve(alpha[1]/(1 + exp(-(x - alpha[2])/alpha[3])), add = T, col = "blue")  # Fitted model

# fit the growth equation  Asym/(1+exp((xmid-input)/scal))

qqnorm(residuals(y.ss))
qqline(residuals(y.ss))
#############Gompertz growth model 
###Asym*exp(-b2*b3^x)

fm1 <- nls(height ~ SSgompertz(log(age), Asym, b2, b3),
           data = Loblolly)
summary(fm1)

alpha <- coef(fm1)


qqnorm(residuals(fm1))
qqline(residuals(fm1))

############ We can use a Growth function

#Chapman richard growth model- where tree height growth is modeled as
#function of time

# Define function

chapm <- function(x,Asym,b,c)Asym*(1-exp(-b*x))^c

#Asym is the maximum value of growth
#c is related to catabolism (destructive metabolism); maximum value 3
# 1-exp function helps define actual growth

nls_lob <- nls(height ~
                 chapm(age, Asym, b,c),
               data=Loblolly,
               start=list(Asym=100, b=0.1, c=2.5))
                 
library(nlshelper)               
plot_nls(nls_lob, ylim=c(0,80), xlim=c(0,30))
