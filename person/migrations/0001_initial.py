# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=128)),
                ('street', models.CharField(max_length=128)),
                ('external_number', models.CharField(max_length=128)),
                ('internal_number', models.CharField(blank=True, default='', max_length=129)),
                ('neighbour', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('zipcode', models.CharField(max_length=10)),
                ('address_type', models.CharField(default='1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('dni', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Country'),
        ),
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Person'),
        ),
    ]
