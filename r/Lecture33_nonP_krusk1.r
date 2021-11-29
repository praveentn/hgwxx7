##################################################################
#### Non-parametric One way ANOVA

#1) If the condition of normality of residuals is not met, 
# we implement the kruskal wallis test

kruskal.test(weight ~ group, data = PlantGrowth)

pairwise.wilcox.test(PlantGrowth$weight, PlantGrowth$group,
                     p.adjust.method = "BH")

#2) where the homogeneity of variance assumption is violated

oneway.test(weight ~ group, data = PlantGrowth)