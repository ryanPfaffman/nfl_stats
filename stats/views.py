from django.shortcuts import render

import random as r

from datetime import datetime, timedelta

from stats_qb import qb_stats_real

from stats_defense import def_stats_real

from stats_rb import rb_stats_real

from game_stats_2 import get_stat, get_names_qb, get_names_rb, get_answers_qb, get_answers_rb, get_answers_def, get_stat_def, get_teams_def

from .models import Qb, Rb, Defense
#start of quiz

Qb.objects.all().delete()
Rb.objects.all().delete()
Defense.objects.all().delete()

#Quarterbacks
qb_stats_list = []

for nary in qb_stats_real:
    for val in nary.values():
        qb_stats_list.append(val)

for x in range(len(qb_stats_list)):
    if type(qb_stats_list[x]) == str:
        a_count = Qb(name=qb_stats_list[x],pass_yds=qb_stats_list[x+1],yds_att=qb_stats_list[x+2],att=qb_stats_list[x+3],cmp=qb_stats_list[x+4],cmp_perc=round(qb_stats_list[x+5] * 100,2),td=qb_stats_list[x+6],int=qb_stats_list[x+7],qb_rating=qb_stats_list[x+8],first=qb_stats_list[x+9],first_perc=round(qb_stats_list[x+10] * 100,2),more_20=qb_stats_list[x+11],more_40=qb_stats_list[x+12],lng=qb_stats_list[x+13],sack=qb_stats_list[x+14],sack_Y=qb_stats_list[x+15])
        a_count.save()

nary = {}
qb_stats_real = []

for x in Qb.objects.all():
    nary['qb_name'] = x.name
    nary['qb_pass_yds'] = x.pass_yds
    nary['qb_yds_att'] = x.yds_att
    nary['qb_att'] = x.att
    nary['qb_cmp'] = x.cmp
    nary['qb_cmp_perc'] = x.cmp_perc
    nary['qb_td'] = x.td
    nary['qb_int'] = x.int
    nary['qb_rating'] = x.qb_rating
    nary['qb_1st'] = x.first
    nary['qb_1st_perc'] = x.first_perc
    nary['qb_20+'] = x.more_20
    nary['qb_40+'] = x.more_40
    nary['qb_long'] = x.lng
    nary['qb_sack'] = x.sack
    nary['qb_sack_yds'] = x.sack_Y
    qb_stats_real.append(nary)
    nary= {}

qb_stats_real = sorted(qb_stats_real, key=lambda i:i["qb_pass_yds"], reverse=True)

qb_names_left = []
qb_stats_lst = []
qb_att_lst = []
qb_num_att_lst = []
qb_comp_lst = []
qb_comp_perc_lst = []
qb_td_lst = []
qb_int_lst = []
qb_rating_lst = []
qb_first_downs_lst = []
qb_first_down_perc_lst = []
qb_more_20_lst = []
qb_more_40_lst = []
qb_long_lst = []
qb_sacks_lst = []
qb_sacks_yds_lst = []

for nary in qb_stats_real:
    for x, y in nary.items():
        if x == 'qb_name' and len(qb_names_left) < 25:
            qb_names_left.append(y)
        elif x == 'qb_pass_yds' and len(qb_stats_lst) < 25:
            qb_stats_lst.append(y)
        elif x == 'qb_yds_att' and len(qb_att_lst) < 25:
            qb_att_lst.append(y)
        elif x == 'qb_att' and len(qb_num_att_lst) < 25:
            qb_num_att_lst.append(y)
        elif x == 'qb_cmp' and len(qb_comp_lst) < 25:
            qb_comp_lst.append(y)
        elif x == 'qb_cmp_perc' and len(qb_comp_perc_lst) < 25:
            qb_comp_perc_lst.append(y)
        elif x == 'qb_td' and len(qb_td_lst) < 25:
            qb_td_lst.append(y)
        elif x == 'qb_int' and len(qb_int_lst) < 25:
            qb_int_lst.append(y)
        elif x == 'qb_rating' and len(qb_rating_lst) < 25:
            qb_rating_lst.append(y)
        elif x == 'qb_1st' and len(qb_first_downs_lst) < 25:
            qb_first_downs_lst.append(y)
        elif x == 'qb_1st_perc' and len(qb_first_down_perc_lst) < 25:
            qb_first_down_perc_lst.append(y)
        elif x == 'qb_20+' and len(qb_more_20_lst) < 25:
            qb_more_20_lst.append(y)
        elif x == 'qb_40+' and len(qb_more_40_lst) < 25:
            qb_more_40_lst.append(y)
        elif x == 'qb_long' and len(qb_long_lst) < 25:
            qb_long_lst.append(y)
        elif x == 'qb_sack' and len(qb_sacks_lst) < 25:
            qb_sacks_lst.append(y)
        elif x == 'qb_sack_yds' and len(qb_sacks_yds_lst) < 25:
            qb_sacks_yds_lst.append(y)

#start of Rb
rb_stats_list = []

for nary in rb_stats_real:
    for val in nary.values():
        rb_stats_list.append(val)

for x in range(len(rb_stats_list)):
    if type(rb_stats_list[x]) == str:
        b_count = Rb(name=rb_stats_list[x], rush_yds=rb_stats_list[x+1], att=rb_stats_list[x+2], rush_yds_att=round(rb_stats_list[x+1]/rb_stats_list[x+2],2),td=rb_stats_list[x+3],twenty=rb_stats_list[x+4], fourty=rb_stats_list[x+5], long=rb_stats_list[x+6], rush_1st=rb_stats_list[x+7], rush_1st_perc=rb_stats_list[x+8], rush_fum=rb_stats_list[x+9])
        b_count.save()

nary = {}
rb_stats_real = []
for rb in Rb.objects.all():
    nary['name'] = rb.name
    nary['rush_yds'] = rb.rush_yds
    nary['rush_yds_att'] = rb.rush_yds_att
    nary['att'] = rb.att
    nary['td'] = rb.td
    nary['20+'] = rb.twenty
    nary['40+'] = rb.fourty
    nary['long'] = rb.long
    nary['rush_1st'] = rb.rush_1st
    nary['rush_1st_perc'] = rb.rush_1st_perc
    nary['rush_fum'] = rb.rush_fum
    rb_stats_real.append(nary)
    nary = {}

rb_stats_real = sorted(rb_stats_real, key=lambda i:i['rush_yds'], reverse=True)

rb_names = []
rb_rush_yds = []
rb_att = []
rb_rush_yds_att = []
rb_td = []
rb_20 = []
rb_40 = []
rb_long = []
rb_rush_1st = []
rb_rush_1st_perc = []
rb_rush_fum = []

for nary in rb_stats_real:
    for x,y in nary.items():
        if x == 'name':
            rb_names.append(y)
        elif x == 'rush_yds':
            rb_rush_yds.append(y)
        elif x == 'att':
            rb_att.append(y)
        elif x == 'rush_yds_att':
            rb_rush_yds_att.append(y)
        elif x == 'td':
            rb_td.append(y)
        elif x == '20+':
            rb_20.append(y)
        elif x == '40+':
            rb_40.append(y)
        elif x == 'long':
            rb_long.append(y)
        elif x == 'rush_1st':
            rb_rush_1st.append(y)
        elif x == 'rush_1st_perc':
            rb_rush_1st_perc.append(y)
        elif x == 'rush_fum':
            rb_rush_fum.append(y)
        else:
            pass

#end of rbs
#start of defense
def_stats_list = []

for nary in def_stats_real:
    for val in nary.values():
        def_stats_list.append(val)

for x in range(len(def_stats_list)):
    if type(def_stats_list[x]) == str:
        c_count = Defense(team=def_stats_list[x],g_p=def_stats_list[x+1],yds=def_stats_list[x+2],yds_g=def_stats_list[x+3],pass_yds=def_stats_list[x+4],pass_yds_g=def_stats_list[x+5],rush_yds=def_stats_list[x+6],rush_yds_g=def_stats_list[x+7],points=def_stats_list[x+8],point_g=def_stats_list[x+9])
        c_count.save()

nary = {}
def_stats_real = []

for defense in Defense.objects.all():
    nary['team'] = defense.team
    nary['g_p'] = defense.g_p
    nary['yds'] = defense.yds
    nary['yds_g'] = defense.yds_g
    nary['pass_yds'] = defense.pass_yds
    nary['pass_yds_g'] = defense.pass_yds_g
    nary['rush_yds'] = defense.rush_yds
    nary['rush_yds_g'] = defense.rush_yds_g
    nary['points'] = defense.points
    nary['points_g'] = defense.point_g
    def_stats_real.append(nary)
    nary = {}

def_stats_real = sorted(def_stats_real, key=lambda i:i['yds'], reverse=True)

team_names_def = []
gp_def = []
yds_def = []
yds_g_def = []
pass_yds_def = []
pass_yds_game_def = []
rush_yds_def = []
rush_yds_g_def = []
points_def = []
points_p_def = []

for nary in def_stats_real:
    for x,y in nary.items():
        if x == 'team':
            team_names_def.append(y)
        elif x == 'g_p':
            gp_def.append(y)
        elif x == 'yds':
            yds_def.append(y)
        elif x == 'yds_g':
            yds_g_def.append(y)
        elif x == 'pass_yds':
            pass_yds_def.append(y)
        elif x == 'pass_yds_g':
            pass_yds_game_def.append(y)
        elif x == 'rush_yds':
            rush_yds_def.append(y)
        elif x == 'rush_yds_g':
            rush_yds_g_def.append(y)
        elif x == 'points':
            points_def.append(y)
        elif x == 'points_g':
            points_p_def.append(y)
        else:
            pass

