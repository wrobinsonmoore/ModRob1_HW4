# Imports
import numpy as np

# Set the numpy print preferences
np.set_printoptions(suppress=True)

# For QUESTION 1. Uncomment if needed!
theta = np.sqrt(5)
w_hat_bracket = np.array([[0, 0, 2/np.sqrt(5)], [0, 0, -1/np.sqrt(5)], [-2/np.sqrt(5), 1/np.sqrt(5), 0]])
result = np.eye(3) + np.sin(theta)*w_hat_bracket + (1-np.cos(theta))*np.matmul(w_hat_bracket, w_hat_bracket)

# Print the result!
print("Result = ")
print(result)