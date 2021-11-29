
library(ISwR)
data(rmr)
head(rmr)

x=rmr$body.weight
y=rmr$metabolic.rate
plot(x,y,xlab="Body wt",ylab="Metabolic")

fit <- lm(y ~ x)
summary(fit)
abline(fit) #fit regression line via pts

library(ggplot2)
#plot 95% CI for predictions from the linear model lm
ggplot(data = rmr, aes(body.weight, metabolic.rate)) + geom_point() + geom_smooth(method = "lm")

#99% CI
ggplot(data = rmr, aes(body.weight, metabolic.rate)) + geom_point() + geom_smooth(method = "lm",level=0.99)


library(stats)
confint(fit, 'x', level=0.95) #95% CI for slope y=mx+b

library(HH)
#plot more intervals
##on our fitted model
ci.plot(fit)

ci.plot(fit,xlab="Body wt",ylab="Metabolic")

################ With unseen data
#predict CI for a new pt x
newconf <- predict(fit, newdata=data.frame(x=103), interval="confidence",
                   level = 0.95)
newconf
##CI for regression line
## with new data
newx <- seq(120, 200, by=20)
fit <- lm(y ~ x)
summary(fit)
plot(x,y,xlab="Body wt",ylab="Metabolic")
abline(fit) #fit regression line via pts
conf_interval = predict(fit, newdata=data.frame(x=newx), interval="confidence",
                        level = 0.95)
lines(newx, conf_interval[,2], col="blue", lty=2)
lines(newx, conf_interval[,3], col="blue", lty=2)

#prediction interval
pred_interval <- predict(fit, newdata=data.frame(x=newx), interval="prediction",
                         level = 0.95)
lines(newx, pred_interval[,2], col="red", lty=2)
lines(newx, pred_interval[,3], col="red", lty=2)

