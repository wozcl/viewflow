# Generated by Django 2.1.4 on 2018-12-21 23:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficinaPartes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacacionesprocess',
            name='apellido',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacacionesprocess',
            name='fecha_nacimiento',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 21, 20, 38, 56, 745040)),
        ),
    ]
