from __future__ import unicode_literals
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.db.models.signals import post_save
#from register.forms import AdminForm
from django.db.models.signals import *
import os
from django.conf import settings

class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    current_position = models.TextField( blank=True)
    current_company = models.TextField( blank=True)        
    location = models.TextField( blank=True)
    summary = models.TextField( blank=True)
    skills = models.TextField(blank=True)

    def __str__(self):
        return self.full_name

class Education(models.Model):
    user= models.ForeignKey(Profile,on_delete=models.CASCADE,)
    college = models.TextField( blank=True)
    course = models.TextField( blank=True)

    def __str__(self):
        return self.user.full_name
    
class Project(models.Model):
    user= models.ForeignKey(Profile,on_delete=models.CASCADE,)
    title = models.TextField( blank=True)
    description = models.TextField( blank=True)

    def __str__(self):
        return self.user.full_name

class Experience(models.Model):
    user= models.ForeignKey(Profile,on_delete=models.CASCADE,)
    designation = models.TextField( blank=True)
    company = models.TextField( blank=True)
    start_date = models.TextField( blank=True)
    end_date = models.TextField( blank=True)
    description = models.TextField( blank=True)

    def __str__(self):
        return self.user.full_name

   
class Job_Profile(models.Model):
    Company = models.CharField(max_length=200)
    designation = models.TextField( blank=True)
    location = models.TextField( blank=True)
    Description = models.TextField(blank=True)
    Experience = models.TextField(blank=True)
    skills = models.TextField(blank=True)
   
    def __str__(self):
        return self.Company

class Applied(models.Model):
    user= models.ForeignKey(Profile,on_delete=models.CASCADE,)
    job = models.ForeignKey(Job_Profile,on_delete=models.CASCADE,)

    def __str__(self):
        return self.user.full_name 
    
    
