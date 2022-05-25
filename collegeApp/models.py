from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_fee = models.IntegerField(null=True)

class Tutor(models.Model):
    tutor_name = models.CharField(max_length=255)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)


class Student(models.Model):
    student_first_name = models.CharField(max_length=255)
    student_last_name = models.CharField(max_length=255,null=True)
    student_address = models.CharField(max_length=255)
    student_age = models.IntegerField()
    student_joined = models.DateField()
    tutor = models.ForeignKey(Tutor,on_delete=models.CASCADE,null=True)

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=255,null=True)
    gender = models.CharField(max_length=100)
    mobile = models.CharField(max_length=255)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)

