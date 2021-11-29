################################################################
#########Non parametric version of t-tests:
########## examine the difference in median values bw  distributions

data("CO2")
head(CO2)
str(CO2)
hist(CO2$uptake)

# Shapiro-Wilk normality test 
#H0: data are normally distributed
shapiro.test(CO2$uptake) #data arenot normally distributed distributed

#########Mann-whitney U test: unpaired data
## compare uptake for chilled and non-chilled
## independent samples
chill = CO2$uptake[CO2$Treatment == 'chilled']
nonchill = CO2$uptake[CO2$Treatment == 'nonchilled']

wilcox.test(chill, nonchill) 

wilcox.test(CO2$uptake~CO2$Treatment) #treatment is factor

########Wilcoxon Signed-Rank Test: paired data

library(MASS) 

head(immer)#wheat yield in 1931 and 32

wilcox.test(immer$Y1, immer$Y2, paired=TRUE) 
#H0: yields of the two sample years are identical populations