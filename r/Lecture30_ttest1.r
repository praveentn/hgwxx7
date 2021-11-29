###########################################################
#################################################
############## t-tests: examine if the difference in means is significant or not

data("ToothGrowth")
head(ToothGrowth)
str(ToothGrowth)

hist(ToothGrowth$len)
# Shapiro-Wilk normality test 
#H0: data are normally distributed
shapiro.test(ToothGrowth$len) #data are normally distributed

library(ggplot2)
qplot(supp,len,data=ToothGrowth, 
      main="Tooth growth of guinea pigs",xlab="Supplement type", ylab="Tooth length") + geom_boxplot(aes(fill = supp))

mean(ToothGrowth$len)
### one sided t-test
### test if the mean value is equal to a certian number
### H0: true value of mean=18
t.test(ToothGrowth$len,mu=18)
 #or greater than or less than a given value

t.test(ToothGrowth$len, alternative = "greater", mu = 3)
#H0: true value of mean is 3


# independent 2-group t-test
# test the difference in mean
#H0: These is no difference in the population means of the 2 groups
# split data set
OJ = ToothGrowth$len[ToothGrowth$supp == 'OJ']
VC = ToothGrowth$len[ToothGrowth$supp == 'VC']

t.test(OJ, VC,
       paired = FALSE, var.equal = FALSE, conf.level = 0.95) 
#Variances of tooth growth are different when using different supplement and dosage.
#test for mean being significantly different

t.test(OJ, VC,alternative = "greater",paired = FALSE) 

#test for mean being significantly greater
#paired=FALSE : measurements collected seperately
#If you randomly sample each set of items separately, under different conditions, the samples are independent


## paired observations: If you collect two measurements on each item
t.test(OJ, VC,
       paired = TRUE, var.equal = FALSE, conf.level = 0.95) 

#e.g before or after treatments
# OJ and VC were applied on test subjects in 2 treatment groups