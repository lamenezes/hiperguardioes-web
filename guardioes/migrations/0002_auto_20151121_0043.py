# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('guardians', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardiandata',
            name='received_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 21, 0, 43, 40, 146562), verbose_name='Received Date'),
        ),
    ]
