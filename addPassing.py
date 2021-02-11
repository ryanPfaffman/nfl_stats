import requests
import select
from bs4 import BeautifulSoup as soup
from stats_qb import qb_stats_real

passing_url = "https://www.espn.com/nfl/stats/player/_/season/2020/seasontype/3/table/passing/sort/passingYards/dir/desc"
passing_page = requests.get(passing_url)
soup = soup(passing_page.text, 'html.parser')

td_s = soup.find_all('td')
td_s_p = '\n'.join((el.get_text()) for el in td_s)

list = td_s_p.split('\n')

listL = len(list)

def getQB(s):
    rtnS = ""
    sL = len(s)

    for x in range(sL):
        if x != sL - 1:
            if s[x].isupper() and s[x + 1].isupper():
                pass
            else:
                rtnS += s[x]
    return rtnS

indexLChanged = False
x = 0

while x < listL:
    if x != listL - 1:
        if list[x].isnumeric() and (list[x + 1].isnumeric() == False and "." not in list[x + 1]):
            list.pop(x)
            listL -= 1
        elif list[x] == "QB":
            list.pop(x)
            listL -= 1
        elif list[x].isnumeric() and list[x + 1].isnumeric() and indexLChanged == False:
            indexL = x - 1
            indexLChanged = True
        if len(list[x]) > 6:
            list[x] = getQB(list[x])
    x += 1

qb_list = list[:indexL]
stats_list = list[indexL:]

stats_listL = len(stats_list)

x = 0
z = 1

stats_list_new = []

z = 1
for x in range(len(stats_list)):
    if z == 1:
        pass
    elif z == 14:
        pass
    elif z == 7:
        pass
    elif z == 6:
        pass
    elif z == 4:
        pass
    else:
        stats_list_new.append(stats_list[x])
    if z == 14:
        z = 0
    z += 1

stats_list = stats_list_new

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

qb_cleaned_list = []

for x in qb_list:
    if x.isdigit() == False:
        qb_cleaned_list.append(x)

#print(qb_cleaned_list)
qb_stats_add = []
temp_nary = {}

iS = 0
#print(qb_list, stats_list)
#print(stats_list[0])
qb_string = ''
for nary in qb_stats_real:
    qb_string += nary['qb_name']

for x in qb_cleaned_list:
    if x in qb_string:
        temp_nary['qb_name'] = x
        temp_nary['qb_cmp'] = stats_list[iS]
        temp_nary['qb_att'] = stats_list[iS + 1]
        temp_nary['qb_pass_yds'] = stats_list[iS + 2]
        temp_nary['qb_long'] = stats_list[iS + 3]
        temp_nary['qb_td'] = stats_list[iS + 4]
        temp_nary['qb_int'] = stats_list[iS + 5]
        temp_nary['qb_sack'] = stats_list[iS + 6]
        temp_nary['qb_sack_yds'] = stats_list[iS + 7]
        temp_nary['qb_rating'] = stats_list[iS + 8]
        qb_stats_add.append(temp_nary)
        temp_nary = {}
        iS += 9

#print(qb_stats_add)

def findIndex(lst, qbName):
    i = 0
    for x in lst:
        if x['qb_name'] == qbName:
            return i
        i += 1

def getQbRating(att, cmp, passYds, td, int):
    formula1 = ((cmp / att) - .3) * 5
    formula2 = ((passYds / att) - 3) * .25
    formula3 = ((td) / att) * 20
    formula4 = 2.375 - ((int / att)) * 25

    return round(((formula1 + formula2 + formula3 + formula4) / 6) * 100, 1)

def addStats(lstToAdd, lstToChange, qbName):
    i = findIndex(lstToAdd, qbName)
    c = findIndex(lstToChange, qbName)

    nary1 = lstToAdd[i]

    lstToChange[c]['qb_cmp'] += nary1['qb_cmp']
    thisNaryCmp = lstToChange[c]['qb_cmp']
    lstToChange[c]['qb_att'] += nary1['qb_att']
    thisNaryAtt = lstToChange[c]['qb_att']
    lstToChange[c]['qb_cmp_perc'] = thisNaryCmp / thisNaryAtt
    lstToChange[c]['qb_pass_yds'] += nary1['qb_pass_yds']
    thisNaryPassYds = lstToChange[c]['qb_pass_yds']
    lstToChange[c]['qb_yds_att'] = round(lstToChange[c]['qb_pass_yds'] / thisNaryAtt, 1)
    if lstToChange[c]['qb_long'] < nary1['qb_long']:
        lstToChange[c]['qb_long'] = nary1['qb_long']
    lstToChange[c]['qb_td'] += nary1['qb_td']
    thisNaryTd = lstToChange[c]['qb_td']
    lstToChange[c]['qb_int'] += nary1['qb_int']
    thisNaryInt = lstToChange[c]['qb_int']
    lstToChange[c]['qb_sack'] += nary1['qb_sack']
    lstToChange[c]['qb_sack_yds'] += nary1['qb_sack_yds']
    lstToChange[c]['qb_1st'] = lstToChange[c]['qb_1st']
    lstToChange[c]['qb_1st_perc'] = lstToChange[c]['qb_1st_perc']
    lstToChange[c]['qb_20+'] = lstToChange[c]['qb_20+']
    lstToChange[c]['qb_40+'] = lstToChange[c]['qb_40+']

    lstToChange[c]['qb_rating'] = getQbRating(thisNaryAtt, thisNaryCmp, thisNaryPassYds, thisNaryTd, thisNaryInt)

    return lstToChange

qb_real_qb_lst = []

for nary in qb_stats_real:
    qb_real_qb_lst.append(nary['qb_name'])

for qb in qb_list:
    if qb in qb_real_qb_lst:
        qb_stats_real = addStats(qb_stats_add, qb_stats_real, qb)
