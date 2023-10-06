"""
This file was used to answer Question 1 (d, e, f, g) and Question 2!
"""

# Imports
import numpy as np

# Set the numpy print preferences
np.set_printoptions(suppress=True)


# For exponential coordinates
theta1 = 2*np.pi/3
theta2 = 4*np.pi/3
R = np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]])
w_hat1 = 1/(2*np.sin(theta1)) * (R - R.T)
w_hat2 = 1/(2*np.sin(theta2)) * (R - R.T)

# Print the result!
print("\nOPTION 1: w_hat is = ")
print(w_hat1)
print("\nOPTION 2: w_hat is = ")
print(w_hat2)
print(1/np.sqrt(3))