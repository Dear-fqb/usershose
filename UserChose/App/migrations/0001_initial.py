# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-11 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=12, verbose_name='鞋子颜色')),
                ('size', models.CharField(max_length=8, verbose_name='鞋子大小')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户姓名')),
                ('userphone', models.CharField(max_length=16, unique=True, verbose_name='手机号')),
            ],
        ),
        migrations.AddField(
            model_name='chose',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.User'),
        ),
    ]
