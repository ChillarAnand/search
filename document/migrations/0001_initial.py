# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('data', models.TextField()),
            ],
        ),
    ]
