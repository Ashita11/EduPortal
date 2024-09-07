
from dataclasses import field
from enum import unique
from socket import fromshare
from unittest.util import _MAX_LENGTH
from urllib import request
import django.forms
# from captcha.fields import CaptchaField






# class sign(django.forms.Form):
#     name=django.forms.CharField(max_length=30)
#     email=django.forms.EmailField()
#     password=django.forms.CharField(widget=django.forms.PasswordInput)
#     confirmpassword=django.forms.CharField(widget=django.forms.PasswordInput)

# class login(django.forms.Form):
#     email=django.forms.EmailField(max_length=30,)
#     password=django.forms.CharField(widget=django.forms.PasswordInput(attrs={'class':'pclass'}))

# class captchademo():
#     captcha=CaptchaField()

# class image():

# class DB(django.forms.Form):
#     name=django.forms.CharField(max_length=30,widget=django.forms.TextInput(attrs={'placeholder':'ENTER YOUR NAME','style':'width:20%;','class':'c1'}))
#     roll=django.forms.IntegerField(max_value=300)
#     email=django.forms.EmailField()
#     contact=django.forms.CharField(widget=django.forms.DecimalField)
#     branch=django.forms.CharField(max_length=30)

class savee(django.forms.Form):
    email=django.forms.EmailField()
    password=django.forms.CharField(widget=django.forms.PasswordInput)

    
