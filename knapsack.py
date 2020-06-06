import cvxpy as cp
import numpy as np

A = np.array([[16, 4, 6], 
              [3, 4, 3], 
              [1, 0, 0], 
              [0, 1, 0], 
              [0, 0, 1]])

b = np.array([30, 20, 3, 4, 1])
c = np.array([11, 4, 9])

x = cp.Variable(3, integer=True)
prob = cp.Problem(cp.Maximize(c@x), [A@x <= b])
prob.solve()


print("The optimal value is", prob.value)
print("A solution x is", x.value)
