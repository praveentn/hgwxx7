#########################
#################Boxplot- visualize the 5 point data summary
#for continuous data

data("ToothGrowth")
head(ToothGrowth)

boxplot(len ~ supp, data = ToothGrowth) #compare tooth length
#for two different supp

library(ggplot2)
qplot(ToothGrowth$supp, ToothGrowth$len, geom="boxplot")
#or 
ggplot(ToothGrowth, aes(x=supp, y=len)) + geom_boxplot()

library(MASS)
head(birthwt)

ggplot(birthwt, aes(x=factor(race), y=bwt)) + geom_boxplot()
#compare numerical variables across categories

ggplot(birthwt, aes(x=factor(race), y=bwt)) + geom_boxplot()+ggtitle("Birth wt")
#compare numerical variables across categories

ggplot(birthwt, aes(x=factor(race), y=bwt)) + geom_boxplot()+coord_flip()

#horizontal boxplots

head(ChickWeight)
summary(ChickWeight)

ggplot(ChickWeight, aes(x=Time, y=weight))+ 
  geom_boxplot(aes(group=Time))
#group the response and weight according to time

ggplot(ChickWeight, aes(x=Time, y=weight))+ 
  geom_boxplot(aes(group=Time))+facet_grid(. ~ Diet)
#group response variable
#panels according to diet

data("diamonds")
head(diamonds)

ggplot(diamonds, aes(factor(cut), price, fill=cut)) + geom_boxplot() + ggtitle("Diamond Price according Cut") + xlab("Type of Cut") + ylab("Diamond Price U$")
#fill-specify colour according to cut