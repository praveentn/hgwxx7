############## t-tests: examine if the difference in means is significant or not

normdis<-rnorm(n=1000, m=30, sd=3)
hist(normdis)

data("ToothGrowth")
head(ToothGrowth)
str(ToothGrowth)

hist(ToothGrowth$len)

#qqplot
qqnorm(ToothGrowth$len)
qqline(ToothGrowth$len)
# Shapiro-Wilk normality test 
#H0: data are normally distributed
shapiro.test(ToothGrowth$len) #data are normally distributed
