from django.db import models

# Create your models here.
class Qb(models.Model):
    name = models.CharField(max_length=150, primary_key=True)
    pass_yds = models.IntegerField()
    yds_att = models.FloatField()
    att = models.IntegerField()
    cmp = models.IntegerField()
    cmp_perc = models.FloatField()
    td = models.IntegerField()
    int = models.IntegerField()
    qb_rating = models.FloatField()
    first = models.IntegerField()
    first_perc = models.FloatField()
    more_20 = models.IntegerField()
    more_40 = models.IntegerField()
    lng = models.IntegerField()
    sack = models.IntegerField()
    sack_Y = models.IntegerField()


class Rb(models.Model):
    name = models.CharField(max_length=150, primary_key=True)
    rush_yds = models.IntegerField()
    att = models.IntegerField()
    rush_yds_att = models.FloatField()
    td = models.IntegerField()
    twenty = models.IntegerField()
    fourty = models.IntegerField()
    long = models.IntegerField()
    rush_1st = models.IntegerField()
    rush_1st_perc = models.IntegerField()
    rush_fum = models.IntegerField()

class Defense(models.Model):
    team = models.CharField(max_length=150, primary_key=True)
    g_p = models.IntegerField()
    yds = models.IntegerField()
    yds_g = models.FloatField()
    pass_yds = models.IntegerField()
    pass_yds_g = models.FloatField()
    rush_yds = models.IntegerField()
    rush_yds_g = models.FloatField()
    points = models.IntegerField()
    point_g = models.FloatField()
