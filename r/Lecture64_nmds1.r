######################## NMDS (Non-metric multi dimensional scaling)
##visualize similarity
##place each object in N-dimensional space such that the 
#between-object distances are preserved as well as possible
x=read.table("carabid-beetles-boreal-forest.txt")
attach(x)
head(x)
summary(x)
require(vegan)
xt=t(x) # now our habitats are rows
head(xt)
###ndms
example1=metaMDS(xt,k=2,trymax=100) #k=2 we want to visualize with 2 axis
ordiplot(example1,type="n")
orditorp(example1,display="species",col="red",air=0.01)
orditorp(example1,display="sites",cex=1.25,air=0.01)

#specify distance algorithm
example2=metaMDS(xt,distance = "bray",k=2,trymax=100) #bray computes dissimilarity
ordiplot(example2,type="n")
orditorp(example2,display="species",col="red",air=0.01)
orditorp(example2,display="sites",cex=1.25,air=0.01)
