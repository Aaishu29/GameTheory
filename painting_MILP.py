import cvxpy as cp
import numpy as np

x = cp.Variable(nonneg=True)
y = cp.Variable(integer=True)
prob = cp.Problem(cp.Maximize(3*x + 2*y), [4*x + 2*y <= 15, 
                                            x + 2*y <= 8, 
                                            x + y <= 5])
prob.solve()


print("The optimal value is", prob.value)
print("A solution x is", x.value)
print("A solution y is", y.value)
