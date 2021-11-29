head(ToothGrowth)

## Confidence interval of mean
s = sd(ToothGrowth$len)  
SE = s/sqrt(n) #s error 

zval=qnorm(0.975) #z value
zval

moe=zval*SE #margin of error

xbar = mean(ToothGrowth$len)   # sample mean 
xbar + c(-moe, moe) 


## t-based Confidence Interval for Mean
## use in cases n<30

n = length(ToothGrowth$len) 

tval=qt(0.975,df=n-1) #critical t value 
#specify degrees of freedom
tval   #very close to z value

moe=tval*SE #margin of error

xbar = mean(ToothGrowth$len)   # sample mean 
xbar + c(-moe, moe) 

t.test(ToothGrowth$len) #95% CI for mean

t.test(ToothGrowth$len,conf.level = 0.9)
