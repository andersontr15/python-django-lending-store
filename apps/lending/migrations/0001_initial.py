# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.TextField(max_length=20)),
                ('last_name', models.TextField(max_length=20)),
                ('email', models.TextField(max_length=20)),
                ('password', models.TextField(max_length=20)),
                ('amount', models.IntegerField()),
                ('purpose', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('raised', models.IntegerField()),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Lender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.TextField(max_length=20)),
                ('last_name', models.TextField(max_length=20)),
                ('email', models.TextField(max_length=20)),
                ('password', models.TextField()),
                ('money', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(null=True)),
                ('borrower', models.ForeignKey(to='lending.Borrower')),
                ('lender', models.ForeignKey(to='lending.Lender')),
            ],
        ),
    ]
