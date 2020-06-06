import cvxpy as cp
import numpy as np

# Rows: NA, SA, As, Au, E, Af
A = np.array([[1, 0, 1, 0, 0, 1], 
              [1, 0, 0, 1, 0, 0], 
              [0, 1, 0, 1, 1, 0],
              [0, 0, 1, 0, 1, 0], 
              [0, 1, 1, 1, 0, 1],
              [1, 1, 0, 0, 1, 0]])

b = np.ones(6)

x = cp.Variable(6, boolean=True)
cost = cp.sum(x)
prob = cp.Problem(cp.Minimize(cost), [A@x >= b])
prob.solve()


print("The optimal value is", prob.value)
print("A solution x is", x.value)
