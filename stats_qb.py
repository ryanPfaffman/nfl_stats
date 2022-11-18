import requests
import pandas as pd
import select
from bs4 import BeautifulSoup as soup

import string
letters = list(string.ascii_lowercase)

pass_url = 'https://www.nfl.com/stats/player-stats'
pass_page = requests.get(pass_url)
soup = soup(pass_page.text, 'html.parser')

#qbs
qbs = soup.find_all('td')

qbs = "\n".join((el.get_text().strip()) for el in qbs)


def is_decimal(string):
    char = '.'
    if char in string and string.replace('.','').isdigit():
        return True
    else:
        return False

passing_list_1 = qbs.split('\n')

passing_list_2 = []

for x in passing_list_1:
    if x.isdigit():
        passing_list_2.append(int(x))
    elif is_decimal(x):
        passing_list_2.append(float(x))
    else:
        passing_list_2.append(x)

temp_nary = {}

qb_stats_real = []
for x in range(len(passing_list_2)):
    if type(passing_list_2[x]) == str:
        temp_nary['qb_name'] = passing_list_2[x]
        temp_nary['qb_pass_yds'] = passing_list_2[x+1]
        temp_nary['qb_yds_att'] = passing_list_2[x+2]
        temp_nary['qb_att'] = passing_list_2[x+3]
        temp_nary['qb_cmp'] = passing_list_2[x+4]
        #print(f'qb_cmp_perc: {passing_list_2[x+5]}')
        temp_nary['qb_cmp_perc'] = passing_list_2[x+5]
        temp_nary['qb_td'] = passing_list_2[x+6]
        temp_nary['qb_int'] = passing_list_2[x+7]
        temp_nary['qb_rating'] = passing_list_2[x+8]
        temp_nary['qb_1st'] = passing_list_2[x+9]
        #print(f'qb_1st_perc: {passing_list_2[x+10]}')
        temp_nary['qb_1st_perc'] = passing_list_2[x+10]
        temp_nary['qb_20+'] = passing_list_2[x+11]
        temp_nary['qb_40+'] = passing_list_2[x+12]
        temp_nary['qb_long'] = passing_list_2[x+13]
        temp_nary['qb_sack'] = passing_list_2[x+14]
        temp_nary['qb_sack_yds'] = passing_list_2[x+15]
        qb_stats_real.append(temp_nary)
        temp_nary = {}
