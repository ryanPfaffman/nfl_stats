import requests
import pandas as pd
import select
from bs4 import BeautifulSoup as soup

import string
letters = list(string.ascii_lowercase)

rush_url = 'https://www.nfl.com/stats/player-stats/category/rushing/2020/REG/all/rushingyards/desc'
rush_page = requests.get(rush_url)
soup = soup(rush_page.text,'html.parser')

rbs = soup.find_all('a', {'class':'d3-o-player-fullname'})

rbs = '\n'.join((el.get_text()) for el in rbs)

rbs_lst = rbs.split('\n')

rbs_lst_1 = []

for x in rbs_lst:
    if x != '':
        rbs_lst_1.append(x.strip())

for x in rbs_lst_1:
    if x == '':
        rbs_lst_1.remove(x)

rb_stats = soup.find_all('td')
rb_stats = '\n'.join((x.get_text()) for x in rb_stats)

rb_stats = str(rb_stats)


rb_stats = rb_stats.split('\n')

new_lst = []

def is_decimal(string):
    test_1 = string
    if test_1.replace('.','').isdigit():
        return True
    else:
        return False


for x in rb_stats:
    if x == '':
        pass
    else:
        new_lst.append(x.strip())

rb_lst = []

for x in new_lst:
    if x == '':
        pass
    elif x.isdigit():
        rb_lst.append(int(x))
    elif is_decimal(x):
        rb_lst.append(float(x))
    else:
        rb_lst.append(x)

def get_nary(lst):
    nary = {}
    rtn_lst = []
    for x in range(len(lst)):
        if type(lst[x]) == str:
            nary['name'] = lst[x]
            nary['rush_yds'] = lst[x+1]
            nary['att'] = lst[x+2]
            nary['td'] = lst[x+3]
            nary['20+'] = lst[x+4]
            nary['40+'] = lst[x+5]
            nary['long'] = lst[x+6]
            nary['rush 1st'] = lst[x+7]
            nary['rush 1st%'] = lst[x+8]
            nary['rush fum'] = lst[x+9]
            rtn_lst.append(nary)
            nary = {}
    return rtn_lst

rb_stats_real = get_nary(rb_lst)
