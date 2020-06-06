import csv
import math
facebook_budget_1=[]
instagram_budget_1=[]
youtube_budget_1=[]
linkedin_budget_1=[]
facebook_budget_2=[]
instagram_budget_2=[]
youtube_budget_2=[]
linkedin_budget_2=[]
facebook_views_1 = []
instagram_views_1 = []
youtube_views_1 =[]
linkedin_views_1 = []
facebook_views_2 = []
instagram_views_2 = []
youtube_views_2 =[]
linkedin_views_2 = []
stage_num = []
with open('abc.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        #print(row[1])
        stage_num.append(row[0])
        facebook_budget_1.append(row[1])
        facebook_views_1.append(row[2])
        instagram_budget_1.append(row[3])
        instagram_views_1.append(row[4])
        youtube_budget_1.append(row[5])
        youtube_views_1.append(row[6])
        linkedin_budget_1.append(row[7])
        linkedin_views_1.append(row[8])
        facebook_budget_2.append(row[9])
        facebook_views_2.append(row[10])
        instagram_budget_2.append(row[11])
        instagram_views_2.append(row[12])
        youtube_budget_2.append(row[13])
        youtube_views_2.append(row[14])
        linkedin_budget_2.append(row[15])
        linkedin_views_2.append(row[16])
    csvFile.close()
fb_new_1 = [int(facebook_views_1[3])]
ins_new_1 =[int(instagram_views_1[3])]
youtube_new_1 = [int(youtube_views_1[3])]
linkedin_new_1 = [int(linkedin_views_1[3])]
fb_new_2 = [int(facebook_views_2[3])]
ins_new_2 =[int(instagram_views_2[3])]
youtube_new_2 = [int(youtube_views_2[3])]
linkedin_new_2 = [int(linkedin_views_2[3])]
l = len(facebook_views_1)
for i in range (3,l-1):
    #print(fb_new_1[i-3])
    #a = int(facebook_views_1[i+1]) - int(facebook_views_1[i])
    fb_new_1.append(int(facebook_views_1[i+1])-int(facebook_views_1[i]))
    print(fb_new_1[i-3])
    ins_new_1.append(int(instagram_views_1[i+1])-int(instagram_views_1[i]))
    youtube_new_1.append(int(youtube_views_1[i+1])-int(youtube_views_1[i]))
    linkedin_new_1.append(int(linkedin_views_1[i+1])-int(linkedin_views_1[i]))
    fb_new_2.append(int(facebook_views_2[i+1])-int(facebook_views_2[i]))
    ins_new_2.append(int(instagram_views_2[i+1])-int(instagram_views_2[i]))
    youtube_new_2.append(int(youtube_views_2[i+1])-int(youtube_views_2[i]))
    linkedin_new_2.append(int(linkedin_views_2[i+1])-int(linkedin_views_2[i]))
#calculation of average no. of views for both firms
fb = (sum(fb_new_1)+ sum(fb_new_2))/int(stage_num[len(stage_num)-1])
insta = (sum(ins_new_1)+ sum(ins_new_2))/int(stage_num[len(stage_num)-1])
youtube = (sum(youtube_new_1)+ sum(youtube_new_2))/int(stage_num[len(stage_num)-1])
linkedin = (sum(linkedin_new_1)+ sum(linkedin_new_2))/int(stage_num[len(stage_num)-1])
print (fb)
print(insta)
print(youtube)
print(linkedin)
#calculation of average no. of views for firm 1
fb_1 = (sum(fb_new_1))/int(stage_num[len(stage_num)-1])
print("fb1")
print(fb_1)
insta_1 = (sum(ins_new_1))/int(stage_num[len(stage_num)-1])
youtube_1 = (sum(youtube_new_1))/int(stage_num[len(stage_num)-1])
linkedin_1 = (sum(linkedin_new_1))/int(stage_num[len(stage_num)-1])
#calculation of average no. of views for firm 2
fb_2= (sum(fb_new_2))/int(stage_num[len(stage_num)-1])
insta_2 = (sum(ins_new_2))/int(stage_num[len(stage_num)-1])
youtube_2 = (sum(youtube_new_2))/int(stage_num[len(stage_num)-1])
linkedin_2 = (sum(linkedin_new_2))/int(stage_num[len(stage_num)-1])
p = input("what is the profit per view? ")
prof = int(p)
#budget ratios of firm 1
fb_b_1 = (fb-fb_1)*(math.log(prof*fb/(fb-fb_1)))
#print(fb_b_1)
insta_b_1 = (insta-insta_1)*(math.log(prof*insta/(insta-insta_1)))
youtube_b_1 = (youtube- youtube_1)*(math.log(prof*youtube/(youtube-youtube_1)))
linkedin_b_1 = (linkedin - linkedin_1)*(math.log(prof*linkedin/(linkedin-linkedin_1)))

#total budget to be invested by firm 1
B = input("What is the total budget you want to invest? ")

#budget distribution array for firm
sum = fb_b_1 + insta_b_1 + youtube_b_1 + linkedin_b_1
x = int(B)/sum
fb_b1 = fb_b_1*x
in_b1 = insta_b_1*x
yt_b1 =  youtube_b_1*x
ln_b1 = linkedin_b_1*x
print("firm1 investment")
print('facebook {0}'.format(fb_b1))
print('instagram {0}'.format(in_b1))
print('youtube {0}'.format(yt_b1))
print('linkedin {0}' .format(ln_b1))

#budget ratios of firm 2
fb_b_2 = (fb-fb_2)*(math.log(prof*fb/(fb-fb_2)))
insta_b_2 = (insta-insta_2)*(math.log(prof*insta/(insta-insta_2)))
youtube_b_2 = (youtube- youtube_2)*(math.log(prof*youtube/(youtube-youtube_2)))
linkedin_b_2 = (linkedin - linkedin_2)*(math.log(prof*linkedin/(linkedin-linkedin_2)))

#total budget to be invested by firm 1
#B = input("What is the total budget you want to invest?")
#budget distribution array for firm
sum1 = fb_b_2 + insta_b_2 + youtube_b_2 + linkedin_b_2
y = int(B)/sum1
fb_b2 = fb_b_2*y
in_b2 = insta_b_2*y
yt_b2 =  youtube_b_2*y
ln_b2 = linkedin_b_2*y
print("firm2 investment")
print('facebook {0}'.format(fb_b2))
print('instagram {0}'.format(in_b2))
print('youtube {0}'.format(yt_b2))
print('linkedin {0}' .format(ln_b2))
