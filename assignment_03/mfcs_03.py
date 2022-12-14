import numpy as np

def Newton_system(F, J, x, eps):
    """
    Solve nonlinear system F=0 by Newton's method.
    J is the Jacobian of F. Both F and J must be functions of x.
    At input, x holds the start value. The iteration continues
    until ||F|| < eps.
    """
    F_value = F(x)
    F_norm = np.linalg.norm(F_value, ord=2)  # l2 norm of vector
    iteration_counter = 0
    # while abs(F_norm) > eps and iteration_counter < 100:
    for _ in range(eps):
        delta = np.linalg.solve(J(x), -F_value)
        x = x + delta
        F_value = F(x)
        F_norm = np.linalg.norm(F_value, ord=2)
        iteration_counter += 1

    # Here, either a solution is found, or too many iterations
    # if abs(F_norm) > eps:
    #     iteration_counter = -1
    return x#, iteration_counter

def f(x):
    return np.array([
        x[1]**2 - 1,
        x[0] + x[1] - 2
    ])

def J(x):
    return np.array([
        [0, 2*x[1]],
        [1, 1]
    ])

print(Newton_system(f, J, np.array([0, 2]), 2))