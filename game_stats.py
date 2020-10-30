import csv
import random as r
from stats_qb import qb_stats_real, nary_value

#put encoding='utf-8-sig' to get rid of the \ufeff BOM (byte order mark)

def get_new():
    return_l = []
    nary_1 = {}
    count = 0
    num = 0

    for x in range(len(qb_stats_real)):
        if type(qb_stats_real[x]) == str:
            nary_1['Player'] = qb_stats_real[x]
            nary_1['Yards'] = qb_stats_real[x+1]
            nary_1['Yards Per Att'] = qb_stats_real[x+2]
            nary_1['Attempts'] = qb_stats_real[x+3]
            nary_1['Completions'] = qb_stats_real[x+4]
            nary_1['Completion %'] = qb_stats_real[x+5]
            nary_1['TD'] = qb_stats_real[x+6]
            nary_1['INT'] = qb_stats_real[x+7]
            nary_1['QB Rating'] = qb_stats_real[x+8]
            nary_1['First Downs'] = qb_stats_real[x+9]
            nary_1['First Down %'] = qb_stats_real[x+10]
            nary_1['20+'] = qb_stats_real[x+11]
            nary_1['40+'] = qb_stats_real[x+12]
            nary_1['Long'] = qb_stats_real[x+13]
            nary_1['Sacks'] = qb_stats_real[x+14]
            nary_1['Sack Yards'] = qb_stats_real[x+15]
            return_l.append(nary_1)
            nary_1 = {}
        else:
            pass
    return return_l

big_list = get_new()

for nary in big_list:
    for x,y in nary.items():
        if str(y)[-2:] == '.0':
            nary[x] = int(y)

with open('csv/test.csv',encoding='utf-8-sig') as csv_file:
    return_csv = []
    other = []
    test_string = csv.DictReader(csv_file)
    for x in test_string:
        return_csv.append(x)

for nary in return_csv:
    for x,y in nary.items():
        if y.replace('.','',1).isdigit():
            y = float(y)
            nary.update({x:y})
        elif y.isdigit():
            y = int(y)
            nary.update({x:y})
        else:
            pass

for nary in return_csv:
    for x,y in nary.items():
        if str(y)[-2:] == '.0':
            nary.update({x:int(y)})

key_lst = []
for nary in return_csv:
    for x in nary:
        key_lst.append(x)
    break

key_lst_lower = []
for x in key_lst:
    key_lst_lower.append(x.lower())

def return_stat(stat):
    if stat.lower() == 'qb rating':
        return 'QB Rating'
    if len(str(stat)) <= 3:
        return str(stat).upper()
    else:
        return str(stat).title()

def highest(lst,stat):
    check = float('-inf')
    qb_string = ''
    qb_leader = ''
    best_qb = ''
    return_nary = {}

    if stat.lower() not in key_lst_lower:
        check = 'Invalid Entry. Try again.'
        print(check)
        while check == 'Invalid Entry. Try again.':
            count = highest(lst,input("Highest stat: Choose from:(Yards,Yards Per Att,Attempts, Completions,Completion %, TD, INT, QB Rating ,First Downs, First Down %, 20+, 40+	Long, Sacks, Sack Yards"))
            return count
    else:
        for nary in lst:
            for x,y in nary.items():
                if x in key_lst:
                    if x == key_lst[0]:
                        qb_string += y
                    if x.lower() == stat.lower():
                        if float(y) > check:
                            check = float(y)
                            best_qb = qb_string

            qb_string = ''
        if str(check)[-2:] == '.0':
            check = int(check)

        return_nary['Stat:'] = return_stat(stat)
        return_nary['Leader'] = best_qb
        return_nary[return_stat(stat)] = check

        check = 'Stat: ' + return_stat(stat)  + '\nLeader: ' + best_qb + "\n" + return_stat(stat) + ": " + str(check)
        return return_nary, check

print(highest(big_list,'TD'))

def game_highest(lst,stat):
    check = float('-inf')
    qb_string = ''
    qb_leader = ''
    best_qb = ''
    first_lst = []
    return_lst = []

    for nary in lst:
        for x,y in nary.items():
            if x == 'Player':
                qb_string += y
            elif x == stat:
                first_lst.append({qb_string:y})

        qb_string = ''

def make_question(lst,stat):
    lst_to_pull = []
    lst_to_cut = []
    new_nary = []
    new_lst = []
    qb_names = []
    best_qb_nary = {}

    qb_string = ''
    question = "\nWho is leading?\n" + 'Stat: ' + stat +"\n\nChoices:\n\n"


    lst_to_pull = sorted(lst, key=lambda i:i[stat],reverse=True)
    lst_to_cut = lst_to_pull[:6]

    for nary in lst_to_cut:
        for x,y in nary.items():
            if x == 'Player':
                qb_string = y
            elif x == stat:
                new_lst.append({qb_string:y})
        qb_string = ''

    best_qb_nary = new_lst[0]

    for nary in new_lst:
        for x in nary:
            qb_names.append(x)

    r.shuffle(qb_names)

    for x in qb_names:
        question += '\n' + x

    question += '\n\nEnter Answer: '

    return question

#print(make_question(return_l,'TD'))

def play_game(lst,stat):
    lst_to_pull = []
    lst_to_cut = []
    new_nary = []
    new_list = []
    user_answer = ''
    qb_string = ''
    best_qb_nary = {}
    answer = ''

    lst_to_pull = sorted(lst, key=lambda i:i[stat],reverse=True)
    lst_to_cut = lst_to_pull[:6]
    for nary in lst_to_cut:
        for x,y in nary.items():
            if x == 'Player':
                qb_string = y
            elif x == stat:
                new_list.append({qb_string:y})
        qb_string = ''

    best_qb_nary = new_list[0]

    for x in best_qb_nary:
        answer += x

    user_answer = input(make_question(lst,stat))

    for x,y in best_qb_nary.items():
        answer = x

    if user_answer.lower() == answer.lower():
        msg_1 = input('\n\nCorrect. Would you like to continute playing? (Y/N)')
        if msg_1.lower() == 'y':
            msg = play_game(lst,input("\nChoose a stat:\nChoose from:(Yards,Yards Per Att,Attempts, Completions,Completion %, TD, INT, QB Rating ,First Downs, First Down %, 20+, 40+	Long, Sacks, Sack Yards"))
        else:
            msg = 'Thanks for playing.'
        return msg
    else:
        msg = '\n\nIncorrect. Try again:'
        print(msg.upper())
        while msg == '\n\nIncorrect. Try again:':
            msg = play_game(lst,stat)
            return msg

#print(game_highest(return_l,'Yards'))
print(play_game(big_list,input("\nChoose a stat:\nChoose from:(Yards,Yards Per Att,Attempts, Completions,Completion %, TD, INT, QB Rating ,First Downs, First Down %, 20+, 40+	Long, Sacks, Sack Yards")))

#print(highest(return_l,input("Highest stat: Choose from:(Yards,Yards Per Att,Attempts, Completions,Completion %, TD, INT, QB Rating ,First Downs, First Down %, 20+, 40+	Long, Sacks, Sack Yards")))
