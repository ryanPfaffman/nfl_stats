import requests
import pandas as pd
import select
from bs4 import BeautifulSoup as soup

defense_url = 'https://www.espn.com/nfl/stats/team/_/view/defense'
defense_page = requests.get(defense_url)
soup = soup(defense_page.text, 'html.parser')

td_s = soup.find_all('td')
td_s_p = '\n'.join((el.get_text()) for el in td_s)

list_1 = td_s_p.split('\n')
teams_list = list_1[0:32]

stats_list = list_1[32:]

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

def_stats_real = []
temp_nary = {}
index_t = 0
index_s = 0

for x in teams_list:
    temp_nary['team'] = x
    temp_nary['gp'] = stats_list[int(index_s)]
    temp_nary['yds'] = stats_list[index_s + 1]
    temp_nary['yds/g'] = stats_list[index_s + 2]
    temp_nary['pass_yds'] = stats_list[index_s + 3]
    temp_nary['pass_yds/g'] = stats_list[index_s + 4]
    temp_nary['rush_yds'] = stats_list[index_s + 5]
    temp_nary['rush_yds/g'] = stats_list[index_s + 6]
    temp_nary['points'] = stats_list[index_s + 7]
    temp_nary['pts/g'] = stats_list[index_s + 8]
    def_stats_real.append(temp_nary)
    temp_nary = {}
    index_t += 1
    index_s += 9
