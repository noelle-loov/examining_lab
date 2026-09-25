import numpy as np
import matplotlib.pyplot as plt
from utils import set_pyplot_to_swedish, linReg

set_pyplot_to_swedish(plt)

# Independent and dependent variables, rename as necessary to what was actually measured.
# Add or remove variables as necessary

# First set of measured values; varying ... (...) and measuring ... (...)
independent_1 = np.array([1, 2, 3, 4])
dependent_1 = np.array([1, 2, 3, 4])
# Convert to base units (remove prefix)
independent_1 *= 1
dependent_1 *= 1
# INCLUDE THE CONSTANT VALUES TOO IN ALL SETS OF MEASUREMENTS
independent_2 = np.array([1 for _ in range(4)])
independent_3 = np.array([1 for _ in range(4)])
independent_4 = np.array([1 for _ in range(4)])
independent_5 = np.array([1 for _ in range(4)])
independent_6 = np.array([1 for _ in range(4)])

# Linearize by taking the natural logarithm of both values, then perform regression
slope, intercept, slope_uncertainty, intercept_uncertainty = linReg(np.log(independent_1), np.log(dependent_1))

# Print slope and intercept; we mainly care about slope
print(f'slope 1: {slope} ± {slope_uncertainty:.2g}')
print(f'intercept 1: {intercept} ± {intercept_uncertainty:.2g}')

plt.plot(np.log(independent_1), np.log(dependent_1), 'bo', label='Measured data 1')
plt.plot(np.log(independent_1), slope*np.log(independent_1) + intercept, 'r-', label='Fitted line 1')
plt.xlabel('ln(independent variable 1)')
plt.ylabel('ln(dependent variable 1)')
plt.legend()
plt.show()


# Second set of measured values; ... (...) and ... (...)
independent_2 = np.array([2, 3, 4, 5])
dependent_2 = np.array([2, 3, 4, 5])
# Convert to base units (remove prefix)
independent_2 *= 1
dependent_2 *= 1

# Linearize by taking the natural logarithm of both values, then perform regression
slope, intercept, slope_uncertainty, intercept_uncertainty = linReg(np.log(independent_2), np.log(dependent_2))

# Print slope and intercept; we mainly care about slope
print(f'slope 2: {slope} ± {slope_uncertainty:.2g}')
print(f'intercept 2: {intercept} ± {intercept_uncertainty:.2g}')

plt.plot(np.log(independent_2), np.log(dependent_2), 'bo', label='Measured data 2')
plt.plot(np.log(independent_2), slope*np.log(independent_2) + intercept, 'r-', label='Fitted line 2')
plt.xlabel('ln(independent variable 2)')
plt.ylabel('ln(dependent variable 2)')
plt.legend()
plt.show()


# Second set of measured values; ... (...) and ... (...)
independent_3 = np.array([3, 4, 5, 6])
dependent_3 = np.array([3, 4, 5, 6])
# Convert to base units (remove prefix)
independent_3 *= 1
dependent_3 *= 1

# Linearize by taking the natural logarithm of both values, then perform regression
slope, intercept, slope_uncertainty, intercept_uncertainty = linReg(np.log(independent_3), np.log(dependent_3))

# Print slope and intercept; we mainly care about slope
print(f'slope 3: {slope} ± {slope_uncertainty:.2g}')
print(f'intercept 3: {intercept} ± {intercept_uncertainty:.2g}')

plt.plot(np.log(independent_3), np.log(dependent_3), 'bo', label='Measured data 3')
plt.plot(np.log(independent_3), slope*np.log(independent_3) + intercept, 'r-', label='Fitted line 3')
plt.xlabel('ln(independent variable 3)')
plt.ylabel('ln(dependent variable 3)')
plt.legend()
plt.show()


# Second set of measured values; ... (...) and ... (...)
independent_4 = np.array([4, 5, 6, 7])
dependent_4 = np.array([4, 5, 6, 7])
# Convert to base units (remove prefix)
independent_4 *= 1
dependent_4 *= 1

# Linearize by taking the natural logarithm of both values, then perform regression
slope, intercept, slope_uncertainty, intercept_uncertainty = linReg(np.log(independent_4), np.log(dependent_4))

# Print slope and intercept; we mainly care about slope
print(f'slope 4: {slope} ± {slope_uncertainty:.2g}')
print(f'intercept 4: {intercept} ± {intercept_uncertainty:.2g}')

plt.plot(np.log(independent_4), np.log(dependent_4), 'bo', label='Measured data 4')
plt.plot(np.log(independent_4), slope*np.log(independent_4) + intercept, 'r-', label='Fitted line 4')
plt.xlabel('ln(independent variable 4)')
plt.ylabel('ln(dependent variable 4)')
plt.legend()
plt.show()


# Second set of measured values; ... (...) and ... (...)
independent_5 = np.array([5, 6, 7, 8])
dependent_5 = np.array([5, 6, 7, 8])
# Convert to base units (remove prefix)
independent_5 *= 1
dependent_5 *= 1

# Linearize by taking the natural logarithm of both values, then perform regression
slope, intercept, slope_uncertainty, intercept_uncertainty = linReg(np.log(independent_5), np.log(dependent_5))

# Print slope and intercept; we mainly care about slope
print(f'slope 5: {slope} ± {slope_uncertainty:.2g}')
print(f'intercept 5: {intercept} ± {intercept_uncertainty:.2g}')

plt.plot(np.log(independent_5), np.log(dependent_5), 'bo', label='Measured data 5')
plt.plot(np.log(independent_5), slope*np.log(independent_5) + intercept, 'r-', label='Fitted line 5')
plt.xlabel('ln(independent variable 5)')
plt.ylabel('ln(dependent variable 5)')
plt.legend()
plt.show()


# Second set of measured values; ... (...) and ... (...)
independent_6 = np.array([6, 7, 8, 9])
dependent_6 = np.array([6, 7, 8, 9])
# Convert to base units (remove prefix)
independent_6 *= 1
dependent_6 *= 1

# Linearize by taking the natural logarithm of both values, then perform regression
slope, intercept, slope_uncertainty, intercept_uncertainty = linReg(np.log(independent_6), np.log(dependent_6))

# Print slope and intercept; we mainly care about slope
print(f'slope 6: {slope} ± {slope_uncertainty:.2g}')
print(f'intercept 6: {intercept} ± {intercept_uncertainty:.2g}')

plt.plot(np.log(independent_6), np.log(dependent_6), 'bo', label='Measured data 6')
plt.plot(np.log(independent_6), slope*np.log(independent_6) + intercept, 'r-', label='Fitted line 6')
plt.xlabel('ln(independent variable 6)')
plt.ylabel('ln(dependent variable 6)')
plt.legend()
plt.show()

# Extra exponents calculated rather than measured
exp_1: float = 1
exp_2: float = 1
exp_3: float = 1

