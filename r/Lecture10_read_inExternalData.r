#setwd("F:\\1_FreeMLVideo_R")
#change to your own working directory

## read in csv and tex files
resp1=read.csv("Resp1.csv",header=T)
head(resp1)
str(resp1)

resp2=read.table("Resp2.txt",header=T)
head(resp2)

#read in the CSV data  UCL website:
#https://archive.ics.uci.edu/ml/datasets/Wine+Quality

winer1=read.csv("winequality-red.csv",header=T)
#header= T will read in column names as well
head(winer1)
summary(winer1)

winer1=read.csv("winequality-red.csv",header=T,sep=",")
#header= T will read in column names as well
head(winer1)
summary(winer1)

#specify the correct seperator
winer=read.table("winequality-red.csv",header=T,sep=";")
#header= T will read in column names as well
head(winer)
summary(winer)

##Read in excel data
#excel
#summary(boston1)
library(readxl)
dfb <- read_excel("boston1.xls")
head(dfb)
summary(dfb)

#Using RCurl to read in csv data hosted online on github and other #sites
library(RCurl)
data1= read.csv(text=getURL("https://raw.githubusercontent.com/sciruela/Happiness-Salaries/master/data.csv"))
head(data1)
summary(data1)

data2=read.csv(text=getURL("https://raw.githubusercontent.com/opetchey/RREEBES/master/Beninca_etal_2008_Nature/data/nutrients_original.csv"), skip=7, header=T)
head(data2)
summary(data2)

data3=read.csv(text=getURL("https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/246663/pmgiftsreceivedaprjun13.csv"))
head(data3)