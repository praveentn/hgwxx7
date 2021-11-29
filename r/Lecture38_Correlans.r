 
data(mtcars)
str(mtcars)
head(mtcars)


library(ggplot2)
p1=qplot(mpg, wt, data = mtcars,
      xlab = "Miles/gallon", ylab = "Weight",
      main = "Miles per gallon vs. Weight")

p2=qplot(Petal.Length,Petal.Width,data=iris,xlab="Petal Length",ylab="Petal Width",main="Sepal Length vs Width")

qplot(Petal.Length,Petal.Width,data=iris,xlab="Petal Length",ylab="Petal Width",col=Species)

library(gridExtra)
grid.arrange(p1, p2, ncol=2)


hist(mtcars$mpg)
hist(mtcars$wt)

# Shapiro-Wilk normality test for mpg
#H0: data are normally distributed
shapiro.test(mtcars$mpg) 
# Shapiro-Wilk normality test for wt
shapiro.test(mtcars$wt) # => p = 0.09


#Pearson's correlation
cor(mtcars$mpg,mtcars$wt) #default Perason's
cor(mtcars$mpg,mtcars$wt, method="pearson") #specify the method

cor(mtcars$mpg,mtcars$wt, method="pearson",use = "complete.obs")
#in case of NAs being present, specify complete.obs

#is my correlation statistically significant?
#Ho=there is no association between the two variables
cor.test(mtcars$mpg,mtcars$wt)

mydata <- mtcars[, c(1,3,4,5,6,7)]
head(mydata)

library(corrplot)
corr1<-cor(mtcars) #compute multiple correlations
corr1
corrplot(corr1)
corrplot(corr1, method="color")

## ANOTHER CORRELATION

cor(iris$Petal.Length,iris$Petal.Width)

#should I even use Pearson's correlation for iris?
shapiro.test(iris$Petal.Length)

cor(iris$Petal.Length,iris$Petal.Width, method="spearman") 
#spearman's rank method

cor(iris$Petal.Length,iris$Petal.Width, method="kendall") 


 