# Generated by Django 3.1.2 on 2020-11-11 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_auto_20201109_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='rb',
            name='rush_yds_att',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
