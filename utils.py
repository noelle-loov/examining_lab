import numpy as np

def set_pyplot_to_swedish(pltInstance):
  """
  This function accepts a matplotlib.pyplot instance and sets it to use Swedish locale formatting for numeric values.
  Uses unsafe member access of the subplots method from the input, which is assumed to be an instance of matplotlib.pyplot, but no checks are made.
  """
  import locale
  _, axes = pltInstance.subplots()
  locale.setlocale(locale.LC_NUMERIC, ('sv_SE', 'UTF-8'))
  axes.ticklabel_format(useLocale=True)
  return

def linReg(x: np.ndarray, y: np.ndarray):
  """
  Performs linear regression on the given x and y data.
  x: independent variable (numpy array)
  y: dependent variable (numpy array)

  Returns: (k1, k2, u1, u2)
  k1: slope of the fitted line
  k2: intercept of the fitted line
  u1: uncertainty in the slope
  u2: uncertainty in the intercept
  """
  n = len(x)
  k1: int | float = (n*np.sum(x*y)-np.sum(x)*np.sum(y)) / ( n*np.sum(x**2)-np.sum(x)**2)
  k2: int | float = (np.sum(y) - (k1 * np.sum(x))) / n

  # Standard deviation for the regression
  dev = np.sqrt((1 / (n - 2)) * np.sum((y - (k1 * x) - k2) ** 2))
  meanX = np.mean(x)
  # Uncertainty in slope
  u1: int | float = dev * np.sqrt(1/np.sum((x - meanX) ** 2))
  # Uncertainty in intercept
  u2: int | float = dev * np.sqrt((1/n) + ((meanX ** 2) / np.sum((x - meanX) ** 2)))

  return (k1, k2, u1, u2)