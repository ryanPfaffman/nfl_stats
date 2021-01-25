import requests
import select
from bs4 import BeautifulSoup as soup
from stats_rb import rb_stats_real

passing_url = "https://www.espn.com/nfl/stats/player/_/stat/rushing/table/rushing/sort/rushingYards/dir/desc"
passing_page = requests.get(passing_url)
soup = soup(passing_page.text, 'html.parser')

td_s = soup.find_all('td')
td_s_p = '\n'.join((el.get_text()) for el in td_s)

list = td_s_p.split('\n')

listL = len(list)

def getRb(s):
    rtnS = ''
    spaceYet = False

    for x in range(len(s)):
        if s[x] == ' ':
            spaceYet = True
            z = x

        if spaceYet == True and s[x].isupper() and x > z + 1:
            break

        rtnS += s[x]

    return rtnS

def isDecimal(string):
    if string.replace('.','').isdigit():
        return True
    else:
        return False

rbYet = False

cleanedList = []

for el in list:
    if el == 'RB' and rbYet == False:
        rbYet = True
        indexForCut = len(cleanedList)
    if rbYet == False and el.isdigit():
        pass
    elif el == 'RB' or el == 'QB' or el == 'WR':
        pass
    elif len(el) > 7:
        cleanedList.append(getRb(el))
    elif rbYet == True and el.isdigit():
        cleanedList.append(int(el))
    elif rbYet == True and isDecimal(el):
        cleanedList.append(float(el))
    else:
        cleanedList.append(el)


runnersList = cleanedList[:indexForCut]
statsList1 = cleanedList[indexForCut:]

statsList = []
c = 1

for x in range(len(statsList1)):
    if c == 1:
        pass
    elif c == 4:
        pass
    elif c == 8:
        pass
    elif c == 10:
        pass
    else:
        statsList.append(statsList1[x])

    if c == 11:
        c = 0
    c += 1

statsToAdd = []
tempNary = {}
i = 0

for x in runnersList:
    tempNary['name'] = x
    tempNary['att'] = statsList[i]
    tempNary['rush_yds'] = statsList[i + 1]
    tempNary['long'] = statsList[i + 2]
    tempNary['20+'] = statsList[i + 3]
    tempNary['td'] = statsList[i + 4]
    tempNary['rush fum'] = statsList[i + 5]
    tempNary['rush 1st'] = statsList[i + 6]
    statsToAdd.append(tempNary)
    tempNary = {}
    i += 7

def getIndex(lst, name):
    c = 0

    for x in lst:
        if x['name'] == name:
            return c

        c += 1

    return -1

def addStats(listA, listZ, name):
    i = getIndex(listA, name)
    z = getIndex(listZ, name)
    curNary = listA[i]
    listZ[z]['att'] += curNary['att']
    listZ[z]['rush_yds'] += curNary['rush_yds']
    if curNary['long'] > listZ[z]['long']:
        listZ[z]['long'] += curNary['long']
    listZ[z]['20+'] += curNary['20+']
    listZ[z]['td'] += curNary['td']
    listZ[z]['rush fum'] += curNary['rush fum']
    listZ[z]['rush 1st'] += curNary['rush 1st']

    return listZ

runnersToAdd = []

for nary in rb_stats_real:
    runnersToAdd.append(nary['name'])

for nary in statsToAdd:
    if nary['name'] in runnersToAdd:
        rb_stats_real = addStats(statsToAdd, rb_stats_real, nary['name'])
print(rb_stats_real)
