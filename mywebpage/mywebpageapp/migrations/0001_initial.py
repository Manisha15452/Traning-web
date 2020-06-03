# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-12-06 00:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Traineename', models.CharField(max_length=100)),
                ('Totalassignments', models.IntegerField()),
                ('Totalassignmentscompleted', models.IntegerField()),
                ('Totalassignmentspending', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TraineeName', models.CharField(max_length=100, verbose_name='Name')),
                ('AssignmentName', models.CharField(max_length=100, verbose_name='Assignment Name')),
                ('CourseName', models.CharField(default='Python', max_length=50, verbose_name='Course')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Phone_number', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=254)),
                ('Comment', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Mywebpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=254)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=20)),
                ('password', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('Username', models.TextField(max_length=20)),
                ('Password', models.TextField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]