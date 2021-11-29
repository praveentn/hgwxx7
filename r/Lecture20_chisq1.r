################### Chi-aquare test
############ H0: Two nominal variables (row and columns)
#have no association between them

#whether or not there is an association 
#between gender and food

# Entering the data into vectors
men = c(150, 120, 45)
women = c(320, 270, 100)

# combining the row vectors in matrices, then converting the matrix into a data frame
food.survey = as.data.frame(rbind(men, women))

# assigning column names to this data frame
names(food.survey) = c('Chicken', 'Salad', 'Cake')

food.survey
chisq.test(food.survey)

#frequencies
library(MASS)   
levels(survey$Smoke) 
sfreq = table(survey$Smoke) 
sfreq


library(gmodels)
#2 way cross-tabulation- multivariate frequency table
#
#frequencies and relative frequencies
head(mtcars)
table(mtcars$carb, mtcars$cyl) 
CrossTable(mtcars$carb, mtcars$cyl, prop.t=TRUE, prop.r=TRUE, prop.c=TRUE)

#marginal totals: total of individual rows and columns
#grandtotal: 32 (total no of individuals in table)
#proportion of carb==1 (0.219) and cyl==4 (0.34)

#see which group is different. Needs an n*n matrix
library(fifer) 
# Makes a table of observations -- similar to first example in chisq.test
M <- as.table(rbind(c(76, 32, 46), c(48,23,47), c(45,34,78)))
dimnames(M) <- list(sex=c("Male","Female","Juv"),loc=c("Lower","Middle","Upper"))
M
chisq.test(M)

# Shows post-hoc pairwise comparisons using fdr method
chisq.post.hoc(M)