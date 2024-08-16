from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Addcourse(models.Model):
    coursename=models.CharField(max_length=225)
    coursefee=models.IntegerField(null=True)
class Student(models.Model):
    course=models.ForeignKey(Addcourse,on_delete=models.CASCADE,null=True)
    studentname=models.CharField(max_length=225)
    Address=models.CharField(max_length=225)
    Age=models.IntegerField(null=True)
    Date=models.DateField(null=True)

class Teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Addcourse,on_delete=models.CASCADE,null=True)
    Address=models.CharField(max_length=225)
    Age=models.IntegerField(null=True)
    Contactnumber=models.CharField(max_length=225)
    img=models.ImageField(blank=True,upload_to="img/",null=True)