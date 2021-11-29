#######################################
##################### Data structures

#VECTORS

x=c(1,12,30,54,5)

length(x)

typeof(x) #what type is my vector

x[2] #index number

x=c(x,8) #add another value
x

x=c(x,"cat") #character vector
x
typeof(x)
x[1:3]

#sequence of numbers
series <- 1:10
seq(10)

y=seq(1, 10, by = 2)
y

typeof(y)

typeof(as.integer(y)) #coerce it into a different data type

## MATRIX: 2D vector

m <- matrix(1:6, nrow = 2, ncol = 3)
m

m2=matrix(y,nrow=3,ncol=2)
m2

#bind columns of two vectors to create a matrix

x <- 1:4
y <- 10:13
cbind(x, y) #join of the basis of columns
#all columns should have same number of rows

nrow(cbind(x, y)) #no of rows
ncol(cbind(x, y)) #no of columns


rbind(x, y) #join by rows

df1=as.data.frame((cbind(x,y))) #convert to data farme
df1

str(df1)
length(df1)

################### Data frames
#most statistical analysis is done on data frames
#R has many in-built data frames

data()

data(package="datasets")

data(ChickWeight)

str(ChickWeight)
#factors represent categorical veraibles using numbers
#factorscould be things like levels: basic, intermediate., advanced 
#represented using 1 2 3
  head(ChickWeight)
  