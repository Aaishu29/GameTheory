import cvxpy as cp
import numpy as np
big=50
#the utilities of player 1
player1 = np.array([[4,1,4],
                    [2,2,3],
                    [0,4,4]])
#utilites of player 2
player2 = np.array([[0,2,0],
                    [4,4,5],
                    [1,0,0]])

#probability distribution for selcting a strateggy profile
probi = cp.Variable((2,3), nonneg=True)
#Binary matrix that stores whether the strategy profile has been selected or not
Bs = cp.Variable((2,3), boolean=True)
#Best responses of both the players(the nash equilibrium)
u = cp.Variable((2,1))

constraints=[]
for i in range(0,2):
    sum=0
    for j in range(0,3):
        #Psi<=Bsi probability can be maximum 1 and minimum 0. When bsi=0, then psi=0 when bsi=1, then 0<psi<1
        constraints+=[probi[i][j]<=Bs[i][j]]
        sum+=probi[i][j]
    #sum of probabilties should be 1
    constraints+=[sum==1]

for i in range(0,3):
    sum1=0
    sum2=0
    for j in range(0,3):
       sum1+=probi[1][j]*player1[i][j]
       sum2+=probi[0][j]*player2[j][i]
    #sum of probabilites*player's utility should be less than or equal to nash equilibrium utility
    constraints+=[sum1<=u[0][0]]
    constraints+=[sum2<=u[1][0]]
    #Ui-Usi<=BIG(1-Bsi)
    constraints+=[(u[0][0]-sum1)<=big*(1-Bs[0][i])]
    constraints+=[(u[1][0]-sum2)<=big*(1-Bs[1][i])]

prob = cp.Problem(cp.Maximize(cp.sum(Bs)), constraints)
prob.solve()

print("Probability Distribution is",probi.value)
print("The binary x is",Bs.value)
print("The nash utilities are", u.value)

