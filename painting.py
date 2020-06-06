import cvxpy as cp

x = cp.Variable(nonneg=True)
y = cp.Variable(nonneg=True)
prob = cp.Problem(cp.Maximize(3*x + 2*y), [4*x + 2*y <= 16, 
                                            x + 2*y <= 8, 
                                            x + y <= 5])
prob.solve()


print("The optimal value is", prob.value)
print("A solution x is", x.value)
print("A solution y is", y.value)
