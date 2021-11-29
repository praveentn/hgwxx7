###################################################################
######### Two way ANOVA
## evaluate simultaneously the effect of two grouping variables
##2 Fctor variables on a response variable

## H0: response mean for all factor levels are equal.

data("ToothGrowth")
head(ToothGrowth)
str(ToothGrowth)

df=ToothGrowth

head(df)
summary(df)
str(df)

df$dose <- factor(df$dose, 
                       levels = c(0.5, 1, 2),
                       labels = c("D0.5", "D1", "D2"))


boxplot(len ~ supp * dose, data=df, frame = FALSE, 
        col = c("red", "blue"), ylab="Tooth Length")

## see if tooth length depends on supp and dose.
#two factor variables are independent
md1 <- aov(len ~ supp + dose, data = df)
summary(md1)

#both supp and dose are statistically significant
#Mean tooth length  for both supp and dose are NOT equal

# test two variables might interact to create an synergistic effect

md2 <- aov(len ~ supp * dose, data = df)
summary(md2)

#two main effects (supp and dose) are statistically significant, 
#as well as their interaction
#relationships between dose and tooth length depends on the supp method
# influence the difference between mean tooth length

## Post Hoc test to identify which dosage group is different
TukeyHSD(md2, which = "dose")

#pairwise t-tests
pairwise.t.test(df$len, df$dose,
                p.adjust.method = "BH")

## Testing when we have unequal sample numbers
library(car)
mya = aov(len ~ supp * dose, data = df)
Anova(mya, type = "III") #Type-III sums of squares used when we have 
#unequal numbers per group

######### CONDITIONS FOR " WAY ANOVA

##1) Test homogeneity of variance assumption

plot(md2, 1)

##2) test for normality of residuals

plot(md2, 2)

# Extract the residuals
aov_residuals <- residuals(object = md2 )
# Run Shapiro-Wilk test
shapiro.test(x = aov_residuals ) #errors are normally distributed
