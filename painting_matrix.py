import cvxpy as cp
import numpy as np

A = np.array([[4, 2], [1, 2], [1, 1]])
b = np.array([16, 8, 5])
c = np.array([3, 2])

x = cp.Variable(2, nonneg=True)
prob = cp.Problem(cp.Maximize(c@x), [A@x <= b])
prob.solve()


print("The optimal value is", prob.value)
print("A solution x is", x.value)
