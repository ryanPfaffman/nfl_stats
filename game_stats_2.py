from stats.views import def_stats_real

def get_names_qb(lst, stat):
    lst_to_pull = sorted(lst, key=lambda i:i[stat],reverse=True)

    top_five = lst_to_pull[:5]

    top_five_names = []

    for x in top_five:
        top_five_names.append(x['qb_name'])

    return top_five_names

def get_names_rb(lst, stat):
    lst_to_pull = sorted(lst, key=lambda i:i[stat],reverse=True)

    top_five = lst_to_pull[:5]

    top_five_names = []

    for x in top_five:
        top_five_names.append(x['name'])

    return top_five_names

def get_stat_def(lst, stat):
    lst_to_pull = sorted(lst, key=lambda i:i[stat])

    top_five = lst_to_pull[:5]

    top_five_stat = []

    for x in top_five:
        top_five_stat.append(x[stat])

    return top_five_stat

def get_teams_def(lst, stat):
    lst_to_pull = sorted(lst, key=lambda i:i[stat])

    top_five = lst_to_pull[:5]

    top_five_teams = []

    for x in top_five:
        top_five_teams.append(x['team'])

    return top_five_teams

def get_stat(lst, stat):
    lst_to_pull = sorted(lst, key=lambda i:i[stat],reverse=True)

    top_five = lst_to_pull[:5]

    top_five_stat = []

    for x in top_five:
        top_five_stat.append(x[stat])

    return top_five_stat


def get_answers_qb(lst, stat):
    lst_to_pull = sorted(lst, key=lambda i:i[stat],reverse=True)

    top_five = lst_to_pull[:5]
    top_five_stat = []
    nary = {}
    lst_to_check = []

    highest_stat = float('-inf')
    for x in top_five:
        nary['qb_name'] = x['qb_name']
        nary[stat] = x[stat]
        lst_to_check.append(nary)
        if x[stat] > highest_stat:
            highest_stat = x[stat]
        nary = {}

    return_lst = []

    for nary in lst_to_check:
        for x,y in nary.items():
            if y == highest_stat:
                return_lst.append(nary)

    return return_lst

def get_answers_rb(lst, stat):
    lst_to_pull = sorted(lst, key=lambda i:i[stat],reverse=True)

    top_five = lst_to_pull[:5]
    top_five_stat = []
    nary = {}
    lst_to_check = []

    highest_stat = float('-inf')
    for x in top_five:
        nary['name'] = x['name']
        nary[stat] = x[stat]
        lst_to_check.append(nary)
        if x[stat] > highest_stat:
            highest_stat = x[stat]
        nary = {}

    return_lst = []

    for nary in lst_to_check:
        for x,y in nary.items():
            if y == highest_stat:
                return_lst.append(nary)

    return return_lst

def get_answers_def(lst, stat):
    lst_to_pull = sorted(lst, key=lambda i:i[stat])

    top_five = lst_to_pull[:5]
    top_five_stat = []
    nary = {}
    lst_to_check = []

    highest_stat = float('inf')
    for x in top_five:
        nary['team'] = x['team']
        nary[stat] = x[stat]
        lst_to_check.append(nary)
        if x[stat] < highest_stat:
            highest_stat = x[stat]
        nary = {}

    return_lst = []

    for nary in lst_to_check:
        for x,y in nary.items():
            if y == highest_stat:
                return_lst.append(nary)

    return return_lst
