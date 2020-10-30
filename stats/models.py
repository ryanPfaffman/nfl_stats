from django.db import models

# Create your models here.
class qb(models.Model):
    name = models.CharField(max_length=150)
    pass_yds = models.FloatField()
    yds_att = models.FloatField()
    att = models.FloatField()
    cmp = models.FloatField()
    cmp_perc = models.FloatField()
    td = models.FloatField()
    int = models.FloatField()
    qb_rating = models.FloatField()
    first = models.FloatField()
    first_perc = models.FloatField()
    more_20 = models.FloatField()
    more_40 = models.FloatField()
    lng = models.FloatField()
    sack = models.FloatField()
    sack_Y = models.FloatField()
