# Hypothesis Testing: Weekly Operating Costs of Bombay Hospitality Ltd.

import math
from scipy import stats

# Step 1: Hypotheses
# H0: The weekly operating cost follows the given model (W = 1000 + 5X)
# H1: The weekly operating cost is higher than the given model

# Step 2: Given data
sample_mean=3050       # observed mean weekly cost
n=25                   # sample size
X_mean=600             # mean number of units produced
X_sd=25                # standard deviation of units

# Theoretical mean cost according to model
mu=1000+5 * X_mean   # 1000 + 5*600 = 4000

# Standard deviation of weekly cost
sigma=5 * X_sd         # 5 * 25 = 125

# Standard error of the mean
se=sigma/math.sqrt(n)

# Step 3: Test statistic (Z-test because sigma is known)
z=(sample_mean - mu) / se

# Step 4: Critical value for alpha = 0.05 (one-tailed test)
alpha=0.05
z_critical=stats.norm.ppf(1-alpha)

# Step 5: Decision
print("Theoretical mean cost (mu):",mu)
print("Observed sample mean:",sample_mean)
print("Z statistic:",round(z,2))
print("Critical value:",round(z_critical,2))

if z>z_critical:
    print("Conclusion: Reject H0. There is evidence that the weekly cost is higher than the model suggests.")
else:
    print("Conclusion: Fail to reject H0. Not enough evidence that the weekly cost is higher.")
