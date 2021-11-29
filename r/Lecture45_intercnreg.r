#Interaction bw X terms

data(iris)
library(ggplot2)

# relation bw Sepal length and width of 3 different species
qplot(Sepal.Length, Petal.Length, data = iris)

fitlm=lm(Petal.Length~Sepal.Length,data=iris)
summary(fitlm)

qplot(Sepal.Length, Petal.Length, data = iris,color = Species)

#is species a significant factor
x=lm(Petal.Length~Sepal.Length+Species,data=iris)
summary(x)

#Is there any significant variation in Petal length across species
#we can ask whether some species tend to have flowers 
#that have long-skinny petals vs. short-wide petals.

fit1=lm(Petal.Length~Sepal.Length*Species,data=iris) #interaction bw
#sepal length & species--> Sepal.Length*Species

#lets examine the statistical significance
anova(fit1)

# in case of Sepal.Length:Species, p<0.05
# Our numerical predictor variable Sepal Length is influenced by Species

#So we can conclude that the regression slopes do vary across the three species.
# quantitative relation bw petal length & sepal length influenced by species

# Species (p<0.05):petal lengths (Y) vary systematically across the three species
# Sepal.Length (p<0.05): Petal length (Y) increased with sepal length (numerical X)

# EQNS FOR DIFFERENT SPECIES 

summary(iris$Species) #factor variable with 3 levels- setosa, versi, virginica

#factor variables: setosa is the reference


## ineractions between numerical terms
## Does the association between Petal length & sepal length depend on petal width

fit2b=lm(Sepal.Length~Petal.Length*Petal.Width,data=iris)
summary(fit2b)
