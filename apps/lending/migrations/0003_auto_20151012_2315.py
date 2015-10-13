# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0002_borrower_needed'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='total_left',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='lender',
            name='total_left',
            field=models.IntegerField(null=True),
        ),
    ]
