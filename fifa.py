import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb
#importing the dataset
fifa=pd.read_csv("players_16.csv")
'''print(fifa)'''
#extracting top 5 records of dataset
fifahead=fifa.head()
'''print(fifahead)'''
#finding the frequency of no.of players w.r.t their nationalities
nation=fifa['nationality'].value_counts()
'''print(nation)'''
#top 10 countries from where most players are coming
top10=nation[0:10]
'''print(top10)'''
#finding out the names of all columns in a dataset
'''for i in fifa.columns:
    print(i)'''
#bar plot between top10 countries and no. of players coming from those countries
x=top10.keys()
y=top10
'''plt.bar(x,y)
plt.show()'''
#extracting the short name column and wage_eur column from dataset
salary=fifa[['short_name','wage_eur']]
'''print(salary)'''
#top 10 max salary getters
top10sal=salary.sort_values(by=['wage_eur'],ascending=False)[0:10]
'''print(top10sal)'''
#bar plot between top10 players with max salaries
x2=top10sal['short_name']
y2=top10sal['wage_eur']
'''plt.bar(x2,y2)
plt.show()'''
#extracting the records of players belonging to germany
germany=fifa[fifa['nationality']=='Germany']
'''print(germany)'''
#head of germany
gerhead=germany.head()
'''print('gerhead')'''
#top 10 height players of germany nation
height=germany[['short_name','height_cm']]
'''print(height)'''
top10height=height.sort_values(by=['height_cm'],ascending=False)[0:10]
'''print(top10height)'''
#extracting the records of top 10 weighed germany players
top10wt=germany.sort_values(by=['weight_kg'],ascending=False)[0:10]
'''print(top10wt)'''
#top 10 salary earning germany players
top10salger=germany.sort_values(by=['wage_eur'],ascending=False)[0:10]
'''print(top10salger)
print(top10salger[['short_name','wage_eur']])'''
#shooting(i.e;players scoring goals by shoot)#top 10 players who has more shooting points
shoot=fifa[['short_name','shooting']].sort_values(by=['shooting'],ascending=False)[0:10]
'''print(shoot)'''
#defending(top 10 players scored more defending points)
defend=fifa[['short_name','defending','nationality','club']]
'''print(defend.sort_values(by=['defending'],ascending=False)[0:10])'''
#extracting the records of players belonging to  Real Madrid club
madrid=fifa[fifa['club']=='Real Madrid']
print(madrid)
#top 10 earners from real madrid club
print(madrid.sort_values(by=['wage_eur'],ascending=False)[0:10])
#top 10 players with high shooting points from real madrid club
print(madrid.sort_values(by=['shooting'],ascending=False)[0:10])
#top 10 players with high defending points from real madrid club
print(madrid.sort_values(by=['defending'],ascending=False)[0:10])
#nationality of players from real madrid club
print(madrid['nationality'].value_counts())

