import numpy as np
import matplotlib.pyplot as plt
from utils import set_pyplot_to_swedish, linReg

set_pyplot_to_swedish(plt)


# First set of measured values; varying Amplitude (cm) and measuring period time (s)
amplitude_1 = np.array([1, 2, 3, 4, 5])
period_1 = np.array([0.123, 0.123, 0.123, 0.123, 0.123])
# First set of constant values, all 3 are measured in cm
length_1 = np.array([69.6 for _ in range(5)])
width_1 = np.array([2.02 for _ in range(5)])
height_1 = np.array([0.515 for _ in range(5)])
# Convert to base units (remove prefix)
amplitude_1 *= 100
period_1 *= 1
length_1 *= 100
width_1 *= 100
height_1 *= 100

# Linearize by taking the natural logarithm of both values, then perform regression
slope, intercept, slope_uncertainty, intercept_uncertainty = linReg(np.log(amplitude_1), np.log(period_1))

# Print slope and intercept; we mainly care about slope
print(f'slope 1: {slope} ± {slope_uncertainty:.2g}')
print(f'intercept 1: {intercept} ± {intercept_uncertainty:.2g}')

plt.plot(np.log(amplitude_1), np.log(period_1), 'bo', label='Measured period time with varied amplitude')
plt.plot(np.log(amplitude_1), slope*np.log(amplitude_1) + intercept, 'r-', label='Fitted line')
plt.xlabel('ln(amplitude (m)) (ln(m))')
plt.ylabel('ln(period (s)) (ln(s))')
plt.legend()
plt.show()

# Since the slope for the first set of measurements is almost 0, we assume the period time is independent of the amplitude.
# Amplitude will be ignored for future measurements.

# Second set of measured values; length (cm) and period time (s)
length_2 = np.array([2, 3, 4, 5])
period_2 = np.array([2, 3, 4, 5])
# Second set of constant values, all 3 are measured in cm
width_2 = np.array([2.02 for _ in range(5)])
height_2 = np.array([0.515 for _ in range(5)])
# Convert to base units (remove prefix)
length_2 *= 100
period_2 *= 1
width_2 *= 100
height_2 *= 100

# Linearize by taking the natural logarithm of both values, then perform regression
slope, intercept, slope_uncertainty, intercept_uncertainty = linReg(np.log(length_2), np.log(period_2))

# Print slope and intercept; we mainly care about slope
print(f'slope 2: {slope} ± {slope_uncertainty:.2g}')
print(f'intercept 2: {intercept} ± {intercept_uncertainty:.2g}')

plt.plot(np.log(length_2), np.log(period_2), 'bo', label='Measured period time with varied length')
plt.plot(np.log(length_2), slope*np.log(length_2) + intercept, 'r-', label='Fitted line')
plt.xlabel('ln(length (m)) (ln(m))')
plt.ylabel('ln(period (s)) (ln(s))')
plt.legend()
plt.show()


# Third set of measured values; width (cm) and period time (s)
width_3 = np.array([3, 4, 5, 6])
period_3 = np.array([3, 4, 5, 6])
# Third set of constant values, all 3 are measured in cm
length_3 = np.array([INPUT_HERE for _ in range(5)])
height_3 = np.array([INPUT_HERE for _ in range(5)])
# Convert to base units (remove prefix)
width_3 *= 100
period_3 *= 1
length_3 *= 100
height_3 *= 100

# Linearize by taking the natural logarithm of both values, then perform regression
slope, intercept, slope_uncertainty, intercept_uncertainty = linReg(np.log(width_3), np.log(period_3))

# Print slope and intercept; we mainly care about slope
print(f'slope 3: {slope} ± {slope_uncertainty:.2g}')
print(f'intercept 3: {intercept} ± {intercept_uncertainty:.2g}')

plt.plot(np.log(width_3), np.log(period_3), 'bo', label='Measured period time with varied width')
plt.plot(np.log(width_3), slope*np.log(width_3) + intercept, 'r-', label='Fitted line')
plt.xlabel('ln(width (m)) (ln(m))')
plt.ylabel('ln(period (s)) (ln(s))')
plt.legend()
plt.show()


# Fourth set of measured values; height (cm) and period time (s))
height_4 = np.array([4, 5, 6, 7])
period_4 = np.array([4, 5, 6, 7])
# Fourth set of constant values, all 4 are measured in cm
length_4 = np.array([INPUT_HERE for _ in range(5)])
width_4 = np.array([INPUT_HERE for _ in range(5)])
# Convert to base units (remove prefix)
height_4 *= 100
period_4 *= 1
length_4 *= 100
width_4 *= 100

# Linearize by taking the natural logarithm of both values, then perform regression
slope, intercept, slope_uncertainty, intercept_uncertainty = linReg(np.log(height_4), np.log(period_4))

# Print slope and intercept; we mainly care about slope
print(f'slope 4: {slope} ± {slope_uncertainty:.2g}')
print(f'intercept 4: {intercept} ± {intercept_uncertainty:.2g}')

plt.plot(np.log(height_4), np.log(period_4), 'bo', label='Measured period time with varied height')
plt.plot(np.log(height_4), slope*np.log(height_4) + intercept, 'r-', label='Fitted line 4')
plt.xlabel('ln(height (m)) (ln(m))')
plt.ylabel('ln(period (s)) (ln(s))')
plt.legend()
plt.show()

# Extra exponents calculated rather than measured
exp_1: float = 1
exp_2: float = 1
exp_3: float = 1

# Copy in formula for calculation constant

# Set up long arrays for the independent variables, padded with the constant values when they are not being varied
