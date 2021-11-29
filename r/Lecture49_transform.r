#################################################
################
## What happens when we break the condition of normality of residuals?

data(iris)
head(iris)

fit1=lm(Sepal.Width ~ Petal.Width, data=iris)
summary(fit1)

par(mfrow = c(2, 2))
plot(fit1)

qqnorm(residuals(fit1))
qqline(residuals(fit1))

hist(iris$Sepal.Width)

#try a transformation of Ys
iris$Sepal.Width.sq <- sqrt(iris$Sepal.Width) #sq root
iris$Sepal.Width.cub <- (iris$Sepal.Width)^(1/3) #cube root
iris$Sepal.Width.ln <- log(iris$Sepal.Width) #log

hist(iris$Sepal.Width.sq)
hist(iris$Sepal.Width.cub)
hist(iris$Sepal.Width.ln)

## Linear regression bw  square root of Y and X

fit2 <- lm(iris$Sepal.Width.sq~iris$Petal.Width)
summary(fit2)

par(mfrow = c(2, 2))
plot(fit2)

qqnorm(residuals(fit2))
qqline(residuals(fit2))

## transform both X and Y
## log-log transform
## power law: some biological problems (such as llometric scaling) lend themselves to log-log
##  power law is Y=a*X^b
## simplify to log(Y)~log(X)
## backtransformation Y (back-transform)=exp(a+b*log(X))

fit3 <- lm(log(iris$Sepal.Width)~log(iris$Petal.Width))

summary(fit3)

par(mfrow = c(2, 2))
plot(fit3)

c = coef(fit3)
a = c[1]
b = c[2]

backtrans = exp(a+ b*log(iris$Petal.Width))

head(backtrans)

##run Box-Cox transformation to avoid sifting through transforms
# run the box-cox transformation
#family of transformations designed to reduce nonnormality of the errors in a linear model


library(MASS)
bc <- boxcox(Sepal.Width ~ Petal.Width, data=iris)

#log-likelihood function governs the selection of the lambda power transform
# select lambda to carry out transformation

trans <- bc$x[which.max(bc$y)]
trans #use only islambda values lie bw -2 to 2

fit4 <- lm(Sepal.Width^trans ~ Petal.Width, data=iris)
summary(fit4)

par(mfrow = c(2, 2))
plot(fit4) #not all data can be transformed