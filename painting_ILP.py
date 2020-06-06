import cvxpy as cp
import numpy as np
import random
from scipy import misc
from skimage import data
import matplotlib.pyplot as plt
import matplotlib as plot
from skimage.transform import resize       #Change made here from previous code

f= data.camera()
resize_1= resize(f,(256,256))    #Change made here from previous code


plt.imshow(resize_1,cmap='gray')  #Change made here from previous code
plt.show()
x=resize_1[33:97,81:145]   #Change made here from previous code

plt.imshow(x,cmap='gray')
plt.show()
c=x
print(c)
#random_matrix = numpy.random.randint(min_val,max_val,(<num_rows>,<num_cols>))
rho = np.random.randint(0,2,(64,64))
#rho = cp.Variable((64,64), integer=True)
# z=[0,1]
# for i in range(0,64):
#     for j in range(0,64):
#         rho[i][j] = random.choice(z)
print(rho)
n=64
c_transformed = np.multiply(c,rho)
plt.imshow(c_transformed,cmap='gray')
plt.show()
print(c_transformed)
x1 = cp.Variable((64,64))
x2 = cp.Variable((64,64))
constraints =[]

for i in range(0,64):
    for j in range(0,64):
        if rho[i][j]==1:
            constraints+=[x1[i][j]==c_transformed[i][j]]
ft=0

for i in range(2,n):
    for j in range(2,n):
        ft +=(cp.abs(x1[i][j]-x1[i-1][j]))**2 + (cp.abs(x1[i][j]-x1[i][j-1]))**2
prob1 = cp.Problem(cp.Minimize(ft), constraints)
prob1.solve()
print(x1.value)

plt.imshow(x1.value, cmap='gray')
plt.show()
constraints=[]
for i in range(0,64):
    for j in range(0,64):
        if rho[i][j]==1:
            constraints+=[x2[i][j]==c_transformed[i][j]]
fa=0

for i in range(2,n):
    for j in range(2,n):
        fa +=  cp.abs(x2[i][j]-x2[i-1][j])+cp.abs(x2[i][j]-x2[i][j-1])

prob2 = cp.Problem(cp.Minimize(fa), constraints)
prob2.solve()
print(x2.value)

plt.imshow(x2.value, cmap='gray')
plt.show()
