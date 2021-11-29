
library(MASS)
data()

##Randomly distributed NAs
data(airquality)
??airquality ##more info about these data
str(airquality)

head(airquality)
summary(airquality)

aq=na.omit(airquality) #remove rows containing NAs
head(aq)
summary(aq)
str(aq)

aq2=airquality[complete.cases(airquality), ] #only retain non-NA rows
head(aq2)
summary(aq2)

## replace NAs with 0
aqty=airquality

aqty[is.na(aqty)]<-0
head(aqty)
summary(aqty)

## replcae missing values with average values

meanOzone=mean(airquality$Ozone,na.rm=T)
# remove NAs while computing mean of Ozone
#with na mean value will be na

aqty.fix=ifelse(is.na(airquality$Ozone),meanOzone,airquality$Ozone)
summary(aqty.fix)


##visualize the patterns of NAs
library(mice)
aqty2=airquality
md.pattern(aqty2)
#111 observations with no values

library(VIM) #visualize the pattern of NAs
mp <- aggr(aqty2, col=c('navyblue','yellow'),
                    numbers=TRUE, sortVars=TRUE,
                    labels=names(aqty2), cex.axis=.7,
                    gap=3, ylab=c("Missing data","Pattern"))

#72.5% observations in the entire data have no missing values
#22.9% missing values in Ozone

#impute
#500 iterataions of predictive mean mapping for imputing
#5 datasets
im_aqty<- mice(aqty2, m=5, maxit = 50, method = 'pmm', seed = 500)

#50 iterataions of predictive mean mapping for imputing

summary(im_aqty)

im_aqty$imp$Ozone #values imputed in ozone

#get back the completed dataset u
completedData <- complete(im_aqty,1)
head(completedData)