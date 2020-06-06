import cvxpy as cp
import numpy as np
v = np.array([1,1,1,1])
# edge weight from {a,b,c,d} to {e,f,g,h}
c = np.array([[1,0,3,0],
             [0,2,0,4],
             [0,0,0,5],
             [0,1,2,0]
             ])

# boolean matrix to check whether the edge will result in maximum bipartite graph or not
x = cp.Variable((4,4), boolean=True)
y=[0,0,0,0]
constraints =[]

for i in range(0,4):
    sum1=0
    sum2=0
    for j in range(0,4):
        sum1+=x[i][j]
        sum2+=x[j][i]
    #the number of edges between any two vertices should be <=1. Therefore these constraints ensure that no row or column should sum upto more than one.
    constraints+=[sum1<=v[i]]
    constraints+=[sum2<=v[i]]
#maximizing the set of edges
prob = cp.Problem(cp.Maximize(cp.sum(cp.multiply(c,x))), constraints)
prob.solve()

print("The maximum weight is", prob.value)
print("The edge matrix is",x.value)

