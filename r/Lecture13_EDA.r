###############################################################
#################### EDA ####################
##### (1)Can explore the distribution of 1 variable 
#### (2) Can explore the relationship between 2 variables 

data(iris)
names(iris)
summary(iris)

##examine data distribution of a quantitative variable

hist(iris$Sepal.Length) # distribution of a varaibles

boxplot(iris$Sepal.Length,main="Summary of iris",xlab="Sepal Length")
#viz of descreptive statstics 

#relation bw 2 quantitative variables
plot(iris$Sepal.Length,iris$Sepal.Width)

#PLOTTING CATEGORICAL or COUNT VARIABLES

data(mtcars)
names(mtcars)
str(mtcars)
counts <- table(mtcars$gear)
counts
barplot(counts, main="Cars", xlab="Number of Gears")

barplot(counts, main="Cars", xlab="Number of Gears",horiz=TRUE)

barplot(counts, main="Cars", xlab="Number of Gears",horiz=TRUE,col="red")


## Improved data viz

library(ggplot2)

# relation bw Sepal length and width of 3 different species
qplot(Sepal.Length, Petal.Length, data = iris,color = Species)

# We see that Iris setosa flowers have the narrowest petals.
qplot(Sepal.Length, Petal.Length, data = iris, color = Species, size = Petal.Width)

##Add labels to the plot

qplot(Sepal.Length, Petal.Length, data = iris, color = Species,
      xlab = "Sepal Length", ylab = "Petal Length",
      main = "Sepal vs. Petal Length in Iris data")

qplot(Sepal.Length, Petal.Length, data = iris, geom = "line", color = Species) #line plot

########################GGPLOT#####################

##use ggplot for viz
#Format: ggplot(data = , aes(x =, y =, ...)) + geom_xxx()
#aes-> we specify x,y 
#geom-> Plot type: wether its a histogram, boxplot
ggplot(data = iris, aes(Sepal.Length, Sepal.Width)) + geom_point()

#distinguish between species using colour scheme
ggplot(data = iris, aes(Sepal.Length, Sepal.Width)) + geom_point(aes(colour = (Species)))
#or
ggplot(iris, aes(x = Sepal.Length, y = Sepal.Width, shape = Species)) + geom_point()

## (1) we can only specify colour and shapes on factor variables
##(2)  Factors:numbers representing categorical values
##(3)function "factor" turns any number into a qualitative representation

str(mtcars)

#use mtcars as a factor in visualization
ggplot(mtcars, aes(x = mpg, y = wt, colour = factor(gear))) + geom_point()

#histogram
ggplot(iris, aes(x = Sepal.Length)) + geom_histogram()

ggplot(iris, aes(x = Sepal.Length, fill = Species)) + geom_histogram()

#boxplot
ggplot(iris, aes(x = Species, y = Sepal.Length)) +geom_boxplot()

#visualize relationship bw the different variables for the 3 species
ggplot(data = iris, aes(Sepal.Length, Sepal.Width)) + geom_point() + facet_grid(. ~ Species) + geom_smooth(method = "lm")


