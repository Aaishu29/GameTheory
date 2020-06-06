import cvxpy as cp
import numpy as np
big=50
#utilities of player one
player1 = np.array([[6,2],
                    [7,0]])
#utilities of player two
player2 = np.array([[6,7],
                    [2,0]])
#probabilities of choosing a strategy profile
probi = cp.Variable((2,2), nonneg=True)
#constraints on maximizing the correlated equilibrium
constraints=[]
sum=0
#the sum of all probablities shall be one
for i in range(0,2):
    for j in range(0,2):
        sum+=probi[i][j]
        #each probability shall be non negetive
        constraints+=[probi[i][j]>=0]

#calculates and computes the constraint that p(si)*u(si)-p(si)*t(si)>=0
sum1=0
sum2=0
sum3=0
sum4=0
for j in range(0,2):
    sum1+=(player1[0][j]-player1[1][j])*probi[0][j]
    sum2+=(player1[1][j]-player1[0][j])*probi[1][j]
    sum3+=(player2[j][0]-player2[j][1])*probi[j][0]
    sum4+=(player2[j][1]-player2[j][0])*probi[j][1]
constraints+=[sum1>=0]
constraints+=[sum2>=0]
constraints+=[sum3>=0]
constraints+=[sum4>=0]

#For symmetry, the correlated utility of player1 and player 2 should be equal
constraints+=[cp.sum(cp.multiply(player1,probi))==cp.sum(cp.multiply(player2,probi))]
#probability should sum to one
constraints+=[sum==1]

#maximize the correlated equilibrium utility. Since it is symmetric, therefore maximize anyone would result in similar outcome
prob = cp.Problem(cp.Maximize(cp.sum(cp.multiply(player1,probi))), constraints)
prob.solve()

print("The highest symmetric utility is", prob.value)
print("A probability distribution is",probi.value)
