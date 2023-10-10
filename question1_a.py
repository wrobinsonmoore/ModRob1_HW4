# Imports
import numpy as np
import matplotlib.pyplot as plt
        

# Set the numpy print preferences
np.set_printoptions(suppress=True)

# Input your rotation matrix here
R = np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]]) # For Question 1
# R = np.array([[0, 0, 1], [0, -1, 0], [1, 0, 0]]) # for Question 2

# Calculate theta
theta1 = np.arccos((R[0][0] + R[1][1] + R[2][2] - 1)/2)
theta2 = -theta1 # Because it's cosine

# For exponential coordinates
# Scenario 1: sin(theta) != 0
tolerance = 1e-5
if np.sin(theta1) <= (0-tolerance) or (np.sin(theta1) >= (0+tolerance)):
    
    w_hat_bracket_1 = 1/(2*np.sin(theta1)) * (R - R.T)
    w1_hat_1 = w_hat_bracket_1[2][1]
    w2_hat_1 = w_hat_bracket_1[0][2]
    w3_hat_1 = w_hat_bracket_1[1][0]
    w_hat1 = [w1_hat_1, w2_hat_1, w3_hat_1]
    
    w_hat_bracket_2 = 1/(2*np.sin(theta2)) * (R - R.T)
    w1_hat_2 = w_hat_bracket_2[2][1]
    w2_hat_2 = w_hat_bracket_2[0][2]
    w3_hat_2 = w_hat_bracket_2[1][0]
    w_hat2 = [w1_hat_2, w2_hat_2, w3_hat_2]

    # Print the result!
    print(f"\nWith theta1 = {theta1} rad, w_hat_bracket is = ")
    print(w_hat_bracket_1)
    print(f"\nAnd the w_hat is = {w_hat1}\n")
    print(f"\nWith theta2 = {theta2} rad, w_hat_bracket is = ")
    print(w_hat_bracket_2, "\n")
    print(f"\nAnd the w_hat is = {w_hat2}\n")

    # And plot the w_hat axes!
    # Create vectors for the coordinate frame
    origin = np.zeros(3)
    x_axis = [1, 0, 0]
    y_axis = [0, 1, 0]
    z_axis = [0, 0, 1]
    w_axis_1 = w_hat1
    w_axis_2 = w_hat2

    # Visualize the coordinate frame
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(*origin, *x_axis, color='r', label='X-axis')
    ax.quiver(*origin, *y_axis, color='g', label='Y-axis')
    ax.quiver(*origin, *z_axis, color='b', label='Z-axis')
    ax.quiver(*origin, *w_axis_1, color='y', label='w1')
    ax.quiver(*origin, *w_axis_2, color='orange', label='w2')

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

    plt.show()

# Scenario 2: theta = k*pi AND k is an EVEN integer
elif theta1/np.pi % 2 == 0:
    print("\nRESULT: w_hat cannot be obtained because R = I and the axis of rotation is undefined!\n")

# Scenario 3: theta = k*pi AND k is an ODD integer
elif theta1/np.pi % 2 != 0:
    # We need to find the individual components of [w_hat]
    w1_hat_pos1 = np.sqrt((R[0][0] + 1)/2)
    w1_hat_pos2 = -np.sqrt((R[0][0] + 1)/2)
    w2_hat_pos1 = np.sqrt((R[1][1] + 1)/2)
    w2_hat_pos2 = -np.sqrt((R[1][1] + 1)/2)
    w3_hat_pos1 = np.sqrt((R[2][2] + 1)/2)
    w3_hat_pos2 = -np.sqrt((R[2][2] + 1)/2)

    # Go through all the potential combinations of (w1_hat, w2_hat, w3_hat)
    potential_combinations = [[w1_hat_pos1, w2_hat_pos1, w3_hat_pos1],
                              [w1_hat_pos1, w2_hat_pos1, w3_hat_pos2],
                              [w1_hat_pos1, w2_hat_pos2, w3_hat_pos1],
                              [w1_hat_pos1, w2_hat_pos2, w3_hat_pos2],
                              [w1_hat_pos2, w2_hat_pos1, w3_hat_pos1],
                              [w1_hat_pos2, w2_hat_pos1, w3_hat_pos2],
                              [w1_hat_pos2, w2_hat_pos2, w3_hat_pos1],
                              [w1_hat_pos2, w2_hat_pos2, w3_hat_pos2]]

    # Check which are actual solutions
    solutions = []
    for combination in potential_combinations:
        w1_hat = combination[0]
        w2_hat = combination[1]
        w3_hat = combination[2]
        w_hat = np.array([[2*np.power(w1_hat, 2)-1, 2*w1_hat*w2_hat, 2*w1_hat*w3_hat],
                        [2*w1_hat*w2_hat, 2*np.power(w2_hat, 2)-1, 2*w2_hat*w3_hat], 
                        [2*w1_hat*w3_hat, 2*w2_hat*w3_hat, 2*np.power(w3_hat, 2)-1]])
        
        # Check if this is equal to R, and if so, check if it has been added to solutions. If NOT, then add it as a potential solution:
        if np.allclose(R, w_hat, atol=tolerance):
            if [w1_hat, w2_hat, w3_hat] not in solutions:
                solutions.append([w1_hat, w2_hat, w3_hat])
        
        # Stop if two solutions have been found
        if len(solutions) >= 2:
            break
        
    # Save them with the appropriate name
    w_hat1 = solutions[0]
    w_hat2 = solutions[1]

    # Print the result!
    print(f"\nWith theta1 = {theta1} rad, w_hat is = ")
    print(w_hat1)
    print(f"\nWith theta2 = {theta1} rad, w_hat is = ")
    print(w_hat2, "\n")

    # And plot the w_hat axes!
    # Create vectors for the coordinate frame
    origin = np.zeros(3)
    x_axis = [1, 0, 0]
    y_axis = [0, 1, 0]
    z_axis = [0, 0, 1]
    w_axis_1 = w_hat1
    w_axis_2 = w_hat2

    # Visualize the coordinate frame
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(*origin, *x_axis, color='r', label='X-axis')
    ax.quiver(*origin, *y_axis, color='g', label='Y-axis')
    ax.quiver(*origin, *z_axis, color='b', label='Z-axis')
    ax.quiver(*origin, *w_axis_1, color='y', label='w1')
    ax.quiver(*origin, *w_axis_2, color='orange', label='w2')

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

    plt.show()
    

