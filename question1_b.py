import numpy as np

# Define the w_hat_theta vector
w_hat_theta = np.array([1, 2, 0])

# Obtain the magnitude = theta
magnitude = np.linalg.norm(w_hat_theta)
theta = magnitude

# Obtain the unit vector
w_hat = [w_hat_theta[0]/magnitude, w_hat_theta[1]/magnitude, w_hat_theta[2]/magnitude]
print(f"\nThe unit vector form is {w_hat} \n")

# Obtain the w_hat_bracket
w_hat_bracket = np.array([[0, -w_hat[2], w_hat[1]],
                          [w_hat[2], 0, -w_hat[0]],
                          [-w_hat[1], w_hat[0], 0]])
print(f"w_hat_bracket =\n {w_hat_bracket}\n")

# Obtain the final expression
answer = np.eye(3) + np.sin(theta)*w_hat_bracket + ((1-np.cos(theta))*(w_hat_bracket@w_hat_bracket))
print(f"The final answer is = \n{answer}\n")