import cvxpy as cp
import numpy as np

Big = 50

# location
l = np.array([1, 4, 7, 9, 15])
# customers
c = np.array([2, 1, 3, 4, 3])
# willing to walk
w = np.array([4, 2, 3, 3, 2])


# position of stations
x = cp.Variable(2, nonneg=True)
# whether each group is served by any of stations
y = cp.Variable(5, boolean=True)
# whether each group is served by each station
z = cp.Variable((2, 5), boolean=True)

# if group j is not served by any of stations, then y[j] should be zero
constraints = [cp.sum(z, axis=0) - y >= 0]

# if left/right distance between station i and group j is more than w[j], then z[i,j] should be zero
for i in range(2):
  for j in range(5):
    constraints += [x[i] - l[j] - w[j] <= Big - Big * z[i,j]]
    constraints += [l[j] - x[i] - w[j] <= Big - Big * z[i,j]]

prob = cp.Problem(cp.Maximize(c@y), constraints)
prob.solve()


print("The optimal value is", prob.value)
print("A solution x is", x.value)
print("A solution y is", y.value)
print("A solution z is", z.value)
