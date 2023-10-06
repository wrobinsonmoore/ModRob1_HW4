import sympy as sp

# Define symbolic variables
alpha, beta, gamma = sp.symbols('alpha beta gamma')

# Matrices
I = sp.eye(3)
R_z_alpha = sp.Matrix([[sp.cos(alpha), -sp.sin(alpha), 0], [sp.sin(alpha), sp.cos(alpha), 0], [0, 0, 1]])
R_y_beta = sp.Matrix([[sp.cos(beta), 0, sp.sin(beta)], [0, 1, 0], [-sp.sin(beta), 0, sp.cos(beta)]])
R_z_gamma = sp.Matrix([[sp.cos(gamma), -sp.sin(gamma), 0], [sp.sin(gamma), sp.cos(gamma), 0], [0, 0, 1]])

# The final rotation matrix to obtain Euler angles is
R_before_simp = I @ R_z_alpha @ R_y_beta @ R_z_gamma

# Simplify the result
R = sp.simplify(R_before_simp)

# Display the simplified result
print(f"The final result is:\n")
sp.pprint(R)