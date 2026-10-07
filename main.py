import numpy as np
import matplotlib.pyplot as plt
from utils import set_pyplot_to_swedish, linReg

set_pyplot_to_swedish(plt)


# First set of measured values; varying Amplitude (cm) and measuring period time (s)
amplitude_1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
period_1 = np.array([0.123, 0.123, 0.123, 0.123, 0.123])
# First set of constant values, all 3 are measured in cm
length_1 = np.array([69.6 for _ in range(5)])
width_1 = np.array([2.02 for _ in range(5)])
height_1 = np.array([0.515 for _ in range(5)])
# Convert to base units (remove prefix)
amplitude_1 *= 0.01
period_1 *= 1
length_1 *= 0.01
width_1 *= 0.01
height_1 *= 0.01

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
length_2 = np.array([55.05, 60.15, 65.2, 69.6, 75.1])
period_2 = np.array([0.078, 0.091, 0.107, 0.123, 0.141])
# Second set of constant values, both are measured in cm
width_2 = np.array([2.02 for _ in range(5)])
height_2 = np.array([0.515 for _ in range(5)])
# Convert to base units (remove prefix)
length_2 *= 0.01
period_2 *= 1
width_2 *= 0.01
height_2 *= 0.01

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
width_3 = np.array([2.04, 3.02, 4.03, 5.00])
period_3 = np.array([0.182, 0.185, 0.182, 0.188])
# Third set of constant values, both are measured in cm
# Length varies slightly due to human error in setting up the experiment
length_3 = np.array([70.15, 70.05, 70.1, 70.1])
height_3 = np.array([0.35 for _ in range(4)])
# Convert to base units (remove prefix)
width_3 *= 0.01
period_3 *= 1
length_3 *= 0.01
height_3 *= 0.01

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

# Since the slope for the third set of measurements is almost 0, we assume the period time is independent of the width.
# Width will be ignored for future measurements.


# Fourth set of measured values; height (cm) and period time (s))
height_4 = np.array([0.35, 0.51, 0.82, 1.02])
period_4 = np.array([0.268, 0.181, 0.117, 0.096])
# Fourth constant value, measured in cm
length_4 = np.array([85.0, 85.05, 85.05, 85.0])
# Convert to base units (remove prefix)
height_4 *= 0.01
period_4 *= 1
length_4 *= 0.01

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
gravity_exponent: float = 0
density_exponent: float = 0.5
elasticity_exponent: float = -0.5

# Values for the above constants, given by lab instructor
# Gravity in Sundsvall
gravity: float = 9.82 # m/s^2
# Density of steel
density: float = 7850 # kg/m^3
# Elasticity of steel
elasticity: float = 200 # GPa
#Convert elasticity to Pa
elasticity *= 1e9

# Copy in formula for calculating constant
all_periods = np.concatenate([period_1, period_2, period_3, period_4])

all_length = np.concatenate([length_1, length_2, length_3, length_4])
all_height = np.concatenate([height_1, height_2, height_3, height_4])

x = (all_length**2 / all_height) * np.sqrt(density / elasticity)

slope, intercept, slope_uncertainty, intercept_uncertainty = linReg(x, all_periods)
print(f'slope all: {slope} ± {slope_uncertainty:.2g}')
print(f'intercept all: {intercept} ± {intercept_uncertainty:.2g}')

plt.plot(x, all_periods, 'bo', label='Measured period time with varied parameters')
plt.plot(x, slope*x + intercept, 'r-', label='Fitted line all')
plt.xlabel('(length^2 / height) * (density / elasticity)^0.5 (m)')
plt.ylabel('period (s)')
plt.legend()
plt.show()

relevant_periods = np.concatenate([period_2, period_4])
relevant_lengths = np.concatenate([length_2, length_4])
relevant_heights = np.concatenate([height_2, height_4])

relevant_x = (relevant_lengths**2 / relevant_heights) * np.sqrt(density / elasticity)

slope, intercept, slope_uncertainty, intercept_uncertainty = linReg(relevant_x, relevant_periods)
print(f'slope relevant: {slope} ± {slope_uncertainty:.2g}')
print(f'intercept relevant: {intercept} ± {intercept_uncertainty:.2g}')

plt.plot(relevant_x, relevant_periods, 'bo', label='Measured period time with relevant parameters')
plt.plot(relevant_x, slope*relevant_x + intercept, 'r-', label='Fitted line relevant')
plt.xlabel('(length^2 / height) * (density / elasticity)^0.5 (m)')
plt.ylabel('period (s)')
plt.legend()
plt.show()

# Based on only length
x = (length_2**2 / height_2) * np.sqrt(density / elasticity)

slope, intercept, slope_uncertainty, intercept_uncertainty = linReg(x, period_2)
print(f'slope length only: {slope} ± {slope_uncertainty:.2g}')
print(f'intercept length only: {intercept} ± {intercept_uncertainty:.2g}')

plt.plot(x, period_2, 'bo', label='Measured period time with only length varied')
plt.plot(x, slope*x + intercept, 'r-', label='Fitted line length only')
plt.xlabel('(length^2 / height) * (density / elasticity)^0.5 (m)')
plt.ylabel('period (s)')
plt.legend()
plt.show()