import cvxpy as cp
import numpy as np
# Supply and demand at each point
v = np.array([2, 2,-3,-7,6])
# cost of transshipment between 2 points
c = np.array([[0,6,4,3,0],
             [6,0,2,5,2],
             [4,2,0,0,7],
             [3,5,0,0,0],
             [0,2,7,0,0]
             ])

z = np.zeros_like(c)
# Number of units transfered between two points
x = cp.Variable((5,5), integer=True)
#The number of units transferred should greater than or equal to zero(non negetive)
constraints =[x>=z]

for i in range(0,5):
    sum1=0
    sum2=0
    for j in range(0,5):
        sum1+=x[i][j]
        sum2+=x[j][i]
        if c[i][j]==0:
            #If there is no direct path between points then the number of units transfered shall be zero
            constraints+=[x[i][j]==0]
    #The number of incoming and outgoing costs shall satisfy the demand
    constraints+=[sum2-sum1==v[i]]

prob = cp.Problem(cp.Minimize(cp.sum(cp.multiply(c,x))), constraints)
prob.solve()

print("The optimal value is when units are integer parts", prob.value)
print("The units transferred matrix is",x.value)

print("------------------------------------------------------------------------------------------------------------------")

y = cp.Variable((5,5), nonneg=True)
#The number of units transferred should greater than or equal to zero(non negetive)
constraint =[y>=z]

for i in range(0,5):
    sum1=0
    sum2=0
    for j in range(0,5):
        sum1+=y[i][j]
        sum2+=y[j][i]
        if c[i][j]==0:
            #If there is no direct path between points then the number of units transfered shall be zero
            constraint+=[y[i][j]==0]
    #The number of incoming and outgoing costs shall satisfy the demand
    constraint+=[sum2-sum1==v[i]]

prob = cp.Problem(cp.Minimize(cp.sum(cp.multiply(c,y))), constraint)
prob.solve()

print("The optimal value is when units are fractional parts", prob.value)
print("The units transferred matrix is",x.value)



