#######################################################
################ One way ANOVA
##an extension of independent two-samples t-test 
##for comparing means ehen we have 2+ groups
##data is organized into 2+ groups based on one single grouping 
#variable (also called factor variable)


data("PlantGrowth")
head(PlantGrowth)
str(PlantGrowth)
summary(PlantGrowth)

levels(PlantGrowth$group)

library(ggpubr)

ggboxplot(PlantGrowth, x = "group", y = "weight", 
          color = "group", palette = c("blue", "red", "green"),
          order = c("ctrl", "trt1", "trt2"),
          ylab = "Weight", xlab = "Treatment")


md = aov(weight ~ group, data = PlantGrowth)
summary(md)

#there are significant differences between the groups highlighted 

#which of the groups are significantly different?
# pst hoc test
t=TukeyHSD(md)
t

plot(t)
#difference between trt2 and trt1 is significant 

#Pairwise t-test
pairwise.t.test(PlantGrowth$weight, PlantGrowth$group,
                p.adjust.method = "BH")

## Conditions of one way ANOVA

## 1) Check the homogeneity of variance assumption
plot(md, 1)

##2) Normality of residuals.
plot(md, 2)

# Extract the residuals
aov_residuals <- residuals(object = md )
# Run Shapiro-Wilk test
shapiro.test(x = aov_residuals ) #errors are normally distributed
