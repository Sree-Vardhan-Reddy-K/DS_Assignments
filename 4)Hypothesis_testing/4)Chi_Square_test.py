#---------CHI SQUARE TEST--------------

import numpy as np
from scipy.stats import chi2

# Step 1: State the Hypotheses
# H0 (Null Hypothesis): Device type and satisfaction level are independent.
# H1 (Alternative Hypothesis): Device type and satisfaction level are NOT independent (there is an association).

# Step 2: Observed Data
observed = np.array([
    [50, 70],   # Very Satisfied
    [80, 100],  # Satisfied
    [60, 90],   # Neutral
    [30, 50],   # Unsatisfied
    [20, 50]    # Very Unsatisfied
])

row_totals=observed.sum(axis=1)   # Row sums
col_totals=observed.sum(axis=0)   # Column sums
grand_total=observed.sum()        # Overall total

# Step 3: Compute Expected Frequencies
# Formula: E_ij = (row_total * col_total) / grand_total

expected=np.outer(row_totals,col_totals)/grand_total

# Step 4: Compute Chi-Square Statistic
# Formula: sum((O-E)^2/E)
chi_square_stat=((observed-expected)**2/expected).sum()

# Degrees of freedom = (rows-1) * (cols-1)
df=(observed.shape[0]-1)*(observed.shape[1]-1)

# Significance level
alpha=0.05

# Critical value from Chi-Square distribution
critical_value=chi2.ppf(1-alpha,df)

# p-value
p_value=1-chi2.cdf(chi_square_stat,df)

# Step 5: Print Detailed Report
print("CHI-SQUARE TEST REPORT")
print("----------------------")

print("1. Hypotheses:")
print("   H0: Device type and satisfaction level are independent.")
print("   H1: Device type and satisfaction level are associated.")

print("\n2. Observed Frequencies:")
print(observed)

print("\n3. Expected Frequencies (under H0):")
print(expected.round(2))

print(f"\n4. Chi-Square Statistic = {chi_square_stat:.4f}")
print(f"   Degrees of Freedom   = {df}")
print(f"   Critical Value (α=0.05) = {critical_value:.4f}")
print(f"   p-value = {p_value:.4f}")

print("\n5. Decision:")
if chi_square_stat>critical_value:
    print("   Reject H0 → There IS a significant association between device type and satisfaction.")
else:
    print("   Fail to Reject H0 → NO significant association between device type and satisfaction.")

print("\nConclusion:")
print("At the 5 percent significance level, the test shows that device type and customer satisfaction")
print("are not significantly associated. Any differences observed may be due to chance.")
