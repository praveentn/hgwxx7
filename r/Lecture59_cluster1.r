##iris data

data(iris)
summary(iris)

#visualize the distribution of iris species sepal length & width
library(ggplot2)
ggplot(data = iris, aes(Sepal.Length, Sepal.Width)) + geom_point(aes(colour = (Species)))

set.seed(20) #ensure replicability
names(iris)
#k-means minimize the within group dispersion and maximize the between-group dispersion. 

#1:2- we want to cluster the species on the basis of sepal length and #width
#we want 3 clusters
#nstart- number of starting assignments, select the one with lowest
#within cluster variation 
irisCluster <- kmeans(iris[, 1:2], 3, nstart = 15)
irisCluster
#71 % is a measure of the total variance in data set that is explained by the clustering. k-means minimize the within group dispersion and maximize the between-group dispersion. 

## compare cluster with species
table(irisCluster$cluster, iris$Species)

# all setosa species assigned to cluster 1.
# 38 versicolor assigned to cluster 2 and 12 to cluster 1

irisCluster$cluster <- as.factor(irisCluster$cluster)
ggplot(iris, aes(Sepal.Length, Sepal.Width, color = irisCluster$cluster)) + geom_point()

#Elbow Method for finding the optimal number of clusters
set.seed(123)
# Compute and plot wss for k = 2 to k = 15.
max <- 15
data <- scale(iris[, -5]) #remove species column
wss <- sapply(1:max, 
              function(k){kmeans(data, k, nstart=50,iter.max = 15 )$tot.withinss}) #how many clusters will reduce within group variation

plot(1:max, wss,
     type="b", pch = 19, frame = FALSE, 
     xlab="Number of clusters K",
     ylab="Total within-clusters sum of squares")


##
irisCluster <- kmeans(iris[, 1:2], 5, nstart = 15)
irisCluster
table(irisCluster$cluster, iris$Species)

###########
library(factoextra)
fviz_cluster(irisCluster, data = data, geom = "point",
             stand = FALSE, frame.type = "norm")
