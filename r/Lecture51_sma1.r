############ Standardized Major Axis (SMA)
#OR RMA
# Linear regression regression may not be appropriate: 
#i) there may be measurement error in x and y (common in observational studies)
#ii) x and y may have different scales/UNITS
 
library(smatr)

#conditions: (1) Linear relation bw x and y (2) normally distributed residuals

#used in cases of allometric models y=ax^b or log y=log a+b(log x)

#test for common slope between DIFFERENT TREE CATEGORIES
data(Orange)
head(Orange)
summary(Orange)

ComSlope2 = sma(circumference ~ age * as.factor(Tree), log = "xy", data = Orange)
summary(ComSlope2)

#test for common slope between sites with different rain 
data(leaflife)
summary(leaflife)
ComSlope = sma(longev ~ lma * rain, log = "xy", data = leaflife)
summary(ComSlope)
plot(ComSlope)

#Multiple comparison
sma(longev ~ lma * site, log = "xy", data = leaflife, multcomp = T, multcompmethod = "adjust")

#site a and 4 are different


# TESTING FOR EVIDENCE FOR A GIVEN SLOPE (OR SCALING FACTOR)
library(MASS)
data("Animals")
head(Animals)

plot(Animals, log = "xy")
ft = sma(brain ~ body, data = Animals, log = "xy")

#does brain size scale as the 2/3 power of body size? 
#Brain=A*Body^2/3
#or is slope =1 ( variables exhibit equal proportional changes, and demonstrate isometry)

ft1 = sma(brain ~ body, data = Animals, log = "xy", slope.test = 1)
ft2 = sma(brain ~ body, data = Animals, log = "xy", slope.test = 2/3)

summary(ft1)
summary(ft2)