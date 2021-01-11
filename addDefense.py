import requests
import pandas as pd
import select
from bs4 import BeautifulSoup as soup
from stats_defense import def_stats_real

defense_url = "https://www.espn.com/nfl/stats/team/_/view/defense/table/passing/sort/netYardsPerGame/dir/asc"
defense_page = requests.get(defense_url)
soup = soup(defense_page.text, 'html.parser')

td_s = soup.find_all('td')
td_s_p = '\n'.join((el.get_text()) for el in td_s)

list = td_s_p.split('\n')

for x in range(len(list)):
    if list[x].isnumeric():
        indexL = x
        break

teams_list = list[:indexL]
stats_list = list[indexL:]

def is_decimal(string):
    if string.replace('.','').isdigit():
        return True
    else:
        return False

for x in range(len(stats_list)):
    if stats_list[x].replace(',','').isdigit():
        stats_list[x] = int(stats_list[x].replace(',',''))
    elif is_decimal(stats_list[x]):
        stats_list[x] = float(stats_list[x])
    else:
        pass

def_stats_add = []
temp_nary = {}

for x in range(len(stats_list)):
    if type(stats_list[x]) == int or type(stats_list[x]) == float:
        index_s = x
        break

for x in teams_list:
    temp_nary['team'] = x
    temp_nary['gp'] = stats_list[index_s]
    temp_nary['yds'] = stats_list[index_s + 1]
    temp_nary['yds/g'] = stats_list[index_s + 2]
    temp_nary['pass_yds'] = stats_list[index_s + 3]
    temp_nary['pass_yds/g'] = stats_list[index_s + 4]
    temp_nary['rush_yds'] = stats_list[index_s + 5]
    temp_nary['rush_yds/g'] = stats_list[index_s + 6]
    temp_nary['points'] = stats_list[index_s + 7]
    temp_nary['pts/g'] = stats_list[index_s + 8]
    def_stats_add.append(temp_nary)
    temp_nary = {}
    index_s += 9

def findIndex(lst, teamName):
    i = 0
    for x in lst:
        if x['team'] == teamName:
            return i
        i += 1

def addStats(lstA, lstToChange, teamName):
    i = findIndex(lstA, teamName)
    z = findIndex(lstToChange, teamName)
    nary1 = lstA[i]
    nary2 = lstToChange[z]

    lstToChange[z]['gp'] += nary1['gp']
    gp = lstToChange[z]['gp']
    lstToChange[z]['yds'] += nary1['yds']
    lstToChange[z]['yds/g'] = round(lstToChange[z]['yds'] / gp, 1)
    lstToChange[z]['pass_yds'] += nary1['pass_yds']
    lstToChange[z]['pass_yds/g'] = round(lstToChange[z]['pass_yds'] / gp, 1)
    lstToChange[z]['rush_yds'] += nary1['rush_yds']
    lstToChange[z]['rush_yds/g'] = round(lstToChange[z]['rush_yds'] / gp, 1)
    lstToChange[z]['points'] += nary1['points']
    lstToChange[z]['pts/g'] = round(lstToChange[z]['points'] / gp, 1)

    return lstToChange

for x in def_stats_add:
    def_stats_real = addStats(def_stats_add, def_stats_real, x['team'])
