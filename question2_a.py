import numpy as np

R = np.array([[0, 0, 1], [0, -1, 0], [1, 0, 0]])

w_hat = np.sqrt((R - 1)/2)

print(w_hat)

print((np.cos(220.76*np.pi/180)))