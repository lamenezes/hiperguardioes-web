# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0002_auto_20150712_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuardianData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collected_date', models.DateTimeField(verbose_name='Collected Date')),
                ('received_date', models.DateTimeField(default=datetime.datetime(2015, 11, 21, 0, 42, 59, 110904), verbose_name='Received Date')),
                ('data', jsonfield.fields.JSONField(verbose_name='Data')),
            ],
        ),
        migrations.CreateModel(
            name='GuardianDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(unique=True, max_length=100, verbose_name='Device')),
                ('node', models.ForeignKey(verbose_name='Node', to='nodes.Node')),
            ],
        ),
        migrations.AddField(
            model_name='guardiandata',
            name='device',
            field=models.ForeignKey(verbose_name='Device', to='guardioes.GuardianDevice'),
        ),
    ]
