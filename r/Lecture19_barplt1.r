#################################################################
############# BAR GRAPH: Represent discrete categories of data
# length- represents the magnitude or frequencies of data

head(mtcars)
c <- table(mtcars$gear)
barplot(c, main="Car Distribution", 
        xlab="Number of Gears")

t=tapply(iris$Sepal.Length, iris$Species, mean)

barplot(t, main="Average Sepal Length", 
        xlab="Species",ylab="Mean")

library(ggplot2)
data(diamonds)
head(diamonds)

table(diamonds$color, diamonds$clarity)

barplot(table(diamonds$color, diamonds$clarity),
         legend = levels(diamonds$color),           
         beside = TRUE)    


barplot( table(diamonds$color, diamonds$clarity),
         legend = levels(diamonds$color),           
         beside = TRUE,
         xlab = "Diamond Clarity",                      # Add a label to the X-axis
         ylab = "Diamond Count",                        # Add a label to the Y-axis
         main = "Diamond Clarity, Grouped by Color",    # Add a plot title
         col = c("#FFFFFF","#F5FCC2","#E0ED87","#CCDE57",     # Add color*
                 "#B3C732","#94A813","#718200") )

d=table(diamonds$color, diamonds$clarity)
######## USe GGPLOT for better graphs

# Very basic bar graph
qplot(factor(cyl), data=mtcars) #plot factor variables
#or
ggplot(mtcars, aes(x=factor(cyl))) + geom_bar()

qplot(color, data=diamonds, geom="bar") #specify bar

#stacked bars
head(diamonds)
ggplot(diamonds, aes(clarity, fill=cut)) + geom_bar(position="dodge")

ggplot(diamonds, aes(cut, fill=cut)) + geom_bar() + 
  facet_grid(. ~ clarity) #seperate panels on the basis of clarity

ship=as.data.frame(Titanic)
head(ship)
ggplot(aes(x=Age, weight=Freq), data=ship) +
  geom_bar()

ggplot(aes(x=Age, weight=Freq), data=ship) +
  geom_bar()+
  facet_grid(Sex~Class)


## error bar: error or uncertainty in a reported measurement (mean)
##one standard deviation of uncertainty, one standard error

library(dplyr)

isum= iris %>% # the names of the new data frame and the data frame to be summarised
  group_by(Species) %>%   # the grouping variable
  summarise(avg = mean(Petal.Length),  # calculates the mean of each group
            sdpl = sd(Petal.Length))

ggplot(isum, aes(Species, avg)) + geom_bar(stat="identity") +  geom_errorbar(aes(ymin=avg-sdpl, ymax=avg+sdpl),width=0.2)
