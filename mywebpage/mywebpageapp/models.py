# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Mywebpage(models.Model):
    title = models.TextField(max_length=254)
    text = models.TextField()


class Contact(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=100)
    Address = models.CharField(max_length=254)
    Comment = models.CharField(max_length=254)

    def __str__(self):
        return self.First_Name


class Ass(models.Model):
    Traineename = models.CharField(max_length=100)
    Totalassignments = models.IntegerField()
    Totalassignmentscompleted = models.IntegerField()
    Totalassignmentspending = models.IntegerField()
    Email = models.EmailField()

    def __str__(self):
        return self.Traineename


class Assignment1(models.Model):
    TraineeName = models.CharField(max_length=100, verbose_name="Name")
    AssignmentName = models.CharField(max_length=100, verbose_name="Assignment Name")
    CourseName= models.CharField(max_length=50, default='Python', verbose_name="Course")

    def __str__(self):
        return self.TraineeName


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    Username=models.TextField(max_length=20)
    Password=models.TextField(max_length=20)

    def __str__(self):
        return self.user.username


class UserLogin(models.Model):
    username = models.TextField(max_length=20)
    password = models.TextField(max_length=20)