# Create your views here.
def home_view(request, *args, **kwargs):
    img_list = [{"img": "<img class=\"slideshow\" src=\"{% static 'images/dontaHightower.jpg' %}\"/>", "bar": "Dont'a Hightower - LB"}, {"img": "<img class=\"slideshow\" src=\"{% static 'images/theKING.jpg' %}\"/>", "bar": "Derrick Henry - RB"}, {"img": "<img class=\"slideshow\" src=\"{% static 'images/patrickMahomes.jpg' %}\"/>", "bar": "Patrick Mahomes - QB"}, {"img": "<img class=\"slideshow\" src=\"{% static 'images/calvinRidley.jpg' %}\"/>", "bar": "Calvin Ridley - WR"}, {"img": "<img class=\"slideshow\" src=\"{% static 'images/aaronRodgers.jpeg' %}\"/>", "bar": "Aaron Rodgers - QB}"]

    home_imgs = {
    "img_1": img_list[0]["img"],
    "bar_1": img_list[0]["bar"],
    "img_2": img_list[1]["img"],
    "bar_2": img_list[1]["bar"],
    "img_3": img_list[2]["img"],
    "bar_3": img_list[2]["bar"],
    "img_4": img_list[3]["img"],
    "bar_4": img_list[3]["bar"],
    "img_5": img_list[4]["img"],
    "bar_5": img_list[4]["bar"],
    }
    return render(request, 'index.html', home_imgs)

def quiz_view(request, *args, **kwargs):
    #Quarterbacks

    #qb_pass_yds
    top_five_stat_pass_yds = get_stat(qb_stats_real, 'qb_pass_yds')
    best_qb_pass_yds_stat = top_five_stat_pass_yds[0]

    top_five_qb_pass_yds = get_names_qb(qb_stats_real, 'qb_pass_yds')
    answer_qb_pass_yds = top_five_qb_pass_yds[0]
    r.shuffle(top_five_qb_pass_yds)

    checker_pass_yds = get_answers_qb(qb_stats_real, 'qb_pass_yds')
    if len(checker_pass_yds) > 1:
        answer_pass_yds_string = ''
        for nary in checker_pass_yds:
            for x,y in nary.items():
                if x == 'qb_name':
                    answer_pass_yds_string += y + ', '
        answer_pass_yds_string = answer_pass_yds_string.strip(', ')
    else:
        answer_pass_yds_string = answer_qb_pass_yds

    #qb_pass_yds_att
    top_five_stat_pass_yds_att = get_stat(qb_stats_real, 'qb_yds_att')
    best_qb_yds_att_stat = top_five_stat_pass_yds_att[0]

    top_five_pass_yds_att = get_names_qb(qb_stats_real, 'qb_yds_att')
    answer_pass_yds_att = top_five_pass_yds_att[0]
    r.shuffle(top_five_pass_yds_att)

    checker_pass_yds_att = get_answers_qb(qb_stats_real, 'qb_yds_att')
    if len(checker_pass_yds_att) > 1:
        answer_pass_yds_att_string = ''
        for nary in checker_pass_yds_att:
            for x,y in nary.items():
                if x == 'qb_name':
                    answer_pass_yds_att_string += y + ', '
        answer_pass_yds_att_string = answer_pass_yds_att_string.strip(', ')
    else:
        answer_pass_yds_att_string = answer_pass_yds_att

    #qb_pass_att
    top_five_stat_pass_att = get_stat(qb_stats_real, 'qb_att')
    best_qb_att_stat = top_five_stat_pass_att[0]

    top_five_pass_att = get_names_qb(qb_stats_real, 'qb_att')
    answer_pass_att = top_five_pass_att[0]
    r.shuffle(top_five_pass_yds_att)

    checker_pass_att = get_answers_qb(qb_stats_real, 'qb_att')
    if len(checker_pass_att) > 1:
        answer_pass_att_string = ''
        for nary in checker_pass_att:
            for x,y in nary.items():
                if x == 'qb_name':
                    answer_pass_att_string += y + ', '
        answer_pass_att_string = answer_pass_att_string.strip(', ')
    else:
        answer_pass_att_string = answer_pass_att

    #qb_pass_cmp
    top_five_stat_pass_cmp = get_stat(qb_stats_real, 'qb_cmp')
    best_qb_cmp_stat = top_five_stat_pass_cmp[0]

    top_five_pass_cmp = get_names_qb(qb_stats_real, 'qb_cmp')
    answer_pass_cmp = top_five_pass_cmp[0]
    r.shuffle(top_five_pass_cmp)

    checker_pass_cmp = get_answers_qb(qb_stats_real, 'qb_cmp')
    if len(checker_pass_cmp) > 1:
        answer_pass_cmp_string = ''
        for nary in checker_pass_cmp:
            for x,y in nary.items():
                if x == 'qb_name':
                    answer_pass_cmp_string += y + ', '
        answer_pass_cmp_string = answer_pass_cmp_string.strip(', ')
    else:
        answer_pass_cmp_string = answer_pass_cmp

    #qb_pass_cmp_perc
    top_five_stat_pass_cmp_perc = get_stat(qb_stats_real, 'qb_cmp_perc')
    best_qb_cmp_perc_stat = top_five_stat_pass_cmp_perc[0]

    top_five_pass_cmp_perc = get_names_qb(qb_stats_real, 'qb_cmp_perc')
    answer_pass_cmp_perc= top_five_pass_cmp_perc[0]
    r.shuffle(top_five_pass_cmp_perc)

    checker_pass_cmp_perc = get_answers_qb(qb_stats_real, 'qb_cmp_perc')
    if len(checker_pass_cmp_perc) > 1:
        answer_pass_cmp_perc_string = ''
        for nary in checker_pass_cmp_perc:
            for x,y in nary.items():
                if x == 'qb_name':
                    answer_pass_cmp_perc_string += y + ', '
        answer_pass_cmp_perc_string = answer_pass_cmp_perc_string.strip(', ')
    else:
        answer_pass_cmp_perc_string = answer_pass_cmp_perc

    #qb_pass_td
    top_five_stat_pass_td = get_stat(qb_stats_real, 'qb_td')
    best_qb_td_stat = top_five_stat_pass_td[0]

    top_five_pass_td = get_names_qb(qb_stats_real, 'qb_td')
    answer_pass_td = top_five_pass_td[0]
    r.shuffle(top_five_pass_td)

    checker_pass_td = get_answers_qb(qb_stats_real, 'qb_td')
    if len(checker_pass_td) > 1:
        answer_pass_td_string = ''
        for nary in checker_pass_td:
            for x,y in nary.items():
                if x == 'qb_name':
                    answer_pass_td_string += y + ', '
        answer_pass_td_string = answer_pass_td_string.strip(', ')
    else:
        answer_pass_td_string = answer_pass_td

    #qb_pass_int
    top_five_stat_pass_int = get_stat(qb_stats_real, 'qb_int')
    best_qb_int_stat = top_five_stat_pass_int[0]

    top_five_pass_int = get_names_qb(qb_stats_real, 'qb_int')
    answer_pass_int = top_five_pass_int[0]
    r.shuffle(top_five_pass_int)

    checker_pass_int = get_answers_qb(qb_stats_real, 'qb_int')
    if len(checker_pass_int) > 1:
        answer_pass_int_string = ''
        for nary in checker_pass_int:
            for x,y in nary.items():
                if x == 'qb_name':
                    answer_pass_int_string += y + ', '
        answer_pass_int_string = answer_pass_int_string.strip(', ')
    else:
        answer_pass_int_string = answer_pass_int

    #qb_pass_rating
    top_five_stat_pass_rating = get_stat(qb_stats_real, 'qb_rating')
    best_qb_rating_stat = top_five_stat_pass_rating[0]

    top_five_pass_rating = get_names_qb(qb_stats_real, 'qb_rating')
    answer_pass_rating = top_five_pass_rating[0]
    r.shuffle(top_five_pass_rating)

    checker_pass_rating = get_answers_qb(qb_stats_real, 'qb_rating')
    if len(checker_pass_rating) > 1:
        answer_pass_rating_string = ''
        for nary in checker_pass_rating:
            for x,y in nary.items():
                if x == 'qb_name':
                    answer_pass_rating_string += y + ', '
        answer_pass_rating_string = answer_pass_rating_string.strip(', ')
    else:
        answer_pass_rating_string = answer_pass_rating

    #qb_pass_1st
    top_five_stat_pass_1st = get_stat(qb_stats_real, 'qb_1st')
    best_qb_1st_stat = top_five_stat_pass_1st[0]

    top_five_pass_1st = get_names_qb(qb_stats_real, 'qb_1st')
    answer_pass_1st = top_five_pass_1st[0]
    r.shuffle(top_five_pass_1st)

    checker_pass_1st = get_answers_qb(qb_stats_real, 'qb_1st')
    if len(checker_pass_1st) > 1:
        answer_pass_1st_string = ''
        for nary in checker_pass_1st:
            for x,y in nary.items():
                if x == 'qb_name':
                    answer_pass_1st_string += y + ', '
        answer_pass_1st_string = answer_pass_1st_string.strip(', ')
    else:
        answer_pass_1st_string = answer_pass_1st

    #qb_pass_1st_perc
    top_five_stat_pass_1st_perc = get_stat(qb_stats_real, 'qb_1st_perc')
    best_qb_1st_perc_stat = top_five_stat_pass_1st_perc[0]

    top_five_pass_1st_perc = get_names_qb(qb_stats_real, 'qb_1st_perc')
    answer_pass_1st_perc = top_five_pass_1st_perc[0]
    r.shuffle(top_five_pass_1st_perc)

    checker_pass_1st_perc = get_answers_qb(qb_stats_real, 'qb_1st_perc')
    if len(checker_pass_1st_perc) > 1:
        answer_pass_1st_perc_string = ''
        for nary in checker_pass_1st_perc:
            for x,y in nary.items():
                if x == 'qb_name':
                    answer_pass_1st_perc_string += y + ", "
        answer_pass_1st_perc_string = answer_pass_1st_perc_string.strip(', ')
    else:
        answer_pass_1st_perc_string = answer_pass_1st_perc

    #qb_pass_20
    top_five_stat_pass_20 = get_stat(qb_stats_real, 'qb_20+')
    best_qb_20_stat = top_five_stat_pass_20[0]

    top_five_pass_20 = get_names_qb(qb_stats_real, 'qb_20+')
    answer_pass_20 = top_five_pass_20[0]
    r.shuffle(top_five_pass_20)

    checker_pass_20 = get_answers_qb(qb_stats_real, 'qb_20+')
    if len(checker_pass_20) > 1:
        answer_qb_20_string = ''
        for nary in checker_pass_20:
            for x,y in nary.items():
                if x == 'qb_name':
                    answer_qb_20_string += y + ', '
        answer_qb_20_string = answer_qb_20_string.strip(', ')
    else:
        answer_qb_20_string = answer_pass_20

    #qb_pass_40
    top_five_stat_pass_40 = get_stat(qb_stats_real, 'qb_40+')
    best_qb_40_stat = top_five_stat_pass_40[0]

    top_five_pass_40 = get_names_qb(qb_stats_real, 'qb_40+')
    answer_qb_40 = top_five_pass_40[0]
    r.shuffle(top_five_pass_40)

    checker_pass_40 = get_answers_qb(qb_stats_real, 'qb_40+')
    if len(checker_pass_40) > 1:
        answer_qb_40_string = ''
        for nary in checker_pass_40:
            for x,y in nary.items():
                if x == 'qb_name':
                    answer_qb_40_string += y + ', '
        answer_qb_40_string = answer_qb_40_string.strip(', ')
    else:
        answer_qb_40_string = answer_qb_40

    #qb_long
    top_five_stat_pass_long = get_stat(qb_stats_real, 'qb_long')
    best_qb_long_stat = top_five_stat_pass_long[0]

    top_five_pass_long = get_names_qb(qb_stats_real, 'qb_long')
    answer_pass_long = top_five_pass_long[0]
    r.shuffle(top_five_pass_long)

    checker_pass_long = get_answers_qb(qb_stats_real, 'qb_long')
    if len(checker_pass_long) > 1:
        answer_pass_long_string = ''
        for nary in checker_pass_long:
            for x,y in nary.items():
                if x == 'qb_name':
                    answer_pass_long_string += y + ', '
        answer_pass_long_string = answer_pass_long_string.strip(', ')
    else:
        answer_pass_long_string = answer_pass_long

    #qb_sack
    top_five_stat_pass_sack = get_stat(qb_stats_real, 'qb_sack')
    best_qb_sack_stat = top_five_stat_pass_sack[0]

    top_five_pass_sack = get_names_qb(qb_stats_real, 'qb_sack')
    answer_pass_sack = top_five_pass_sack[0]
    r.shuffle(top_five_pass_sack)

    checker_pass_sack = get_answers_qb(qb_stats_real, 'qb_sack')
    if len(checker_pass_sack) > 1:
        answer_pass_sack_string = ''
        for nary in checker_pass_sack:
            for x,y in nary.items():
                if x == 'qb_name':
                    answer_pass_sack_string += y + ', '
        answer_pass_sack_string = answer_pass_sack_string.strip(', ')
    else:
        answer_pass_sack_string = answer_pass_sack

    #qb_sack_yds
    top_five_stat_pass_sack_yds = get_stat(qb_stats_real, 'qb_sack_yds')
    best_qb_sack_yds_stat = top_five_stat_pass_sack_yds[0]

    top_five_pass_sack_yds = get_names_qb(qb_stats_real, 'qb_sack_yds')
    answer_pass_sack_yds = top_five_pass_sack_yds[0]
    r.shuffle(top_five_pass_sack_yds)

    checker_pass_sack_yds = get_answers_qb(qb_stats_real, 'qb_sack_yds')
    if len(checker_pass_sack_yds) > 1:
        answer_pass_sack_yds_string = ''
        for nary in checker_pass_sack_yds:
            for x,y in nary.items():
                if x == 'qb_name':
                    answer_pass_sack_yds_string += y + ', '
        answer_pass_sack_yds_string = answer_pass_sack_yds_string.strip(', ')
    else:
        answer_pass_sack_yds_string = answer_pass_sack_yds

    #Running Backs

    #rb_rush_yds
    top_five_stat_rush_yds = get_stat(rb_stats_real,'rush_yds')
    best_rb_yds_stat = top_five_stat_rush_yds[0]

    top_five_rb_rush_yds = get_names_rb(rb_stats_real,'rush_yds')
    answer_rb_rush_yds = top_five_rb_rush_yds[0]
    r.shuffle(top_five_rb_rush_yds)

    checker_rush_yds = get_answers_rb(rb_stats_real, 'rush_yds')
    if len(checker_rush_yds) > 1:
        answer_rb_rush_yds_string = ''
        for nary in checker_rush_yds:
            for x,y in nary.items():
                if x == 'name':
                    answer_rb_rush_yds_string += y + ', '
        answer_rb_rush_yds_string = answer_rb_rush_yds_string.strip(', ')
    else:
        answer_rb_rush_yds_string = answer_rb_rush_yds

    #rb_att
    top_five_stat_rb_att = get_stat(rb_stats_real, 'att')
    best_rb_att_stat = top_five_stat_rb_att[0]

    top_five_rb_att = get_names_rb(rb_stats_real, 'att')
    answer_rb_att = top_five_rb_att[0]
    r.shuffle(top_five_rb_att)

    checker_rb_att = get_answers_rb(rb_stats_real, 'att')
    if len(checker_rush_yds) > 1:
        answer_rb_att_string = ''
        for nary in checker_rb_att:
            for x,y in nary.items():
                if x == 'name':
                    answer_rb_att_string += y + ', '
        answer_rb_att_string = answer_rb_att_string.strip(', ')
    else:
        answer_rb_att_string = answer_rb_att

    #rb_yds_att
    top_five_stat_rb_yds_att = get_stat(rb_stats_real, 'rush_yds_att')
    best_rb_yds_att_stat = top_five_stat_rb_yds_att[0]

    top_five_rb_yds_att = get_names_rb(rb_stats_real, 'rush_yds_att')
    answer_rb_yds_att = top_five_rb_yds_att[0]
    r.shuffle(top_five_rb_yds_att)

    checker_rb_yds_att = get_answers_rb(rb_stats_real, 'rush_yds_att')
    if len(checker_rush_yds) > 1:
        answer_rb_yds_att_string = ''
        for nary in checker_rb_yds_att:
            for x,y in nary.items():
                if x == 'name':
                    answer_rb_yds_att_string += y + ', '
        answer_rb_yds_att_string = answer_rb_yds_att_string.strip(', ')
    else:
        answer_rb_yds_att_string = answer_rb_yds_att

    #rb_td
    top_five_stat_rb_td = get_stat(rb_stats_real, 'td')
    best_rb_td_stat = top_five_stat_rb_td[0]

    top_five_rb_td = get_names_rb(rb_stats_real, 'td')
    answer_rb_td = top_five_rb_td[0]
    r.shuffle(top_five_rb_td)

    checker_rb_td = get_answers_rb(rb_stats_real, 'td')
    if len(checker_rb_td) > 1:
        answer_rb_td_string = ''
        for nary in checker_rb_td:
            for x,y in nary.items():
                if x == 'name':
                    answer_rb_td_string += y + ', '
        answer_rb_td_string = answer_rb_td_string.strip(', ')
    else:
        answer_rb_td_string = answer_rb_td

    #rb_20+
    top_five_stat_rb_20 = get_stat(rb_stats_real, '20+')
    best_rb_20_stat = top_five_stat_rb_20[0]

    top_five_rb_20 = get_names_rb(rb_stats_real, '20+')
    answer_rb_20 = top_five_rb_20[0]
    r.shuffle(top_five_rb_td)

    checker_rb_20 = get_answers_rb(rb_stats_real, '20+')
    if len(checker_rb_20) > 1:
        answer_rb_20_string = ''
        for nary in checker_rb_20:
            for x,y in nary.items():
                if x == 'name':
                    answer_rb_20_string += y + ', '
        answer_rb_20_string = answer_rb_20_string.strip(', ')
    else:
        answer_rb_20_string = answer_rb_20

    #rb_40+
    top_five_stat_rb_40 = get_stat(rb_stats_real, '40+')
    best_rb_40_stat = top_five_stat_rb_40[0]

    top_five_rb_40 = get_names_rb(rb_stats_real, '40+')
    answer_rb_40 = top_five_rb_40[0]
    r.shuffle(top_five_rb_40)

    checker_rb_40 = get_answers_rb(rb_stats_real, '40+')
    if len(checker_rb_40) > 1:
        answer_rb_40_string = ''
        for nary in checker_rb_40:
            for x,y in nary.items():
                if x == 'name':
                    answer_rb_40_string += y + ', '
        answer_rb_40_string = answer_rb_40_string.strip(', ')
    else:
        answer_rb_40_string = answer_rb_40

    #rb_long
    top_five_stat_rb_long = get_stat(rb_stats_real, 'long')
    best_rb_long_stat = top_five_stat_rb_long[0]

    top_five_rb_long = get_names_rb(rb_stats_real, 'long')
    answer_rb_long = top_five_rb_long[0]
    r.shuffle(top_five_rb_long)

    checker_rb_long = get_answers_rb(rb_stats_real, 'long')
    if len(checker_rb_long) > 1:
        answer_rb_long_string = ''
        for nary in checker_rb_long:
            for x,y in nary.items():
                if x == 'name':
                    answer_rb_long_string += y + ', '
        answer_rb_long_string = answer_rb_long_string.strip(', ')
    else:
        answer_rb_long_string = answer_rb_long

    #rb_first
    top_five_stat_rb_first = get_stat(rb_stats_real, 'rush_1st')
    best_rb_first_stat = top_five_stat_rb_first[0]

    top_five_rb_first = get_names_rb(rb_stats_real, 'rush_1st')
    answer_rb_first = top_five_rb_first[0]
    r.shuffle(top_five_rb_first)

    checker_rb_first = get_answers_rb(rb_stats_real, 'rush_1st')
    if len(checker_rb_first) > 1:
        answer_rb_first_string = ''
        for nary in checker_rb_first:
            for x,y in nary.items():
                if x == 'name':
                    answer_rb_first_string += y + ', '
        answer_rb_first_string = answer_rb_first_string.strip(', ')
    else:
        answer_rb_first_string = answer_rb_first

    #rb_first_perc
    top_five_stat_rb_first_perc = get_stat(rb_stats_real, 'rush_1st_perc')
    best_rb_first_perc_stat = top_five_stat_rb_first_perc[0]

    top_five_rb_first_perc = get_names_rb(rb_stats_real, 'rush_1st_perc')
    answer_rb_first_perc = top_five_rb_first_perc[0]
    r.shuffle(top_five_rb_first_perc)

    checker_rb_first_perc = get_answers_rb(rb_stats_real, 'rush_1st_perc')
    if len(checker_rb_first_perc) > 1:
        answer_rb_first_perc_string = ''
        for nary in checker_rb_first_perc:
            for x,y in nary.items():
                if x == 'name':
                    answer_rb_first_perc_string += y + ', '
        answer_rb_first_perc_string = answer_rb_first_perc_string.strip(', ')
    else:
        answer_rb_first_perc_string = answer_rb_first_perc

    #rb_fumbles
    top_five_stat_rb_fumbles = get_stat(rb_stats_real, 'rush_fum')
    best_rb_fumbles_stat = top_five_stat_rb_fumbles[0]

    top_five_rb_fumbles = get_names_rb(rb_stats_real, 'rush_fum')
    answer_rb_fumbles = top_five_rb_fumbles[0]
    r.shuffle(top_five_rb_fumbles)

    checker_rb_fumbles = get_answers_rb(rb_stats_real, 'rush_fum')
    if len(checker_rb_fumbles) > 1:
        answer_rb_fumbles_string = ''
        for nary in checker_rb_fumbles:
            for x,y in nary.items():
                if x == 'name':
                    answer_rb_fumbles_string += y + ', '
        answer_rb_fumbles_string = answer_rb_fumbles_string.strip(', ')
    else:
        answer_rb_fumbles_string = answer_rb_fumbles

    #Defense

    #def_yds
    top_five_stat_def_yds = get_stat_def(def_stats_real, 'yds')
    best_def_yds_stat = top_five_stat_def_yds[0]

    top_five_def_yds = get_teams_def(def_stats_real, 'yds')
    answer_def_yds = top_five_def_yds[0]
    r.shuffle(top_five_def_yds)

    checker_def_yds = get_answers_def(def_stats_real, 'yds')
    if len(checker_def_yds) > 1:
        answer_def_yds_string = ''
        for nary in checker_def_yds:
            for x,y in nary.items():
                if x == 'team':
                    answer_def_yds_string += y + ', '
        answer_def_yds_string = answer_def_yds_string.strip(', ')
    else:
        answer_def_yds_string = answer_def_yds

    #def_yds_g
    top_five_stat_def_yds_g = get_stat_def(def_stats_real, 'yds_g')
    best_def_yds_g_stat = top_five_stat_def_yds_g[0]

    top_five_def_yds_g = get_teams_def(def_stats_real, 'yds_g')
    answer_def_yds_g = top_five_def_yds_g[0]
    r.shuffle(top_five_def_yds_g)

    checker_def_yds_g = get_answers_def(def_stats_real, 'yds_g')
    if len(checker_def_yds_g) > 1:
        answer_def_yds_g_string = ''
        for nary in checker_def_yds_g:
            for x,y in nary.items():
                if x == 'team':
                    answer_def_yds_g_string += y + ', '
        answer_def_yds_g_string = answer_def_yds_g_string.strip(', ')
    else:
        answer_def_yds_g_string = answer_def_yds_g

    #def_pass_yds
    top_five_stat_def_pass_yds = get_stat_def(def_stats_real, 'pass_yds')
    best_def_pass_yds_stat = top_five_stat_def_pass_yds[0]

    top_five_def_pass_yds = get_teams_def(def_stats_real, 'pass_yds')
    answer_def_pass_yds = top_five_def_pass_yds[0]
    r.shuffle(top_five_def_pass_yds)

    checker_def_pass_yds = get_answers_def(def_stats_real, 'pass_yds')
    if len(checker_def_pass_yds) > 1:
        answer_def_pass_yds_string = ''
        for nary in checker_def_pass_yds:
            for x,y in nary.items():
                if x == 'team':
                    answer_def_pass_yds_string += y + ', '
        answer_def_pass_yds_string = answer_def_pass_yds_string.strip(', ')
    else:
        answer_def_pass_yds_string = answer_def_pass_yds

    #def_pass_yds_g
    top_five_stat_def_pass_yds_g = get_stat_def(def_stats_real, 'pass_yds_g')
    best_def_pass_yds_g_stat = top_five_stat_def_pass_yds_g[0]

    top_five_def_pass_yds_g = get_teams_def(def_stats_real, 'pass_yds_g')
    answer_def_pass_yds_g = top_five_def_pass_yds_g[0]
    r.shuffle(top_five_def_pass_yds_g)

    checker_def_pass_yds_g = get_answers_def(def_stats_real, 'pass_yds_g')
    if len(checker_def_pass_yds_g) > 1:
        answer_def_pass_yds_g_string = ''
        for nary in checker_def_pass_yds_g:
            for x,y in nary.items():
                if x == 'team':
                    answer_def_pass_yds_g_string += y + ', '
        answer_def_pass_yds_g_string = answer_def_pass_yds_g_string.strip(', ')
    else:
        answer_def_pass_yds_g_string = answer_def_pass_yds_g

    #def_rush_yds
    top_five_stat_def_rush_yds = get_stat_def(def_stats_real, 'rush_yds')
    best_def_rush_yds_stat = top_five_stat_def_rush_yds[0]

    top_five_def_rush_yds = get_teams_def(def_stats_real, 'rush_yds')
    answer_def_rush_yds = top_five_def_rush_yds[0]
    r.shuffle(top_five_def_rush_yds)

    checker_def_rush_yds = get_answers_def(def_stats_real, 'rush_yds')
    if len(checker_def_rush_yds) > 1:
        answer_def_rush_yds_string = ''
        for nary in checker_def_rush_yds:
            for x,y in nary.items():
                if x == 'team':
                    answer_def_rush_yds_string += y + ', '
        answer_def_rush_yds_string = answer_def_rush_yds_string.strip(', ')
    else:
        answer_def_rush_yds_string = answer_def_rush_yds

    #def_rush_yds_g
    top_five_stat_def_rush_yds_g = get_stat_def(def_stats_real, 'rush_yds_g')
    best_def_rush_yds_g_stat = top_five_stat_def_rush_yds_g[0]

    top_five_def_rush_yds_g = get_teams_def(def_stats_real, 'rush_yds_g')
    answer_def_rush_yds_g = top_five_def_rush_yds_g[0]
    r.shuffle(top_five_def_rush_yds_g)

    checker_def_rush_yds_g = get_answers_def(def_stats_real, 'rush_yds_g')
    if len(checker_def_rush_yds_g) > 1:
        answer_def_rush_yds_g_string = ''
        for nary in checker_def_rush_yds_g:
            for x,y in nary.items():
                if x == 'team':
                    answer_def_rush_yds_g_string += y + ', '
        answer_def_rush_yds_g_string = answer_def_rush_yds_g_string.strip(', ')
    else:
        answer_def_rush_yds_g_string = answer_def_rush_yds_g

    #def_points
    top_five_stat_def_points = get_stat_def(def_stats_real, 'points')
    best_def_points_stat = top_five_stat_def_points[0]

    top_five_def_points = get_teams_def(def_stats_real, 'points')
    answer_def_points = top_five_def_points[0]
    r.shuffle(top_five_def_points)

    checker_def_points = get_answers_def(def_stats_real, 'points')
    if len(checker_def_points) > 1:
        answer_def_points_string = ''
        for nary in checker_def_points:
            for x,y in nary.items():
                if x == 'team':
                    answer_def_points_string += y + ', '
        answer_def_points_string = answer_def_points_string.strip(', ')
    else:
        answer_def_points_string = answer_def_points

    #def_points_g
    top_five_stat_def_points_g = get_stat_def(def_stats_real, 'points_g')
    best_def_points_g_stat = top_five_stat_def_points_g[0]

    top_five_def_points_g = get_teams_def(def_stats_real, 'points_g')
    answer_def_points_g = top_five_def_points_g[0]
    r.shuffle(top_five_def_points_g)

    checker_def_points_g = get_answers_def(def_stats_real, 'points_g')
    if len(checker_def_points_g) > 1:
        answer_def_points_g_string = ''
        for nary in checker_def_points_g:
            for x,y in nary.items():
                if x == 'team':
                    answer_def_points_g_string += y + ', '
        answer_def_points_g_string = answer_def_points_g_string.strip(', ')
    else:
        answer_def_points_g_string = answer_def_points_g

    quiz_stuff = {
    #Quarterbacks

    #qb_pass_yds
    'qb_pass_yds_num_1': top_five_qb_pass_yds[0],
    'qb_pass_yds_num_2': top_five_qb_pass_yds[1],
    'qb_pass_yds_num_3': top_five_qb_pass_yds[2],
    'qb_pass_yds_num_4': top_five_qb_pass_yds[3],
    'qb_pass_yds_num_5': top_five_qb_pass_yds[4],
    'answer_qb_pass_yds': answer_pass_yds_string,
    'best_qb_pass_yds_stat': best_qb_pass_yds_stat,
    #qb_yds_per_att
    'pass_yds_att_num_1': top_five_pass_yds_att[0],
    'pass_yds_att_num_2': top_five_pass_yds_att[1],
    'pass_yds_att_num_3': top_five_pass_yds_att[2],
    'pass_yds_att_num_4': top_five_pass_yds_att[3],
    'pass_yds_att_num_5': top_five_pass_yds_att[4],
    'answer_qb_yds_att': answer_pass_yds_att_string,
    'best_qb_yds_att_stat': best_qb_yds_att_stat,
    #pass_att
    'qb_att_num_1': top_five_pass_att[0],
    'qb_att_num_2': top_five_pass_att[1],
    'qb_att_num_3': top_five_pass_att[2],
    'qb_att_num_4': top_five_pass_att[3],
    'qb_att_num_5': top_five_pass_att[4],
    'answer_qb_att': answer_pass_att_string,
    'best_qb_att_stat': best_qb_att_stat,
    #pass_cmp
    'qb_cmp_num_1': top_five_pass_cmp[0],
    'qb_cmp_num_2': top_five_pass_cmp[1],
    'qb_cmp_num_3': top_five_pass_cmp[2],
    'qb_cmp_num_4': top_five_pass_cmp[3],
    'qb_cmp_num_5': top_five_pass_cmp[4],
    'answer_qb_cmp': answer_pass_cmp_string,
    'best_qb_cmp_stat': best_qb_cmp_stat,
    #pass_cmp_perc
    'qb_cmp_perc_num_1': top_five_pass_cmp_perc[0],
    'qb_cmp_perc_num_2': top_five_pass_cmp_perc[1],
    'qb_cmp_perc_num_3': top_five_pass_cmp_perc[2],
    'qb_cmp_perc_num_4': top_five_pass_cmp_perc[3],
    'qb_cmp_perc_num_5': top_five_pass_cmp_perc[4],
    'answer_qb_cmp_perc': answer_pass_cmp_perc_string,
    'best_qb_cmp_perc_stat': best_qb_cmp_perc_stat,
    #pass_td
    'qb_td_num_1': top_five_pass_td[0],
    'qb_td_num_2': top_five_pass_td[1],
    'qb_td_num_3': top_five_pass_td[2],
    'qb_td_num_4': top_five_pass_td[3],
    'qb_td_num_5': top_five_pass_td[4],
    'answer_qb_td': answer_pass_td_string,
    'best_qb_td_stat': best_qb_td_stat,
    #pass_int
    'qb_int_num_1': top_five_pass_int[0],
    'qb_int_num_2': top_five_pass_int[1],
    'qb_int_num_3': top_five_pass_int[2],
    'qb_int_num_4': top_five_pass_int[3],
    'qb_int_num_5': top_five_pass_int[4],
    'answer_qb_int': answer_pass_int_string,
    'best_qb_int_stat': best_qb_int_stat,
    #pass_rating
    'qb_rating_num_1': top_five_pass_rating[0],
    'qb_rating_num_2': top_five_pass_rating[1],
    'qb_rating_num_3': top_five_pass_rating[2],
    'qb_rating_num_4': top_five_pass_rating[3],
    'qb_rating_num_5': top_five_pass_rating[4],
    'answer_qb_rating': answer_pass_rating_string,
    'best_qb_rating_stat': best_qb_rating_stat,
    #pass_1st
    'qb_1st_num_1': top_five_pass_1st[0],
    'qb_1st_num_2': top_five_pass_1st[1],
    'qb_1st_num_3': top_five_pass_1st[2],
    'qb_1st_num_4': top_five_pass_1st[3],
    'qb_1st_num_5': top_five_pass_1st[4],
    'answer_qb_1st': answer_pass_1st_string,
    'best_qb_1st_stat': best_qb_1st_stat,
    #pass_1st_perc
    'qb_1st_perc_num_1': top_five_pass_1st_perc[0],
    'qb_1st_perc_num_2': top_five_pass_1st_perc[1],
    'qb_1st_perc_num_3': top_five_pass_1st_perc[2],
    'qb_1st_perc_num_4': top_five_pass_1st_perc[3],
    'qb_1st_perc_num_5': top_five_pass_1st_perc[4],
    'answer_qb_1st_perc': answer_pass_1st_perc_string,
    'best_qb_1st_perc_stat': best_qb_1st_perc_stat,
    #pass_20+
    'qb_20_num_1': top_five_pass_20[0],
    'qb_20_num_2': top_five_pass_20[1],
    'qb_20_num_3': top_five_pass_20[2],
    'qb_20_num_4': top_five_pass_20[3],
    'qb_20_num_5': top_five_pass_20[4],
    'answer_qb_20': answer_qb_20_string,
    'best_qb_20_stat': best_qb_20_stat,
    #pass_40+
    'qb_40_num_1': top_five_pass_40[0],
    'qb_40_num_2': top_five_pass_40[1],
    'qb_40_num_3': top_five_pass_40[2],
    'qb_40_num_4': top_five_pass_40[3],
    'qb_40_num_5': top_five_pass_40[4],
    'answer_qb_40': answer_qb_40_string,
    'best_qb_40_stat': best_qb_40_stat,
    #pass_long
    'qb_long_num_1': top_five_pass_long[0],
    'qb_long_num_2': top_five_pass_long[1],
    'qb_long_num_3': top_five_pass_long[2],
    'qb_long_num_4': top_five_pass_long[3],
    'qb_long_num_5': top_five_pass_long[4],
    'answer_qb_long': answer_pass_long_string,
    'best_qb_long_stat': best_qb_long_stat,
    #pass_sack
    'qb_sack_num_1': top_five_pass_sack[0],
    'qb_sack_num_2': top_five_pass_sack[1],
    'qb_sack_num_3': top_five_pass_sack[2],
    'qb_sack_num_4': top_five_pass_sack[3],
    'qb_sack_num_5': top_five_pass_sack[4],
    'answer_qb_sack': answer_pass_sack_string,
    'best_qb_sack_stat': best_qb_sack_stat,
    #pass_sack_yds
    'qb_sack_yds_num_1': top_five_pass_sack_yds[0],
    'qb_sack_yds_num_2': top_five_pass_sack_yds[1],
    'qb_sack_yds_num_3': top_five_pass_sack_yds[2],
    'qb_sack_yds_num_4': top_five_pass_sack_yds[3],
    'qb_sack_yds_num_5': top_five_pass_sack_yds[4],
    'answer_qb_sack_yds': answer_pass_sack_yds_string,
    'best_qb_sack_yds_stat': best_qb_sack_yds_stat,

    #Running Backs

    #rb_rush_yds
    'rb_yds_num_1': top_five_rb_rush_yds[0],
    'rb_yds_num_2': top_five_rb_rush_yds[1],
    'rb_yds_num_3': top_five_rb_rush_yds[2],
    'rb_yds_num_4': top_five_rb_rush_yds[3],
    'rb_yds_num_5': top_five_rb_rush_yds[4],
    'answer_rb_rush_yds': answer_rb_rush_yds_string,
    'best_rb_yds_stat': best_rb_yds_stat,
    #rb_att
    'rb_att_num_1': top_five_rb_att[0],
    'rb_att_num_2': top_five_rb_att[1],
    'rb_att_num_3': top_five_rb_att[2],
    'rb_att_num_4': top_five_rb_att[3],
    'rb_att_num_5': top_five_rb_att[4],
    'answer_rb_att': answer_rb_att_string,
    'best_rb_att_stat': best_rb_att_stat,
    #rb_yds_att
    'rb_yds_att_num_1': top_five_rb_yds_att[0],
    'rb_yds_att_num_2': top_five_rb_yds_att[1],
    'rb_yds_att_num_3': top_five_rb_yds_att[2],
    'rb_yds_att_num_4': top_five_rb_yds_att[3],
    'rb_yds_att_num_5': top_five_rb_yds_att[4],
    'answer_rb_yds_att': answer_rb_yds_att_string,
    'best_rb_yds_att_stat': best_rb_yds_att_stat,
    #rb_td
    'rb_td_num_1': top_five_rb_td[0],
    'rb_td_num_2': top_five_rb_td[1],
    'rb_td_num_3': top_five_rb_td[2],
    'rb_td_num_4': top_five_rb_td[3],
    'rb_td_num_5': top_five_rb_td[4],
    'answer_rb_td': answer_rb_td_string,
    'best_rb_td_stat': best_rb_td_stat,
    #rb_20+
    'rb_20_num_1': top_five_rb_20[0],
    'rb_20_num_2': top_five_rb_20[1],
    'rb_20_num_3': top_five_rb_20[2],
    'rb_20_num_4': top_five_rb_20[3],
    'rb_20_num_5': top_five_rb_20[4],
    'answer_rb_20': answer_rb_20_string,
    'best_rb_20_stat': best_rb_20_stat,
    #rb_40+
    'rb_40_num_1': top_five_rb_40[0],
    'rb_40_num_2': top_five_rb_40[1],
    'rb_40_num_3': top_five_rb_40[2],
    'rb_40_num_4': top_five_rb_40[3],
    'rb_40_num_5': top_five_rb_40[4],
    'answer_rb_40': answer_rb_40_string,
    'best_rb_40_stat': best_rb_40_stat,
    #rb_long
    'rb_long_num_1': top_five_rb_long[0],
    'rb_long_num_2': top_five_rb_long[1],
    'rb_long_num_3': top_five_rb_long[2],
    'rb_long_num_4': top_five_rb_long[3],
    'rb_long_num_5': top_five_rb_long[4],
    'answer_rb_long': answer_rb_long_string,
    'best_rb_long_stat': best_rb_long_stat,
    #rb_first
    'rb_first_num_1': top_five_rb_first[0],
    'rb_first_num_2': top_five_rb_first[1],
    'rb_first_num_3': top_five_rb_first[2],
    'rb_first_num_4': top_five_rb_first[3],
    'rb_first_num_5': top_five_rb_first[4],
    'answer_rb_first': answer_rb_first_string,
    'best_rb_first_stat': best_rb_first_stat,
    #rb_first_perc
    'rb_first_perc_num_1': top_five_rb_first_perc[0],
    'rb_first_perc_num_2': top_five_rb_first_perc[1],
    'rb_first_perc_num_3': top_five_rb_first_perc[2],
    'rb_first_perc_num_4': top_five_rb_first_perc[3],
    'rb_first_perc_num_5': top_five_rb_first_perc[4],
    'answer_rb_first_perc': answer_rb_first_perc_string,
    'best_rb_first_perc_stat': best_rb_first_perc_stat,
    #rb_fumbles
    'rb_fumbles_num_1': top_five_rb_fumbles[0],
    'rb_fumbles_num_2': top_five_rb_fumbles[1],
    'rb_fumbles_num_3': top_five_rb_fumbles[2],
    'rb_fumbles_num_4': top_five_rb_fumbles[3],
    'rb_fumbles_num_5': top_five_rb_fumbles[4],
    'answer_rb_fumbles': answer_rb_fumbles_string,
    'best_rb_fumbles_stat': best_rb_fumbles_stat,

    #Defense
    #def_yds
    'def_yds_num_1': top_five_def_yds[0],
    'def_yds_num_2': top_five_def_yds[1],
    'def_yds_num_3': top_five_def_yds[2],
    'def_yds_num_4': top_five_def_yds[3],
    'def_yds_num_5': top_five_def_yds[4],
    'answer_def_yds': answer_def_yds_string,
    'best_def_yds_stat': best_def_yds_stat,
    #def_yds_g
    'def_yds_g_num_1': top_five_def_yds_g[0],
    'def_yds_g_num_2': top_five_def_yds_g[1],
    'def_yds_g_num_3': top_five_def_yds_g[2],
    'def_yds_g_num_4': top_five_def_yds_g[3],
    'def_yds_g_num_5': top_five_def_yds_g[4],
    'answer_def_yds_g': answer_def_yds_g_string,
    'best_def_yds_g_stat': best_def_yds_g_stat,
    #def_pass_yds
    'def_pass_yds_num_1': top_five_def_pass_yds[0],
    'def_pass_yds_num_2': top_five_def_pass_yds[1],
    'def_pass_yds_num_3': top_five_def_pass_yds[2],
    'def_pass_yds_num_4': top_five_def_pass_yds[3],
    'def_pass_yds_num_5': top_five_def_pass_yds[4],
    'answer_def_pass_yds': answer_def_pass_yds_string,
    'best_def_pass_yds_stat': best_def_pass_yds_stat,
    #def_pass_yds_g
    'def_pass_yds_g_num_1': top_five_def_pass_yds_g[0],
    'def_pass_yds_g_num_2': top_five_def_pass_yds_g[1],
    'def_pass_yds_g_num_3': top_five_def_pass_yds_g[2],
    'def_pass_yds_g_num_4': top_five_def_pass_yds_g[3],
    'def_pass_yds_g_num_5': top_five_def_pass_yds_g[4],
    'answer_def_pass_yds_g': answer_def_pass_yds_g_string,
    'best_def_pass_yds_g_stat': best_def_pass_yds_g_stat,
    #def_rush_yds
    'def_rush_yds_num_1': top_five_def_rush_yds[0],
    'def_rush_yds_num_2': top_five_def_rush_yds[1],
    'def_rush_yds_num_3': top_five_def_rush_yds[2],
    'def_rush_yds_num_4': top_five_def_rush_yds[3],
    'def_rush_yds_num_5': top_five_def_rush_yds[4],
    'answer_def_rush_yds': answer_def_rush_yds_string,
    'best_def_rush_yds_stat': best_def_rush_yds_stat,
    #def_rush_yds_g
    'def_rush_yds_g_num_1': top_five_def_rush_yds_g[0],
    'def_rush_yds_g_num_2': top_five_def_rush_yds_g[1],
    'def_rush_yds_g_num_3': top_five_def_rush_yds_g[2],
    'def_rush_yds_g_num_4': top_five_def_rush_yds_g[3],
    'def_rush_yds_g_num_5': top_five_def_rush_yds_g[4],
    'answer_def_rush_yds_g': answer_def_rush_yds_g_string,
    'best_def_rush_yds_g_stat': best_def_rush_yds_g_stat,
    #def_points
    'def_points_num_1': top_five_def_points[0],
    'def_points_num_2': top_five_def_points[1],
    'def_points_num_3': top_five_def_points[2],
    'def_points_num_4': top_five_def_points[3],
    'def_points_num_5': top_five_def_points[4],
    'answer_def_points': answer_def_points_string,
    'best_def_points_stat': best_def_points_stat,
    #def_points_g
    'def_points_g_num_1': top_five_def_points_g[0],
    'def_points_g_num_2': top_five_def_points_g[1],
    'def_points_g_num_3': top_five_def_points_g[2],
    'def_points_g_num_4': top_five_def_points_g[3],
    'def_points_g_num_5': top_five_def_points_g[4],
    'answer_def_points_g': answer_def_points_g_string,
    'best_def_points_g_stat': best_def_points_g_stat,

       }
    return render(request, 'quiz.html', quiz_stuff)

def passing_view(request, *args, **kwargs):
    qb_stats = {
    'qb_1': qb_names_left[0],
's_qb_1':qb_stats_lst[0],
'yd_att_1':qb_att_lst[0],
'num_att_1':qb_num_att_lst[0],
'comp_1':qb_comp_lst[0],
'comp_perc_1':qb_comp_perc_lst[0],
'td_1':qb_td_lst[0],
'int_1':qb_int_lst[0],
'rating_1':qb_rating_lst[0],
'first_downs_1':qb_first_downs_lst[0],
'first_downs_perc_1':qb_first_down_perc_lst[0],
'more_20_1':qb_more_20_lst[0],
'more_40_1':qb_more_40_lst[0],
'long_1':qb_long_lst[0],
'sacks_1':qb_sacks_lst[0],
'sacks_yds_1':qb_sacks_yds_lst[0],
'qb_2': qb_names_left[1],
's_qb_2':qb_stats_lst[1],
'yd_att_2':qb_att_lst[1],
'num_att_2':qb_num_att_lst[1],
'comp_2':qb_comp_lst[1],
'comp_perc_2':qb_comp_perc_lst[1],
'td_2':qb_td_lst[1],
'int_2':qb_int_lst[1],
'rating_2':qb_rating_lst[1],
'first_downs_2':qb_first_downs_lst[1],
'first_downs_perc_2':qb_first_down_perc_lst[1],
'more_20_2':qb_more_20_lst[1],
'more_40_2':qb_more_40_lst[1],
'long_2':qb_long_lst[1],
'sacks_2':qb_sacks_lst[1],
'sacks_yds_2':qb_sacks_yds_lst[1],
'qb_3': qb_names_left[2],
's_qb_3':qb_stats_lst[2],
'yd_att_3':qb_att_lst[2],
'num_att_3':qb_num_att_lst[2],
'comp_3':qb_comp_lst[2],
'comp_perc_3':qb_comp_perc_lst[2],
'td_3':qb_td_lst[2],
'int_3':qb_int_lst[2],
'rating_3':qb_rating_lst[2],
'first_downs_3':qb_first_downs_lst[2],
'first_downs_perc_3':qb_first_down_perc_lst[2],
'more_20_3':qb_more_20_lst[2],
'more_40_3':qb_more_40_lst[2],
'long_3':qb_long_lst[2],
'sacks_3':qb_sacks_lst[2],
'sacks_yds_3':qb_sacks_yds_lst[2],
'qb_4': qb_names_left[3],
's_qb_4':qb_stats_lst[3],
'yd_att_4':qb_att_lst[3],
'num_att_4':qb_num_att_lst[3],
'comp_4':qb_comp_lst[3],
'comp_perc_4':qb_comp_perc_lst[3],
'td_4':qb_td_lst[3],
'int_4':qb_int_lst[3],
'rating_4':qb_rating_lst[3],
'first_downs_4':qb_first_downs_lst[3],
'first_downs_perc_4':qb_first_down_perc_lst[3],
'more_20_4':qb_more_20_lst[3],
'more_40_4':qb_more_40_lst[3],
'long_4':qb_long_lst[3],
'sacks_4':qb_sacks_lst[3],
'sacks_yds_4':qb_sacks_yds_lst[3],
'qb_5': qb_names_left[4],
's_qb_5':qb_stats_lst[4],
'yd_att_5':qb_att_lst[4],
'num_att_5':qb_num_att_lst[4],
'comp_5':qb_comp_lst[4],
'comp_perc_5':qb_comp_perc_lst[4],
'td_5':qb_td_lst[4],
'int_5':qb_int_lst[4],
'rating_5':qb_rating_lst[4],
'first_downs_5':qb_first_downs_lst[4],
'first_downs_perc_5':qb_first_down_perc_lst[4],
'more_20_5':qb_more_20_lst[4],
'more_40_5':qb_more_40_lst[4],
'long_5':qb_long_lst[4],
'sacks_5':qb_sacks_lst[4],
'sacks_yds_5':qb_sacks_yds_lst[4],
'qb_6': qb_names_left[5],
's_qb_6':qb_stats_lst[5],
'yd_att_6':qb_att_lst[5],
'num_att_6':qb_num_att_lst[5],
'comp_6':qb_comp_lst[5],
'comp_perc_6':qb_comp_perc_lst[5],
'td_6':qb_td_lst[5],
'int_6':qb_int_lst[5],
'rating_6':qb_rating_lst[5],
'first_downs_6':qb_first_downs_lst[5],
'first_downs_perc_6':qb_first_down_perc_lst[5],
'more_20_6':qb_more_20_lst[5],
'more_40_6':qb_more_40_lst[5],
'long_6':qb_long_lst[5],
'sacks_6':qb_sacks_lst[5],
'sacks_yds_6':qb_sacks_yds_lst[5],
'qb_7': qb_names_left[6],
's_qb_7':qb_stats_lst[6],
'yd_att_7':qb_att_lst[6],
'num_att_7':qb_num_att_lst[6],
'comp_7':qb_comp_lst[6],
'comp_perc_7':qb_comp_perc_lst[6],
'td_7':qb_td_lst[6],
'int_7':qb_int_lst[6],
'rating_7':qb_rating_lst[6],
'first_downs_7':qb_first_downs_lst[6],
'first_downs_perc_7':qb_first_down_perc_lst[6],
'more_20_7':qb_more_20_lst[6],
'more_40_7':qb_more_40_lst[6],
'long_7':qb_long_lst[6],
'sacks_7':qb_sacks_lst[6],
'sacks_yds_7':qb_sacks_yds_lst[6],
'qb_8': qb_names_left[7],
's_qb_8':qb_stats_lst[7],
'yd_att_8':qb_att_lst[7],
'num_att_8':qb_num_att_lst[7],
'comp_8':qb_comp_lst[7],
'comp_perc_8':qb_comp_perc_lst[7],
'td_8':qb_td_lst[7],
'int_8':qb_int_lst[7],
'rating_8':qb_rating_lst[7],
'first_downs_8':qb_first_downs_lst[7],
'first_downs_perc_8':qb_first_down_perc_lst[7],
'more_20_8':qb_more_20_lst[7],
'more_40_8':qb_more_40_lst[7],
'long_8':qb_long_lst[7],
'sacks_8':qb_sacks_lst[7],
'sacks_yds_8':qb_sacks_yds_lst[7],
'qb_9': qb_names_left[8],
's_qb_9':qb_stats_lst[8],
'yd_att_9':qb_att_lst[8],
'num_att_9':qb_num_att_lst[8],
'comp_9':qb_comp_lst[8],
'comp_perc_9':qb_comp_perc_lst[8],
'td_9':qb_td_lst[8],
'int_9':qb_int_lst[8],
'rating_9':qb_rating_lst[8],
'first_downs_9':qb_first_downs_lst[8],
'first_downs_perc_9':qb_first_down_perc_lst[8],
'more_20_9':qb_more_20_lst[8],
'more_40_9':qb_more_40_lst[8],
'long_9':qb_long_lst[8],
'sacks_9':qb_sacks_lst[8],
'sacks_yds_9':qb_sacks_yds_lst[8],
'qb_10': qb_names_left[9],
's_qb_10':qb_stats_lst[9],
'yd_att_10':qb_att_lst[9],
'num_att_10':qb_num_att_lst[9],
'comp_10':qb_comp_lst[9],
'comp_perc_10':qb_comp_perc_lst[9],
'td_10':qb_td_lst[9],
'int_10':qb_int_lst[9],
'rating_10':qb_rating_lst[9],
'first_downs_10':qb_first_downs_lst[9],
'first_downs_perc_10':qb_first_down_perc_lst[9],
'more_20_10':qb_more_20_lst[9],
'more_40_10':qb_more_40_lst[9],
'long_10':qb_long_lst[9],
'sacks_10':qb_sacks_lst[9],
'sacks_yds_10':qb_sacks_yds_lst[9],
'qb_11': qb_names_left[10],
's_qb_11':qb_stats_lst[10],
'yd_att_11':qb_att_lst[10],
'num_att_11':qb_num_att_lst[10],
'comp_11':qb_comp_lst[10],
'comp_perc_11':qb_comp_perc_lst[10],
'td_11':qb_td_lst[10],
'int_11':qb_int_lst[10],
'rating_11':qb_rating_lst[10],
'first_downs_11':qb_first_downs_lst[10],
'first_downs_perc_11':qb_first_down_perc_lst[10],
'more_20_11':qb_more_20_lst[10],
'more_40_11':qb_more_40_lst[10],
'long_11':qb_long_lst[10],
'sacks_11':qb_sacks_lst[10],
'sacks_yds_11':qb_sacks_yds_lst[10],
'qb_12': qb_names_left[11],
's_qb_12':qb_stats_lst[11],
'yd_att_12':qb_att_lst[11],
'num_att_12':qb_num_att_lst[11],
'comp_12':qb_comp_lst[11],
'comp_perc_12':qb_comp_perc_lst[11],
'td_12':qb_td_lst[11],
'int_12':qb_int_lst[11],
'rating_12':qb_rating_lst[11],
'first_downs_12':qb_first_downs_lst[11],
'first_downs_perc_12':qb_first_down_perc_lst[11],
'more_20_12':qb_more_20_lst[11],
'more_40_12':qb_more_40_lst[11],
'long_12':qb_long_lst[11],
'sacks_12':qb_sacks_lst[11],
'sacks_yds_12':qb_sacks_yds_lst[11],
'qb_13': qb_names_left[12],
's_qb_13':qb_stats_lst[12],
'yd_att_13':qb_att_lst[12],
'num_att_13':qb_num_att_lst[12],
'comp_13':qb_comp_lst[12],
'comp_perc_13':qb_comp_perc_lst[12],
'td_13':qb_td_lst[12],
'int_13':qb_int_lst[12],
'rating_13':qb_rating_lst[12],
'first_downs_13':qb_first_downs_lst[12],
'first_downs_perc_13':qb_first_down_perc_lst[12],
'more_20_13':qb_more_20_lst[12],
'more_40_13':qb_more_40_lst[12],
'long_13':qb_long_lst[12],
'sacks_13':qb_sacks_lst[12],
'sacks_yds_13':qb_sacks_yds_lst[12],
'qb_14': qb_names_left[13],
's_qb_14':qb_stats_lst[13],
'yd_att_14':qb_att_lst[13],
'num_att_14':qb_num_att_lst[13],
'comp_14':qb_comp_lst[13],
'comp_perc_14':qb_comp_perc_lst[13],
'td_14':qb_td_lst[13],
'int_14':qb_int_lst[13],
'rating_14':qb_rating_lst[13],
'first_downs_14':qb_first_downs_lst[13],
'first_downs_perc_14':qb_first_down_perc_lst[13],
'more_20_14':qb_more_20_lst[13],
'more_40_14':qb_more_40_lst[13],
'long_14':qb_long_lst[13],
'sacks_14':qb_sacks_lst[13],
'sacks_yds_14':qb_sacks_yds_lst[13],
'qb_15': qb_names_left[14],
's_qb_15':qb_stats_lst[14],
'yd_att_15':qb_att_lst[14],
'num_att_15':qb_num_att_lst[14],
'comp_15':qb_comp_lst[14],
'comp_perc_15':qb_comp_perc_lst[14],
'td_15':qb_td_lst[14],
'int_15':qb_int_lst[14],
'rating_15':qb_rating_lst[14],
'first_downs_15':qb_first_downs_lst[14],
'first_downs_perc_15':qb_first_down_perc_lst[14],
'more_20_15':qb_more_20_lst[14],
'more_40_15':qb_more_40_lst[14],
'long_15':qb_long_lst[14],
'sacks_15':qb_sacks_lst[14],
'sacks_yds_15':qb_sacks_yds_lst[14],
'qb_16': qb_names_left[15],
's_qb_16':qb_stats_lst[15],
'yd_att_16':qb_att_lst[15],
'num_att_16':qb_num_att_lst[15],
'comp_16':qb_comp_lst[15],
'comp_perc_16':qb_comp_perc_lst[15],
'td_16':qb_td_lst[15],
'int_16':qb_int_lst[15],
'rating_16':qb_rating_lst[15],
'first_downs_16':qb_first_downs_lst[15],
'first_downs_perc_16':qb_first_down_perc_lst[15],
'more_20_16':qb_more_20_lst[15],
'more_40_16':qb_more_40_lst[15],
'long_16':qb_long_lst[15],
'sacks_16':qb_sacks_lst[15],
'sacks_yds_16':qb_sacks_yds_lst[15],
'qb_17': qb_names_left[16],
's_qb_17':qb_stats_lst[16],
'yd_att_17':qb_att_lst[16],
'num_att_17':qb_num_att_lst[16],
'comp_17':qb_comp_lst[16],
'comp_perc_17':qb_comp_perc_lst[16],
'td_17':qb_td_lst[16],
'int_17':qb_int_lst[16],
'rating_17':qb_rating_lst[16],
'first_downs_17':qb_first_downs_lst[16],
'first_downs_perc_17':qb_first_down_perc_lst[16],
'more_20_17':qb_more_20_lst[16],
'more_40_17':qb_more_40_lst[16],
'long_17':qb_long_lst[16],
'sacks_17':qb_sacks_lst[16],
'sacks_yds_17':qb_sacks_yds_lst[16],
'qb_18': qb_names_left[17],
's_qb_18':qb_stats_lst[17],
'yd_att_18':qb_att_lst[17],
'num_att_18':qb_num_att_lst[17],
'comp_18':qb_comp_lst[17],
'comp_perc_18':qb_comp_perc_lst[17],
'td_18':qb_td_lst[17],
'int_18':qb_int_lst[17],
'rating_18':qb_rating_lst[17],
'first_downs_18':qb_first_downs_lst[17],
'first_downs_perc_18':qb_first_down_perc_lst[17],
'more_20_18':qb_more_20_lst[17],
'more_40_18':qb_more_40_lst[17],
'long_18':qb_long_lst[17],
'sacks_18':qb_sacks_lst[17],
'sacks_yds_18':qb_sacks_yds_lst[17],
'qb_19': qb_names_left[18],
's_qb_19':qb_stats_lst[18],
'yd_att_19':qb_att_lst[18],
'num_att_19':qb_num_att_lst[18],
'comp_19':qb_comp_lst[18],
'comp_perc_19':qb_comp_perc_lst[18],
'td_19':qb_td_lst[18],
'int_19':qb_int_lst[18],
'rating_19':qb_rating_lst[18],
'first_downs_19':qb_first_downs_lst[18],
'first_downs_perc_19':qb_first_down_perc_lst[18],
'more_20_19':qb_more_20_lst[18],
'more_40_19':qb_more_40_lst[18],
'long_19':qb_long_lst[18],
'sacks_19':qb_sacks_lst[18],
'sacks_yds_19':qb_sacks_yds_lst[18],
'qb_20': qb_names_left[19],
's_qb_20':qb_stats_lst[19],
'yd_att_20':qb_att_lst[19],
'num_att_20':qb_num_att_lst[19],
'comp_20':qb_comp_lst[19],
'comp_perc_20':qb_comp_perc_lst[19],
'td_20':qb_td_lst[19],
'int_20':qb_int_lst[19],
'rating_20':qb_rating_lst[19],
'first_downs_20':qb_first_downs_lst[19],
'first_downs_perc_20':qb_first_down_perc_lst[19],
'more_20_20':qb_more_20_lst[19],
'more_40_20':qb_more_40_lst[19],
'long_20':qb_long_lst[19],
'sacks_20':qb_sacks_lst[19],
'sacks_yds_20':qb_sacks_yds_lst[19],
'qb_21': qb_names_left[20],
's_qb_21':qb_stats_lst[20],
'yd_att_21':qb_att_lst[20],
'num_att_21':qb_num_att_lst[20],
'comp_21':qb_comp_lst[20],
'comp_perc_21':qb_comp_perc_lst[20],
'td_21':qb_td_lst[20],
'int_21':qb_int_lst[20],
'rating_21':qb_rating_lst[20],
'first_downs_21':qb_first_downs_lst[20],
'first_downs_perc_21':qb_first_down_perc_lst[20],
'more_20_21':qb_more_20_lst[20],
'more_40_21':qb_more_40_lst[20],
'long_21':qb_long_lst[20],
'sacks_21':qb_sacks_lst[20],
'sacks_yds_21':qb_sacks_yds_lst[20],
'qb_22': qb_names_left[21],
's_qb_22':qb_stats_lst[21],
'yd_att_22':qb_att_lst[21],
'num_att_22':qb_num_att_lst[21],
'comp_22':qb_comp_lst[21],
'comp_perc_22':qb_comp_perc_lst[21],
'td_22':qb_td_lst[21],
'int_22':qb_int_lst[21],
'rating_22':qb_rating_lst[21],
'first_downs_22':qb_first_downs_lst[21],
'first_downs_perc_22':qb_first_down_perc_lst[21],
'more_20_22':qb_more_20_lst[21],
'more_40_22':qb_more_40_lst[21],
'long_22':qb_long_lst[21],
'sacks_22':qb_sacks_lst[21],
'sacks_yds_22':qb_sacks_yds_lst[21],
'qb_23': qb_names_left[22],
's_qb_23':qb_stats_lst[22],
'yd_att_23':qb_att_lst[22],
'num_att_23':qb_num_att_lst[22],
'comp_23':qb_comp_lst[22],
'comp_perc_23':qb_comp_perc_lst[22],
'td_23':qb_td_lst[22],
'int_23':qb_int_lst[22],
'rating_23':qb_rating_lst[22],
'first_downs_23':qb_first_downs_lst[22],
'first_downs_perc_23':qb_first_down_perc_lst[22],
'more_20_23':qb_more_20_lst[22],
'more_40_23':qb_more_40_lst[22],
'long_23':qb_long_lst[22],
'sacks_23':qb_sacks_lst[22],
'sacks_yds_23':qb_sacks_yds_lst[22],
'qb_24': qb_names_left[23],
's_qb_24':qb_stats_lst[23],
'yd_att_24':qb_att_lst[23],
'num_att_24':qb_num_att_lst[23],
'comp_24':qb_comp_lst[23],
'comp_perc_24':qb_comp_perc_lst[23],
'td_24':qb_td_lst[23],
'int_24':qb_int_lst[23],
'rating_24':qb_rating_lst[23],
'first_downs_24':qb_first_downs_lst[23],
'first_downs_perc_24':qb_first_down_perc_lst[23],
'more_20_24':qb_more_20_lst[23],
'more_40_24':qb_more_40_lst[23],
'long_24':qb_long_lst[23],
'sacks_24':qb_sacks_lst[23],
'sacks_yds_24':qb_sacks_yds_lst[23],
'qb_25': qb_names_left[24],
's_qb_25':qb_stats_lst[24],
'yd_att_25':qb_att_lst[24],
'num_att_25':qb_num_att_lst[24],
'comp_25':qb_comp_lst[24],
'comp_perc_25':qb_comp_perc_lst[24],
'td_25':qb_td_lst[24],
'int_25':qb_int_lst[24],
'rating_25':qb_rating_lst[24],
'first_downs_25':qb_first_downs_lst[24],
'first_downs_perc_25':qb_first_down_perc_lst[24],
'more_20_25':qb_more_20_lst[24],
'more_40_25':qb_more_40_lst[24],
'long_25':qb_long_lst[24],
'sacks_25':qb_sacks_lst[24],
'sacks_yds_25':qb_sacks_yds_lst[24],
    }
    return render(request, 'passing.html',qb_stats)


def rushing_view(request, *args, **kwargs):
    rb_stats = {
    'rb_1': rb_names[0],
'rb_1_rush_yds': rb_rush_yds[0],
'rb_1_att': rb_att[0],
'rb_1_rush_yds_att': rb_rush_yds_att[0],
'rb_1_td': rb_td[0],
'rb_1_20': rb_20[0],
'rb_1_40': rb_40[0],
'rb_1_long': rb_long[0],
'rb_1_rush_1st': rb_rush_1st[0],
'rb_1_rush_1st_perc': rb_rush_1st_perc[0],
'rb_1_rush_fum': rb_rush_fum[0],
'rb_2': rb_names[1],
'rb_2_rush_yds': rb_rush_yds[1],
'rb_2_att': rb_att[1],
'rb_2_rush_yds_att': rb_rush_yds_att[1],
'rb_2_td': rb_td[1],
'rb_2_20': rb_20[1],
'rb_2_40': rb_40[1],
'rb_2_long': rb_long[1],
'rb_2_rush_1st': rb_rush_1st[1],
'rb_2_rush_1st_perc': rb_rush_1st_perc[1],
'rb_2_rush_fum': rb_rush_fum[1],
'rb_3': rb_names[2],
'rb_3_rush_yds': rb_rush_yds[2],
'rb_3_att': rb_att[2],
'rb_3_rush_yds_att': rb_rush_yds_att[2],
'rb_3_td': rb_td[2],
'rb_3_20': rb_20[2],
'rb_3_40': rb_40[2],
'rb_3_long': rb_long[2],
'rb_3_rush_1st': rb_rush_1st[2],
'rb_3_rush_1st_perc': rb_rush_1st_perc[2],
'rb_3_rush_fum': rb_rush_fum[2],
'rb_4': rb_names[3],
'rb_4_rush_yds': rb_rush_yds[3],
'rb_4_att': rb_att[3],
'rb_4_rush_yds_att': rb_rush_yds_att[3],
'rb_4_td': rb_td[3],
'rb_4_20': rb_20[3],
'rb_4_40': rb_40[3],
'rb_4_long': rb_long[3],
'rb_4_rush_1st': rb_rush_1st[3],
'rb_4_rush_1st_perc': rb_rush_1st_perc[3],
'rb_4_rush_fum': rb_rush_fum[3],
'rb_5': rb_names[4],
'rb_5_rush_yds': rb_rush_yds[4],
'rb_5_att': rb_att[4],
'rb_5_rush_yds_att': rb_rush_yds_att[4],
'rb_5_td': rb_td[4],
'rb_5_20': rb_20[4],
'rb_5_40': rb_40[4],
'rb_5_long': rb_long[4],
'rb_5_rush_1st': rb_rush_1st[4],
'rb_5_rush_1st_perc': rb_rush_1st_perc[4],
'rb_5_rush_fum': rb_rush_fum[4],
'rb_6': rb_names[5],
'rb_6_rush_yds': rb_rush_yds[5],
'rb_6_att': rb_att[5],
'rb_6_rush_yds_att': rb_rush_yds_att[5],
'rb_6_td': rb_td[5],
'rb_6_20': rb_20[5],
'rb_6_40': rb_40[5],
'rb_6_long': rb_long[5],
'rb_6_rush_1st': rb_rush_1st[5],
'rb_6_rush_1st_perc': rb_rush_1st_perc[5],
'rb_6_rush_fum': rb_rush_fum[5],
'rb_7': rb_names[6],
'rb_7_rush_yds': rb_rush_yds[6],
'rb_7_att': rb_att[6],
'rb_7_rush_yds_att': rb_rush_yds_att[6],
'rb_7_td': rb_td[6],
'rb_7_20': rb_20[6],
'rb_7_40': rb_40[6],
'rb_7_long': rb_long[6],
'rb_7_rush_1st': rb_rush_1st[6],
'rb_7_rush_1st_perc': rb_rush_1st_perc[6],
'rb_7_rush_fum': rb_rush_fum[6],
'rb_8': rb_names[7],
'rb_8_rush_yds': rb_rush_yds[7],
'rb_8_att': rb_att[7],
'rb_8_rush_yds_att': rb_rush_yds_att[7],
'rb_8_td': rb_td[7],
'rb_8_20': rb_20[7],
'rb_8_40': rb_40[7],
'rb_8_long': rb_long[7],
'rb_8_rush_1st': rb_rush_1st[7],
'rb_8_rush_1st_perc': rb_rush_1st_perc[7],
'rb_8_rush_fum': rb_rush_fum[7],
'rb_9': rb_names[8],
'rb_9_rush_yds': rb_rush_yds[8],
'rb_9_att': rb_att[8],
'rb_9_rush_yds_att': rb_rush_yds_att[8],
'rb_9_td': rb_td[8],
'rb_9_20': rb_20[8],
'rb_9_40': rb_40[8],
'rb_9_long': rb_long[8],
'rb_9_rush_1st': rb_rush_1st[8],
'rb_9_rush_1st_perc': rb_rush_1st_perc[8],
'rb_9_rush_fum': rb_rush_fum[8],
'rb_10': rb_names[9],
'rb_10_rush_yds': rb_rush_yds[9],
'rb_10_att': rb_att[9],
'rb_10_rush_yds_att': rb_rush_yds_att[9],
'rb_10_td': rb_td[9],
'rb_10_20': rb_20[9],
'rb_10_40': rb_40[9],
'rb_10_long': rb_long[9],
'rb_10_rush_1st': rb_rush_1st[9],
'rb_10_rush_1st_perc': rb_rush_1st_perc[9],
'rb_10_rush_fum': rb_rush_fum[9],
'rb_11': rb_names[10],
'rb_11_rush_yds': rb_rush_yds[10],
'rb_11_att': rb_att[10],
'rb_11_rush_yds_att': rb_rush_yds_att[10],
'rb_11_td': rb_td[10],
'rb_11_20': rb_20[10],
'rb_11_40': rb_40[10],
'rb_11_long': rb_long[10],
'rb_11_rush_1st': rb_rush_1st[10],
'rb_11_rush_1st_perc': rb_rush_1st_perc[10],
'rb_11_rush_fum': rb_rush_fum[10],
'rb_12': rb_names[11],
'rb_12_rush_yds': rb_rush_yds[11],
'rb_12_att': rb_att[11],
'rb_12_rush_yds_att': rb_rush_yds_att[11],
'rb_12_td': rb_td[11],
'rb_12_20': rb_20[11],
'rb_12_40': rb_40[11],
'rb_12_long': rb_long[11],
'rb_12_rush_1st': rb_rush_1st[11],
'rb_12_rush_1st_perc': rb_rush_1st_perc[11],
'rb_12_rush_fum': rb_rush_fum[11],
'rb_13': rb_names[12],
'rb_13_rush_yds': rb_rush_yds[12],
'rb_13_att': rb_att[12],
'rb_13_rush_yds_att': rb_rush_yds_att[12],
'rb_13_td': rb_td[12],
'rb_13_20': rb_20[12],
'rb_13_40': rb_40[12],
'rb_13_long': rb_long[12],
'rb_13_rush_1st': rb_rush_1st[12],
'rb_13_rush_1st_perc': rb_rush_1st_perc[12],
'rb_13_rush_fum': rb_rush_fum[12],
'rb_14': rb_names[13],
'rb_14_rush_yds': rb_rush_yds[13],
'rb_14_att': rb_att[13],
'rb_14_rush_yds_att': rb_rush_yds_att[14],
'rb_14_td': rb_td[13],
'rb_14_20': rb_20[13],
'rb_14_40': rb_40[13],
'rb_14_long': rb_long[13],
'rb_14_rush_1st': rb_rush_1st[13],
'rb_14_rush_1st_perc': rb_rush_1st_perc[13],
'rb_14_rush_fum': rb_rush_fum[13],
'rb_15': rb_names[14],
'rb_15_rush_yds': rb_rush_yds[14],
'rb_15_att': rb_att[14],
'rb_15_rush_yds_att': rb_rush_yds_att[14],
'rb_15_td': rb_td[14],
'rb_15_20': rb_20[14],
'rb_15_40': rb_40[14],
'rb_15_long': rb_long[14],
'rb_15_rush_1st': rb_rush_1st[14],
'rb_15_rush_1st_perc': rb_rush_1st_perc[14],
'rb_15_rush_fum': rb_rush_fum[14],
'rb_16': rb_names[15],
'rb_16_rush_yds': rb_rush_yds[15],
'rb_16_att': rb_att[15],
'rb_16_rush_yds_att': rb_rush_yds_att[15],
'rb_16_td': rb_td[15],
'rb_16_20': rb_20[15],
'rb_16_40': rb_40[15],
'rb_16_long': rb_long[15],
'rb_16_rush_1st': rb_rush_1st[15],
'rb_16_rush_1st_perc': rb_rush_1st_perc[15],
'rb_16_rush_fum': rb_rush_fum[15],
'rb_17': rb_names[16],
'rb_17_rush_yds': rb_rush_yds[16],
'rb_17_att': rb_att[16],
'rb_17_rush_yds_att': rb_rush_yds_att[16],
'rb_17_td': rb_td[16],
'rb_17_20': rb_20[16],
'rb_17_40': rb_40[16],
'rb_17_long': rb_long[16],
'rb_17_rush_1st': rb_rush_1st[16],
'rb_17_rush_1st_perc': rb_rush_1st_perc[16],
'rb_17_rush_fum': rb_rush_fum[16],
'rb_18': rb_names[17],
'rb_18_rush_yds': rb_rush_yds[17],
'rb_18_att': rb_att[17],
'rb_18_rush_yds_att': rb_rush_yds_att[17],
'rb_18_td': rb_td[17],
'rb_18_20': rb_20[17],
'rb_18_40': rb_40[17],
'rb_18_long': rb_long[17],
'rb_18_rush_1st': rb_rush_1st[17],
'rb_18_rush_1st_perc': rb_rush_1st_perc[17],
'rb_18_rush_fum': rb_rush_fum[17],
'rb_19': rb_names[18],
'rb_19_rush_yds': rb_rush_yds[18],
'rb_19_att': rb_att[18],
'rb_19_rush_yds_att': rb_rush_yds_att[18],
'rb_19_td': rb_td[18],
'rb_19_20': rb_20[18],
'rb_19_40': rb_40[18],
'rb_19_long': rb_long[18],
'rb_19_rush_1st': rb_rush_1st[18],
'rb_19_rush_1st_perc': rb_rush_1st_perc[18],
'rb_19_rush_fum': rb_rush_fum[18],
'rb_20': rb_names[19],
'rb_20_rush_yds': rb_rush_yds[19],
'rb_20_att': rb_att[19],
'rb_20_rush_yds_att': rb_rush_yds_att[19],
'rb_20_td': rb_td[19],
'rb_20_20': rb_20[19],
'rb_20_40': rb_40[19],
'rb_20_long': rb_long[19],
'rb_20_rush_1st': rb_rush_1st[19],
'rb_20_rush_1st_perc': rb_rush_1st_perc[19],
'rb_20_rush_fum': rb_rush_fum[19],
'rb_21': rb_names[20],
'rb_21_rush_yds': rb_rush_yds[20],
'rb_21_att': rb_att[20],
'rb_21_rush_yds_att': rb_rush_yds_att[20],
'rb_21_td': rb_td[20],
'rb_21_20': rb_20[20],
'rb_21_40': rb_40[20],
'rb_21_long': rb_long[20],
'rb_21_rush_1st': rb_rush_1st[20],
'rb_21_rush_1st_perc': rb_rush_1st_perc[20],
'rb_21_rush_fum': rb_rush_fum[20],
'rb_22': rb_names[21],
'rb_22_rush_yds': rb_rush_yds[21],
'rb_22_att': rb_att[21],
'rb_22_rush_yds_att': rb_rush_yds_att[21],
'rb_22_td': rb_td[21],
'rb_22_20': rb_20[21],
'rb_22_40': rb_40[21],
'rb_22_long': rb_long[21],
'rb_22_rush_1st': rb_rush_1st[21],
'rb_22_rush_1st_perc': rb_rush_1st_perc[21],
'rb_22_rush_fum': rb_rush_fum[21],
'rb_23': rb_names[22],
'rb_23_rush_yds': rb_rush_yds[22],
'rb_23_att': rb_att[22],
'rb_23_rush_yds_att': rb_rush_yds_att[22],
'rb_23_td': rb_td[22],
'rb_23_20': rb_20[22],
'rb_23_40': rb_40[22],
'rb_23_long': rb_long[22],
'rb_23_rush_1st': rb_rush_1st[22],
'rb_23_rush_1st_perc': rb_rush_1st_perc[22],
'rb_23_rush_fum': rb_rush_fum[22],
'rb_24': rb_names[23],
'rb_24_rush_yds': rb_rush_yds[23],
'rb_24_att': rb_att[23],
'rb_24_rush_yds_att': rb_rush_yds_att[23],
'rb_24_td': rb_td[23],
'rb_24_20': rb_20[23],
'rb_24_40': rb_40[23],
'rb_24_long': rb_long[23],
'rb_24_rush_1st': rb_rush_1st[23],
'rb_24_rush_1st_perc': rb_rush_1st_perc[23],
'rb_24_rush_fum': rb_rush_fum[23],
'rb_25': rb_names[24],
'rb_25_rush_yds': rb_rush_yds[24],
'rb_25_att': rb_att[24],
'rb_25_rush_yds_att': rb_rush_yds_att[24],
'rb_25_td': rb_td[24],
'rb_25_20': rb_20[24],
'rb_25_40': rb_40[24],
'rb_25_long': rb_long[24],
'rb_25_rush_1st': rb_rush_1st[24],
'rb_25_rush_1st_perc': rb_rush_1st_perc[24],
'rb_25_rush_fum': rb_rush_fum[24],
}
    return render(request, 'rushing.html', rb_stats)


def defense_view(request, *args, **kwargs):
    def_stats = {
'team_1': team_names_def[0],
'gp_team_1': gp_def[0],
'yds_team_1': yds_def[0],
'yds_g_team_1': yds_g_def[0],
'pass_yds_team_1': pass_yds_def[0],
'pass_yds_g_team_1': pass_yds_game_def[0],
'rush_yds_team_1': rush_yds_def[0],
'rush_yds_g_team_1': rush_yds_g_def[0],
'points_team_1': points_def[0],
'points_p_team_1': points_p_def[0],
'team_2': team_names_def[1],
'gp_team_2': gp_def[1],
'yds_team_2': yds_def[1],
'yds_g_team_2': yds_g_def[1],
'pass_yds_team_2': pass_yds_def[1],
'pass_yds_g_team_2': pass_yds_game_def[1],
'rush_yds_team_2': rush_yds_def[1],
'rush_yds_g_team_2': rush_yds_g_def[1],
'points_team_2': points_def[1],
'points_p_team_2': points_p_def[1],
'team_3': team_names_def[2],
'gp_team_3': gp_def[2],
'yds_team_3': yds_def[2],
'yds_g_team_3': yds_g_def[2],
'pass_yds_team_3': pass_yds_def[2],
'pass_yds_g_team_3': pass_yds_game_def[2],
'rush_yds_team_3': rush_yds_def[2],
'rush_yds_g_team_3': rush_yds_g_def[2],
'points_team_3': points_def[2],
'points_p_team_3': points_p_def[2],
'team_4': team_names_def[3],
'gp_team_4': gp_def[3],
'yds_team_4': yds_def[3],
'yds_g_team_4': yds_g_def[3],
'pass_yds_team_4': pass_yds_def[3],
'pass_yds_g_team_4': pass_yds_game_def[3],
'rush_yds_team_4': rush_yds_def[3],
'rush_yds_g_team_4': rush_yds_g_def[3],
'points_team_4': points_def[3],
'points_p_team_4': points_p_def[3],
'team_5': team_names_def[4],
'gp_team_5': gp_def[4],
'yds_team_5': yds_def[4],
'yds_g_team_5': yds_g_def[4],
'pass_yds_team_5': pass_yds_def[4],
'pass_yds_g_team_5': pass_yds_game_def[4],
'rush_yds_team_5': rush_yds_def[4],
'rush_yds_g_team_5': rush_yds_g_def[4],
'points_team_5': points_def[4],
'points_p_team_5': points_p_def[4],
'team_6': team_names_def[5],
'gp_team_6': gp_def[5],
'yds_team_6': yds_def[5],
'yds_g_team_6': yds_g_def[5],
'pass_yds_team_6': pass_yds_def[5],
'pass_yds_g_team_6': pass_yds_game_def[5],
'rush_yds_team_6': rush_yds_def[5],
'rush_yds_g_team_6': rush_yds_g_def[5],
'points_team_6': points_def[5],
'points_p_team_6': points_p_def[5],
'team_7': team_names_def[6],
'gp_team_7': gp_def[6],
'yds_team_7': yds_def[6],
'yds_g_team_7': yds_g_def[6],
'pass_yds_team_7': pass_yds_def[6],
'pass_yds_g_team_7': pass_yds_game_def[6],
'rush_yds_team_7': rush_yds_def[6],
'rush_yds_g_team_7': rush_yds_g_def[6],
'points_team_7': points_def[6],
'points_p_team_7': points_p_def[6],
'team_8': team_names_def[7],
'gp_team_8': gp_def[7],
'yds_team_8': yds_def[7],
'yds_g_team_8': yds_g_def[7],
'pass_yds_team_8': pass_yds_def[7],
'pass_yds_g_team_8': pass_yds_game_def[7],
'rush_yds_team_8': rush_yds_def[7],
'rush_yds_g_team_8': rush_yds_g_def[7],
'points_team_8': points_def[7],
'points_p_team_8': points_p_def[7],
'team_9': team_names_def[8],
'gp_team_9': gp_def[8],
'yds_team_9': yds_def[8],
'yds_g_team_9': yds_g_def[8],
'pass_yds_team_9': pass_yds_def[8],
'pass_yds_g_team_9': pass_yds_game_def[8],
'rush_yds_team_9': rush_yds_def[8],
'rush_yds_g_team_9': rush_yds_g_def[8],
'points_team_9': points_def[8],
'points_p_team_9': points_p_def[8],
'team_10': team_names_def[9],
'gp_team_10': gp_def[9],
'yds_team_10': yds_def[9],
'yds_g_team_10': yds_g_def[9],
'pass_yds_team_10': pass_yds_def[9],
'pass_yds_g_team_10': pass_yds_game_def[9],
'rush_yds_team_10': rush_yds_def[9],
'rush_yds_g_team_10': rush_yds_g_def[9],
'points_team_10': points_def[9],
'points_p_team_10': points_p_def[9],
'team_11': team_names_def[10],
'gp_team_11': gp_def[10],
'yds_team_11': yds_def[10],
'yds_g_team_11': yds_g_def[10],
'pass_yds_team_11': pass_yds_def[10],
'pass_yds_g_team_11': pass_yds_game_def[10],
'rush_yds_team_11': rush_yds_def[10],
'rush_yds_g_team_11': rush_yds_g_def[10],
'points_team_11': points_def[10],
'points_p_team_11': points_p_def[10],
'team_12': team_names_def[11],
'gp_team_12': gp_def[11],
'yds_team_12': yds_def[11],
'yds_g_team_12': yds_g_def[11],
'pass_yds_team_12': pass_yds_def[11],
'pass_yds_g_team_12': pass_yds_game_def[11],
'rush_yds_team_12': rush_yds_def[11],
'rush_yds_g_team_12': rush_yds_g_def[11],
'points_team_12': points_def[11],
'points_p_team_12': points_p_def[11],
'team_13': team_names_def[12],
'gp_team_13': gp_def[12],
'yds_team_13': yds_def[12],
'yds_g_team_13': yds_g_def[12],
'pass_yds_team_13': pass_yds_def[12],
'pass_yds_g_team_13': pass_yds_game_def[12],
'rush_yds_team_13': rush_yds_def[12],
'rush_yds_g_team_13': rush_yds_g_def[12],
'points_team_13': points_def[12],
'points_p_team_13': points_p_def[12],
'team_14': team_names_def[13],
'gp_team_14': gp_def[13],
'yds_team_14': yds_def[13],
'yds_g_team_14': yds_g_def[13],
'pass_yds_team_14': pass_yds_def[13],
'pass_yds_g_team_14': pass_yds_game_def[13],
'rush_yds_team_14': rush_yds_def[13],
'rush_yds_g_team_14': rush_yds_g_def[13],
'points_team_14': points_def[13],
'points_p_team_14': points_p_def[13],
'team_15': team_names_def[14],
'gp_team_15': gp_def[14],
'yds_team_15': yds_def[14],
'yds_g_team_15': yds_g_def[14],
'pass_yds_team_15': pass_yds_def[14],
'pass_yds_g_team_15': pass_yds_game_def[14],
'rush_yds_team_15': rush_yds_def[14],
'rush_yds_g_team_15': rush_yds_g_def[14],
'points_team_15': points_def[14],
'points_p_team_15': points_p_def[14],
'team_16': team_names_def[15],
'gp_team_16': gp_def[15],
'yds_team_16': yds_def[15],
'yds_g_team_16': yds_g_def[15],
'pass_yds_team_16': pass_yds_def[15],
'pass_yds_g_team_16': pass_yds_game_def[15],
'rush_yds_team_16': rush_yds_def[15],
'rush_yds_g_team_16': rush_yds_g_def[15],
'points_team_16': points_def[15],
'points_p_team_16': points_p_def[15],
'team_17': team_names_def[16],
'gp_team_17': gp_def[16],
'yds_team_17': yds_def[16],
'yds_g_team_17': yds_g_def[16],
'pass_yds_team_17': pass_yds_def[16],
'pass_yds_g_team_17': pass_yds_game_def[16],
'rush_yds_team_17': rush_yds_def[16],
'rush_yds_g_team_17': rush_yds_g_def[16],
'points_team_17': points_def[16],
'points_p_team_17': points_p_def[16],
'team_18': team_names_def[17],
'gp_team_18': gp_def[17],
'yds_team_18': yds_def[17],
'yds_g_team_18': yds_g_def[17],
'pass_yds_team_18': pass_yds_def[17],
'pass_yds_g_team_18': pass_yds_game_def[17],
'rush_yds_team_18': rush_yds_def[17],
'rush_yds_g_team_18': rush_yds_g_def[17],
'points_team_18': points_def[17],
'points_p_team_18': points_p_def[17],
'team_19': team_names_def[18],
'gp_team_19': gp_def[18],
'yds_team_19': yds_def[18],
'yds_g_team_19': yds_g_def[18],
'pass_yds_team_19': pass_yds_def[18],
'pass_yds_g_team_19': pass_yds_game_def[18],
'rush_yds_team_19': rush_yds_def[18],
'rush_yds_g_team_19': rush_yds_g_def[18],
'points_team_19': points_def[18],
'points_p_team_19': points_p_def[18],
'team_20': team_names_def[19],
'gp_team_20': gp_def[19],
'yds_team_20': yds_def[19],
'yds_g_team_20': yds_g_def[19],
'pass_yds_team_20': pass_yds_def[19],
'pass_yds_g_team_20': pass_yds_game_def[19],
'rush_yds_team_20': rush_yds_def[19],
'rush_yds_g_team_20': rush_yds_g_def[19],
'points_team_20': points_def[19],
'points_p_team_20': points_p_def[19],
'team_21': team_names_def[20],
'gp_team_21': gp_def[20],
'yds_team_21': yds_def[20],
'yds_g_team_21': yds_g_def[20],
'pass_yds_team_21': pass_yds_def[20],
'pass_yds_g_team_21': pass_yds_game_def[20],
'rush_yds_team_21': rush_yds_def[20],
'rush_yds_g_team_21': rush_yds_g_def[20],
'points_team_21': points_def[20],
'points_p_team_21': points_p_def[20],
'team_22': team_names_def[21],
'gp_team_22': gp_def[21],
'yds_team_22': yds_def[21],
'yds_g_team_22': yds_g_def[21],
'pass_yds_team_22': pass_yds_def[21],
'pass_yds_g_team_22': pass_yds_game_def[21],
'rush_yds_team_22': rush_yds_def[21],
'rush_yds_g_team_22': rush_yds_g_def[21],
'points_team_22': points_def[21],
'points_p_team_22': points_p_def[21],
'team_23': team_names_def[22],
'gp_team_23': gp_def[22],
'yds_team_23': yds_def[22],
'yds_g_team_23': yds_g_def[22],
'pass_yds_team_23': pass_yds_def[22],
'pass_yds_g_team_23': pass_yds_game_def[22],
'rush_yds_team_23': rush_yds_def[22],
'rush_yds_g_team_23': rush_yds_g_def[22],
'points_team_23': points_def[22],
'points_p_team_23': points_p_def[22],
'team_24': team_names_def[23],
'gp_team_24': gp_def[23],
'yds_team_24': yds_def[23],
'yds_g_team_24': yds_g_def[23],
'pass_yds_team_24': pass_yds_def[23],
'pass_yds_g_team_24': pass_yds_game_def[23],
'rush_yds_team_24': rush_yds_def[23],
'rush_yds_g_team_24': rush_yds_g_def[23],
'points_team_24': points_def[23],
'points_p_team_24': points_p_def[23],
'team_25': team_names_def[24],
'gp_team_25': gp_def[24],
'yds_team_25': yds_def[24],
'yds_g_team_25': yds_g_def[24],
'pass_yds_team_25': pass_yds_def[24],
'pass_yds_g_team_25': pass_yds_game_def[24],
'rush_yds_team_25': rush_yds_def[24],
'rush_yds_g_team_25': rush_yds_g_def[24],
'points_team_25': points_def[24],
'points_p_team_25': points_p_def[24],
'team_26': team_names_def[25],
'gp_team_26': gp_def[25],
'yds_team_26': yds_def[25],
'yds_g_team_26': yds_g_def[25],
'pass_yds_team_26': pass_yds_def[25],
'pass_yds_g_team_26': pass_yds_game_def[25],
'rush_yds_team_26': rush_yds_def[25],
'rush_yds_g_team_26': rush_yds_g_def[25],
'points_team_26': points_def[25],
'points_p_team_26': points_p_def[25],
'team_27': team_names_def[26],
'gp_team_27': gp_def[26],
'yds_team_27': yds_def[26],
'yds_g_team_27': yds_g_def[26],
'pass_yds_team_27': pass_yds_def[26],
'pass_yds_g_team_27': pass_yds_game_def[26],
'rush_yds_team_27': rush_yds_def[26],
'rush_yds_g_team_27': rush_yds_g_def[26],
'points_team_27': points_def[26],
'points_p_team_27': points_p_def[26],
'team_28': team_names_def[27],
'gp_team_28': gp_def[27],
'yds_team_28': yds_def[27],
'yds_g_team_28': yds_g_def[27],
'pass_yds_team_28': pass_yds_def[27],
'pass_yds_g_team_28': pass_yds_game_def[27],
'rush_yds_team_28': rush_yds_def[27],
'rush_yds_g_team_28': rush_yds_g_def[27],
'points_team_28': points_def[27],
'points_p_team_28': points_p_def[27],
'team_29': team_names_def[28],
'gp_team_29': gp_def[28],
'yds_team_29': yds_def[28],
'yds_g_team_29': yds_g_def[28],
'pass_yds_team_29': pass_yds_def[28],
'pass_yds_g_team_29': pass_yds_game_def[28],
'rush_yds_team_29': rush_yds_def[28],
'rush_yds_g_team_29': rush_yds_g_def[28],
'points_team_29': points_def[28],
'points_p_team_29': points_p_def[28],
'team_30': team_names_def[29],
'gp_team_30': gp_def[29],
'yds_team_30': yds_def[29],
'yds_g_team_30': yds_g_def[29],
'pass_yds_team_30': pass_yds_def[29],
'pass_yds_g_team_30': pass_yds_game_def[29],
'rush_yds_team_30': rush_yds_def[29],
'rush_yds_g_team_30': rush_yds_g_def[29],
'points_team_30': points_def[29],
'points_p_team_30': points_p_def[29],
'team_31': team_names_def[30],
'gp_team_31': gp_def[30],
'yds_team_31': yds_def[30],
'yds_g_team_31': yds_g_def[30],
'pass_yds_team_31': pass_yds_def[30],
'pass_yds_g_team_31': pass_yds_game_def[30],
'rush_yds_team_31': rush_yds_def[30],
'rush_yds_g_team_31': rush_yds_g_def[30],
'points_team_31': points_def[30],
'points_p_team_31': points_p_def[30],
'team_32': team_names_def[31],
'gp_team_32': gp_def[31],
'yds_team_32': yds_def[31],
'yds_g_team_32': yds_g_def[31],
'pass_yds_team_32': pass_yds_def[31],
'pass_yds_g_team_32': pass_yds_game_def[31],
'rush_yds_team_32': rush_yds_def[31],
'rush_yds_g_team_32': rush_yds_g_def[31],
'points_team_32': points_def[31],
'points_p_team_32': points_p_def[31],
    }
    return render(request, 'defense.html', def_stats)
