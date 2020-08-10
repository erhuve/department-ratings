import requests
import json
import math
import csv
import pandas as pd
import plotly.express as px
import plotly.io as pio
###Commented code is for writing to JSON or writing to CSV

SCHOOL_ID = 675 ###NYU, find your school id by searching on ratemyprofessors

page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(SCHOOL_ID))
jsonpage = json.loads(page.content)
num = jsonpage['remaining'] + 20
amt = math.ceil(num / 20)
#data = [{'name': 'Dylan, Bob', 'rating': '5', 'rating_class': 'good', 'tNumRatings': 46} for i in range(num + 1)]
j = 0

csv_file = open('data.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['tDept', 'tNumRatings', 'overall_rating'])

for i in range(1, amt + 1):
    newpage = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=" + str(i) + "&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(SCHOOL_ID))
    newjson = json.loads(newpage.content)   
    temp = newjson['professors']
    profs = []
    profs.extend(temp)

    k = 0
    for x in range(1, len(profs) + 1):
        # data[x + j]['name'] = profs[k]['tLname'] + ', ' + profs[k]['tFname']
        # data[x + j]['rating'] = profs[k]['overall_rating']
        # data[x + j]['rating_class'] = profs[k]['rating_class']
        # data[x + j]['tNumRatings'] = profs[k]['tNumRatings']
        csv_writer.writerow([profs[k]['tDept'], profs[k]['tNumRatings'], profs[k]['overall_rating']])
        k += 1
    #j += 20
csv_file.close()
# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile)

csv_file = open('depts.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Department','# of Ratings','Overall Rating','Effective Rating'])

df = pd.read_csv('data.csv')
pphaha = df.groupby('tDept')
gk = pphaha.mean()
lp = pphaha.sum()
k = pphaha.groups.keys()

sum1 = lp['tNumRatings'].values
mean1 = gk['overall_rating'].values

# print(sum1)
# print(sum1)

# gk.to_csv('mean.csv', index = False)
# lp.to_csv('sum.csv', index = False)

x = 0
for i in k:
    csv_writer.writerow([i, sum1.item(x), mean1.item(x), (mean1.item(x) * sum1.item(x) + 6) / (sum1.item(x) + 2)])
    x += 1
    
csv_file.close()    
dtf = pd.read_csv('depts.csv')
result = dtf.sort_values(by=['Overall Rating', '# of Ratings'], ascending = False)
result = result.fillna(0)
result.to_csv('depts.csv', index = False)


df = pd.read_csv('depts.csv')

fig = px.scatter(df, x = '# of Ratings', y = 'Effective Rating', size = 'Effective Rating', color = 'Department', hover_name = 'Department', hover_data=['Overall Rating'], log_x = True, size_max = 50)

pio.write_html(fig, file = 'index.html', auto_open = True)