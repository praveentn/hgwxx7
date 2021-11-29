################### Variation 

head(iris)

summary(iris$Petal.Length)

std=sd(iris$Petal.Length) #standard deviation of petal length mean
std

library(sciplot)
se(iris$Petal.Length)

#display 5 point summary graphically- boxplot

boxplot(iris$Petal.Length, main="Sepal Length",ylab="length")
