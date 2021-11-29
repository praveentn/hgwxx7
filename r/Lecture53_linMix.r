###############################################
############### LINEAR MIXED EFFECT MODEL

#### Regression models: modelled the impact of fixed effects.
#are constant across individuals,
#### Mixed effect models- account for random effects
#vary across individuaals
#Effects are fixed if they are interesting in themselves 
#or random if there is interest in the underlying population

library(lme4)

### specify random effect:  (1 | grouping factor) )
### random effect model generated for each level of grouping factor
### provide another way to quantify individual differences.

#experiment on the effect of diet on early growth of chicks
#allowing for individual variability in weight of each Chick (random)
#(in technical terms, a random intercept for each Chick: (1 | Chick) )


model = lmer(log(weight) ~ Time*Diet + (1 | Chick), data=ChickWeight,REML=F)

summary(model)

#Model parameters are computed using maximum likelihood estimates using REML=F


##fixed effects of diet & time on the intercept
#a constant difference in weights among chicks 
#randomly assigned to different diets
#random intercept model
model2 = lmer(log(weight) ~ Time+Diet + (1 | Chick), data=ChickWeight,REML=F)

summary(model2)

#impact ofinteraction bw diet and time
# quantify the impact on 
#the slope (i.e., effects of diet on the rate of growth)
model3 = lmer(log(weight) ~ Time*Diet + (1 | Chick), data=ChickWeight,REML=F)

summary(model3)

coef(summary(model3))

anova(model2,model3)
##Is the interaction between time and diet significant?
#interaction bw time and weight is signidicant
# all four diets influence weight gain differently

coeffs <- coef(summary(model3))
p <- pnorm(abs(coeffs[, "t value"]), lower.tail = FALSE) * 2

library(ggplot2)
ggplot(fortify(model2), aes(Time, weight, color=Diet)) +
  stat_summary(fun.data=mean_se, geom="pointrange") +
  stat_summary(aes(y=.fitted), fun.y=mean) #diets influence wt gain

##impact of diet 1 on checken weight
exp(0.0765) #a 7.9% increase

#impact of diet 2

exp(0.067+0.048) #12.1% increase in weight 


##Random slopes (no random intercept): allowing for a different average slope for each diet

model4 = lmer(log(weight) ~ Time*Diet +  (0 + Time | Chick), data=ChickWeight,REML=F)

summary(model4)

library(lsmeans)
library(lmerTest)

Clst <- lstrends (model4, ~ Diet, var = "Time")
#estimate and compare the average
#slopes for each diet

## for random slope & intercept : (1 + Time | Chick)