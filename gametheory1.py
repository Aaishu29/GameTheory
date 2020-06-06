import math
import matplotlib
platforms = ['facebook', 'instagram', 'youtube', 'linkedIn']
budget1=[0,0,0,0]
budget2=[0,0,0,0]
influence1=[5000,3000,4000,1000]
influence2=[4000,5000,2000,2000]
Budget_1=[]
Budget_2=[]
influence_1=[]
influence_2=[]
profit=0.5
new_entrants=500
total=1000
market1=[]
market2=[]
#facebook
market_share1=influence1[0]/(influence1[0]+influence2[0]+new_entrants)
market_share2=1-market_share1
market1.append(market_share1)
market2.append(market_share2)
a11=math.sqrt(profit*(1+budget2[0]-market_share1)) - 1 - budget2[0]
a21=math.sqrt(profit*(1+budget1[0]-market_share2)) - 1 - budget1[0]
x11 = (market_share1+a11)/(1+a11+a21)
x21 = (market_share2+a21)/(1+a11+a21)



#instagram
market_share1=influence1[1]/(influence1[1]+influence2[1]+new_entrants)
market_share2=1-market_share1
market1.append(market_share1)
market2.append(market_share2)
a12=math.sqrt(profit*(1+budget2[1]-market_share1)) - 1 - budget2[1]
a22=math.sqrt(profit*(1+budget1[1]-market_share2)) - 1 - budget1[1]
x12 = (market_share1+a12)/(1+a12+a22)
x22 = (market_share2+a22)/(1+a12+a22)

#youtube
market_share1=influence1[2]/(influence1[2]+influence2[2]+new_entrants)
market_share2=1-market_share1
market1.append(market_share1)
market2.append(market_share2)
a13=math.sqrt(profit*(1+budget2[2]-market_share1)) - 1 - budget2[2]
a23=math.sqrt(profit*(1+budget1[2]-market_share2)) - 1 - budget1[2]
x13 = (market_share1+a13)/(1+a13+a23)
x23 = (market_share2+a23)/(1+a13+a23)

#linkedin
market_share1=influence1[3]/(influence1[3]+influence2[3]+new_entrants)
market_share2=1-market_share1
market1.append(market_share1)
market2.append(market_share2)
a14=math.sqrt(profit*(1+budget2[3]-market_share1)) - 1 - budget2[3]
a24=math.sqrt(profit*(1+budget1[3]-market_share2)) - 1 - budget1[3]
x14 = (market_share1+a14)/(1+a14+a24)
x24 = (market_share2+a24)/(1+a14+a24)

Budget_1=[a11,a12,a13,a14]
Budget_2=[a21,a22,a23,a24]
influence_1=[x11,x12,x13,x14]
influence_2=[x21,x22,x23,x24]

x1=1000/sum(Budget_1)
x2=1000/sum(Budget_2)

print(market1)
print(market2)
