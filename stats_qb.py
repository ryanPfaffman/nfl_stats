import requests
import pandas as pd
import select
from bs4 import BeautifulSoup as soup

import string
letters = list(string.ascii_lowercase)

pass_url = 'https://www.nfl.com/stats/player-stats/'
pass_page = requests.get(pass_url)
soup = soup(pass_page.text, 'html.parser')

#qbs
qbs = soup.find_all('a', {'class':'d3-o-player-fullname'})

qbs = "\n".join((el.get_text()) for el in qbs)

qbs_lst = []
qbs_lst = qbs.split('\n')
qbs_lst_1 = []
for x in qbs_lst:
    if x != '':
        qbs_lst_1.append(x.strip())
for x in qbs_lst_1:
    if x == '':
        qbs_lst_1.remove(x)

characters = [' ',',']
space = [' ']

#pass yards
pass_yds = soup.find_all('td', attrs = {'class': 'selected'})
pass_yds = str(pass_yds)
new_pass_yds = ''
new_pass_yds_2 = ''

for x in pass_yds:
    if x.isdigit() or x in characters:
        new_pass_yds += x
for x in new_pass_yds:
    if x not in space:
        new_pass_yds_2 += x

pass_yds_lst = new_pass_yds_2.split(',')

both = list(zip(qbs_lst_1,pass_yds_lst))

check = float('-inf')
top_5 = []
for x,y in both:
    y = int(y)
    if y > check:
        check = y
        best_qb = x

first_td = soup.find_all('td')
first_td = "\n".join((x.get_text()) for x in first_td)
first_td = str(first_td)
stats_list_1 = []
stats_list_1 = first_td.split('\n')
qb_names = []
stats = []

stats_list_2 = []
for x in stats_list_1:
    stats_list_2.append(x.strip())

for x in stats_list_2:
    if x == '':
        stats_list_2.remove(x)

for x in stats_list_2:
    if x in qbs_lst_1:
        pass
    elif x not in qbs_lst_1:
        stats.append(x)
    else:
        pass

stats_clean = []
for x in stats:
    if x != '':
        stats_clean.append(float(x))

qb_stats = []
count = 0
for x in range(len(stats_clean)):
    for y in qbs_lst_1:
        while count < len(stats_clean):
            qb_stats.append(y)
            qb_stats.append(stats_clean[count:count + 15 % len(stats_clean)])
            count += 15
            break

qb_stats = str(qb_stats)

qb_stats_2 = qb_stats.split(',')

qb_stats_2 =  str(qb_stats_2)

qb_char = ['[',']','"',"'"]

qb_clean = ''

for x in qb_stats_2:
    if x not in qb_char:
        qb_clean += x

list_qb_stats = []
qb_stat_lst = qb_clean.split(',')
for x in qb_stat_lst:
    list_qb_stats.append(x.strip())

list_qb_stats_new = []

for x in list_qb_stats:
    if x not in qbs_lst_1:
        list_qb_stats_new.append(float(x))
    else:
        list_qb_stats_new.append(x)

qb_stats_real = list_qb_stats_new

def nary_value(lst, offset = 1):
    new_nary = {}
    for x in range(len(lst)):
        if type(lst[x]) == str:
            key = lst[x]
            new_nary.update({key: lst[x + offset % len(lst)]})

    return new_nary

def return_lowest(nary):
    best_qb = ''
    check = float('inf')
    return_nary = {}
    for key,value in nary.items():
        if value < check:
            best_qb = key
            check = value
    return_nary.update({best_qb: check})
    return return_nary

def return_highest(nary):
    best_qb = ''
    check = float('-inf')
    return_nary = {}
    for key,value in nary.items():
        if value > check:
            best_qb = key
            check = value
    return_nary.update({best_qb: check})
    return return_nary

def divide(nary_1, nary_2):
    return_nary = {}
    nary_1_lst = []
    nary_2_lst = []
    qb_lst = []
    return_values = []
    if len(nary_1) == len(nary_2):
        for value in nary_1.values():
            nary_1_lst.append(value)
        for y in nary_2.values():
            nary_2_lst.append(y)
        for x in nary_1.keys():
            qb_lst.append(x)

        for x in range(len(nary_2)):
            return_nary.update({qb_lst[x]: round(nary_1_lst[x] / nary_2_lst[x],2)})

        return return_nary

qb_pass_yds = nary_value(qb_stats_real, 1)
qb_yds_att = nary_value(qb_stats_real, 2)
qb_num_att = nary_value(qb_stats_real, 3)
qb_comp = nary_value(qb_stats_real, 4)
qb_comp_perc = nary_value(qb_stats_real, 5)
qb_td = nary_value(qb_stats_real, 6)
qb_int = nary_value(qb_stats_real, 7)
qb_rating = nary_value(qb_stats_real, 8)
qb_first_downs = nary_value(qb_stats_real, 9)
qb_first_down_perc = nary_value(qb_stats_real, 10)
qb_more_20 = nary_value(qb_stats_real, 11)
qb_more_40 = nary_value(qb_stats_real, 12)
qb_long = nary_value(qb_stats_real, 13)
qb_sacks = nary_value(qb_stats_real, 14)
qb_sacks_yds = nary_value(qb_stats_real, 15)
yrd_per_sack = divide(qb_sacks_yds,qb_sacks)

def create_qb(lst, clas):
    for x in range(len(lst)):
        if type(lst[x]) == str:
            clas.objects.create(name=lst[x],pass_yds=lst[x+1],yds_att=lst[x+2],att=lst[x+3],cmp=lst[x+4],cmp_perc=lst[x+5],td=lst[x+6],int=lst[x+7],qb_rating=lst[x+8],first=lst[x+9],first_perc = lst[x+10],more_20 = lst[x+11],more_40=lst[x+12],lng=lst[x+13],sack = lst[x+14], sack_Y=lst[x+15])
