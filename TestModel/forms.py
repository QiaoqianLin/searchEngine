from django import forms
from .choices import *

class AddForm(forms.Form):

    keywords = forms.CharField()
    type = forms.ChoiceField(choices = STATUS_CHOICES, required=True)

# class AddForm(forms.Form):
#     CONTACT_GROUP=(("PRE-SALES","PRE-SALES"),("SALES","SALES"),("SERVICE","SERVICE"))
#
#     contact_name = forms.CharField(max_length=50,blank=True,null=True)
#     contact_group = forms.CharField(max_length=50,choices=CONTACT_GROUP,blank=True,null=True)
#     a = forms.IntegerField()
#     b = forms.IntegerField()