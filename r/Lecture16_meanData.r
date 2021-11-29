######## Measures of centre for quantitative/numerical data

#what is the typical value?

x<-rnorm(1000, 3, .25)
hist(x)

mean(x)


x=c(2,3,4,5,2,6,8,800,9,10,6,8)
median(x)

#compare the means and medians
#histograms: distribution of values of continuous variables
#frequency of values represented using bars

time <- c(19.09, 19.55, 17.89, 17.73, 25.15, 27.27, 25.24, 21.05, 21.65, 20.92, 22.61, 15.71, 22.04, 22.60, 24.25)
hist(time)

#left skew: Mean <median
# few smaller values reduce the mean

library(moments)

skewness(time) #skewness is a measure of the asymmetry o

N <- 10000
x <- rnbinom(N, 10, .5)
hist(x)
 #right skew: mean>median
#few larger values increase the mean
skewness(x) #positive skew



skewness(iris$Petal.Length)

mean(iris$Petal.Length)
median(iris$Petal.Length)

range(iris$Petal.Length) #minimum to maximum 