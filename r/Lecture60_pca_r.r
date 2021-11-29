###################### PCA
data(iris)
head(iris)

#skewness can effect results
#centre and scale
# log transform 
# PC comp: Z¹ = F¹¹X¹ + F²¹X² + F³¹X³ + .... +Fp¹Xp. Thetas are loadings.
#Without normalization loadings will be very large 

log.x<- log(iris[, 1:4])
ir.species <- iris[, 5]

# apply PCA - scale. = TRUE is highly 
# advisable, but default is FALSE. 
ir.pca <- prcomp(log.x,
                 center = TRUE,
                 scale. = TRUE) #apply on quantitative variables

print(ir.pca)
# plot method-- see which PC explains maximum variability in data
# which PC to retain
plot(ir.pca, type = "l")

summary(ir.pca)


###
library(devtools)
install_github('fawda123/ggord')

p <- ggord(ir.pca, iris$Species)
p


# Install R packages for MVA
install.packages("FactoMineR")
# Load
library("FactoMineR")

install.packages("factoextra")
library("factoextra")

res.pca <- PCA(log.x,  graph = FALSE)
get_eig(res.pca)

# Visualize eigenvalues/variances
fviz_screeplot(res.pca, addlabels = TRUE, ylim = c(0, 90))


##how much have the individual predictors contributed to the PC variance

var <- get_pca_var(res.pca)
var

# Contribution of variables
head(var$contrib)

# Contributions of variables to PC1
fviz_contrib(res.pca, choice = "var", axes = 1, top = 10)

# Contributions of variables to PC2
fviz_contrib(res.pca, choice = "var", axes = 2, top = 10)

# Graph of variables to PC: default plot
fviz_pca_var(res.pca, col.var = "black")
