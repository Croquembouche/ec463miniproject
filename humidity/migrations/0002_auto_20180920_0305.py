# Generated by Django 2.1.1 on 2018-09-20 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humidity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humidity',
            name='datetime_recorded',
            field=models.DateTimeField(verbose_name='datetime_recorded'),
        ),
        migrations.AlterField(
            model_name='humidity',
            name='humidity',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
