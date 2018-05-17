
# from django.forms import ModelForm
from django import forms
# # Create your models here.


from django.db import models
from django.utils import timezone
from .choices import *
class Contact(models.Model):


    keywords = models.CharField(max_length=50,blank=True,null=True)
    type = models.CharField(max_length=50,choices=STATUS_CHOICES,default=1)

