import numpy as np

# Define your Roll-Pitch-Yaw (rpy) angles 
roll = 30*np.pi/180
gamma_rpy = roll
pitch = 60*np.pi/180
beta_rpy = pitch
yaw = 45*np.pi/180
alpha_rpy = yaw

# Obtain the equivalents in ZYZ (results in deg). The other potential answer will be given by our knowledge of each of the trigonometrical functions!
beta = (np.arccos(np.cos(beta_rpy)*np.cos(gamma_rpy)))*180/np.pi
gamma = (np.arctan((np.sin(gamma_rpy)*np.cos(beta_rpy))/(np.sin(beta_rpy)))*180/np.pi)
alpha = (np.arcsin((np.sin(alpha_rpy)*np.sin(beta_rpy)*np.cos(gamma_rpy) - np.sin(gamma_rpy)*np.cos(alpha_rpy))/(np.sin(np.arccos(np.cos(beta_rpy)*np.cos(gamma_rpy))))))*180/np.pi

# Obtain one possibility for each ZYZ angle and print it
print(f"alpha = {alpha}")
print(f"beta = {beta}")
print(f"gamma = {gamma}")

# print(np.sin(45*np.pi/180)*np.sin(60*np.pi/180)*np.cos(30*np.pi/180) - np.sin(30*np.pi/180)*np.cos(45*np.pi/180))
print(np.sin(191.31*np.pi/180)*np.sin(295.66*np.pi/180))
# print((np.sin(alpha_rpy)*np.sin(beta_rpy)*np.cos(gamma_rpy) - np.sin(gamma_rpy)*np.cos(alpha_rpy))/(np.sin(np.arccos(np.cos(beta_rpy)*np.cos(gamma_rpy)))))

