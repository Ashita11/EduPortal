from email.policy import default
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone



# class user(models.Model):
#     uroll = models.IntegerField(default=0)
#     uname = models.CharField(max_length=100,default=0)
#     uemail = models.EmailField(primary_key=True,default=0)
#     upass = models.CharField(max_length=30,default=0)
#     umob =models.DecimalField(default=0,decimal_places=0,max_digits=10)
#     ubranch = models.CharField(max_length=30,default=0)
#     um =models.IntegerField(default=0)
#     uelec =models.IntegerField(default=0)
#     uelex =models.IntegerField(default=0)
#     uchem =models.IntegerField(default=0)
#     uphy =models.IntegerField(default=0)
#     um2 =models.IntegerField(default=0)
#     uelec2 =models.IntegerField(default=0)
#     uelex2 =models.IntegerField(default=0)
#     uchem2 =models.IntegerField(default=0)
#     uphy2 =models.IntegerField(default=0)
#     upaid=models.IntegerField(default=0)
#     ufine=models.IntegerField(default=0)
#     upending=models.IntegerField(default=0)
#     jm=models.JSONField(default="dict")
#     jp=models.JSONField(default="dict")
#     jc=models.JSONField(default="dict")
#     jel=models.JSONField(default="dict")
#     jex=models.JSONField(default="dict")

#     class Meta:
#         app_label = 'Student'

# class teacherr(models.Model):
#     temail=models.EmailField(primary_key=True,default=0)
#     tpass=models.CharField(max_length=30,default=0)


#     class Meta:
#         app_label = 'Student'




class Course(models.Model):
    name = models.CharField(max_length=100)
    fee = models.FloatField()
   
class Section(models.Model):
    name = models.CharField(max_length=10)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,default=None)

class Subject(models.Model):
    code = models.CharField(max_length=100,default=None)
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE) 
    sec = models.ForeignKey(Section,on_delete=models.CASCADE,default=None) 

class Student(models.Model):
    uroll = models.IntegerField(default=0)
    uname = models.CharField(max_length=100,default=0)
    uemail = models.EmailField(primary_key=True,default=0)
    upass = models.CharField(max_length=30,default=0)
    umob = models.DecimalField(default=0,decimal_places=0,max_digits=10)
    ucourse = models.ForeignKey(Course,on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE,default=None)

class Staff(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject)
    mob = models.DecimalField(max_digits=10,decimal_places=0,default=None)
    doj = models.DateField(default=None)
    dob = models.DateField(default=None)
    pswd = models.CharField(max_length=100,default=None)

class Attendance(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    date = models.DateField()
    status = models.BooleanField(default=False)