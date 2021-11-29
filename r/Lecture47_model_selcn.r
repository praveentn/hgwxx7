library(MASS)



##examine all models
step(lm(mpg~wt+drat+disp+qsec,data=mtcars),direction="both")

step(lm(mpg~wt+drat+disp+qsec,data=mtcars),direction="backward")

## include performance of the null model as well
null=lm(Sepal.Length~1, data=iris) #mean value of Y predicts new Ys

full=lm(Sepal.Length~., data=iris) #include all Xs

step(null, scope=list(lower=null, upper=full), direction="both")


library(relaimpo)

# Bootstrap Measures of Relative Importance (1000 samples)
#drawing randomly with replacement from a set of data points

fit <- lm(formula = Sepal.Length ~ Petal.Length + Sepal.Width + 
            Petal.Width, data = iris)
boot <- boot.relimp(fit, b = 1000, type = c("lmg", 
                                            "last", "first", "pratt"), rank = TRUE, 
                    diff = TRUE, rela = TRUE) #different imp evaluation methods
#lmg is the R2 contribution averaged over orderings among regressors, cf
#last is each variables contribution when included last
#first is each variables contribution when included first,
booteval.relimp(boot) # print result
plot(booteval.relimp(boot,sort=TRUE)) # plot result
