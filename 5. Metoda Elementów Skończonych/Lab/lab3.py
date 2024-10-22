import math

# Node coordinates
x_coords = [0, 4, 4, 0]
y_coords = [0, 0, 4, 5]

# Derivatives of shape functions with respect to ξ and η
def calculate_partial_derivatives(xi, eta):
    dN1_dxi = -(1 / 4) * (1 - eta)
    dN2_dxi = (1 / 4) * (1 - eta)
    dN3_dxi = (1 / 4) * (1 + eta)
    dN4_dxi = -(1 / 4) * (1 + eta)

    dN1_deta = -(1 / 4) * (1 - xi)
    dN2_deta = -(1 / 4) * (1 + xi)
    dN3_deta = (1 / 4) * (1 + xi)
    dN4_deta = (1 / 4) * (1 - xi)

    return [dN1_dxi, dN2_dxi, dN3_dxi, dN4_dxi], [dN1_deta, dN2_deta, dN3_deta, dN4_deta]

# Function to compute the Jacobian matrix
def compute_jacobian(x_coords, y_coords, xi, eta):
    # Get the partial derivatives
    dN_dxi, dN_deta = calculate_partial_derivatives(xi, eta)

    # Calculate the Jacobian components
    dx_dxi = sum(dN_dxi[i] * x_coords[i] for i in range(4))
    dy_dxi = sum(dN_dxi[i] * y_coords[i] for i in range(4))
    dx_deta = sum(dN_deta[i] * x_coords[i] for i in range(4))
    dy_deta = sum(dN_deta[i] * y_coords[i] for i in range(4))

    return [[dx_dxi, dy_dxi], [dx_deta, dy_deta]]

# Example usage with ξ = -1/sqrt(3) and η = -1/sqrt(3)
xi = -1 / math.sqrt(3)
eta = -1 / math.sqrt(3)

jacobian_matrix = compute_jacobian(x_coords, y_coords, xi, eta)
print("Jacobian matrix at ξ =", xi, "and η =", eta, "is:")
for row in jacobian_matrix:
    print(row)
