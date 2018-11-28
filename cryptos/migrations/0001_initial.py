# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoBalance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('balanceBTC', models.IntegerField(default=0)),
                ('balanceLTC', models.IntegerField(default=0)),
                ('balanceXRP', models.IntegerField(default=0)),
                ('balanceETH', models.IntegerField(default=0)),
                ('balanceXLM', models.IntegerField(default=0)),
                ('balanceXMR', models.IntegerField(default=0)),
                ('balanceADA', models.IntegerField(default=0)),
                ('balanceTRX', models.IntegerField(default=0)),
                ('balanceEOS', models.IntegerField(default=0)),
                ('balanceBCH', models.IntegerField(default=0)),
            ],
        ),
    ]
