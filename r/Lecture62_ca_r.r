###################################
#############CA (Correspondence analysis)
############# MVA for examining relationship between variables 
#in a contingency table

setwd("F:\\Basic to Advanced Linear Modelling\\Data")
#Data from: Niemelä et al. (1988)
#Carabid beetles collected using pitfall traps in fragments of different habitats
#number of individuals for all species recorded in each of five habitats
#species in row and habitats in columns

#for mva
library("FactoMineR")
library("factoextra")

x=read.table("carabid-beetles-boreal-forest.txt")
attach(x)
head(x)
summary(x)

chisq <- chisq.test(x)
chisq

resca <- CA(x, graph = FALSE) #carry out Correspondence Analysis
#on categorical data

print(resca)

summary(resca, nb.dec = 2, ncp = 2) #2 decimal places

# interpret correspondence analysis, 
#the first step is to evaluate whether there is a 
#significant dependency between the rows and columns.

#examine dep bw rows and columns using eigen values
eig <- get_eigenvalue(resca) 
#Eigenvalues correspond to the amount of information retained by each axis

trace <- sum(eig$eigenvalue) #total sum of eigen values
corcoef <- sqrt(trace)
corcoef #value of 0.2 signifies significant correlation

#how many dimensions are sufficent for interpretation?
#look at eigen value table

eigenvals=get_eigenvalue(resca)
head(round(eigenvals, 2))

#variance percent= Axis eigen value/trace

fviz_screeplot(resca) #visualize variance explained by Dimensions

fviz_ca_biplot(resca) #symetric plot
#shows a global pattern within the data.
#row and column profiles simultaneously in a common space

##look at rows (species)
row <- get_ca_row(resca)
row

#contribution of the species/rows to the dimensions
head(row$contrib)
fviz_contrib(resca, choice = "row", axes = 1)
head(col$contrib)
fviz_contrib(resca, choice = "row", axes = 1) #contribution of species 
#in row to dimension 1
#to both dimension 1 and 2
fviz_contrib(resca, choice = "row", axes = 1:2)
#top contributing species
fviz_contrib(resca, choice = "row", axes = 1, top = 5)


#contribution of habitats/columns to te CA dimensions
#look at habitats (columns)
col <- get_ca_col(resca)
col
#look at column contribution
head(col$coord)

#contributions of habitats to dimension 1 and 2
fviz_contrib(resca, choice = "col", axes = 1:2)

