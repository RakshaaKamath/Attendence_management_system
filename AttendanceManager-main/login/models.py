from django.db import models
from dateutil.relativedelta import relativedelta
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
class Department(models.Model):
    dept_id = models.CharField(max_length=20,primary_key = True)
    dept_name = models.CharField(max_length=50)

class Class(models.Model): 
    class_id = models.CharField(max_length=20,primary_key=True)
    total_students = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(100)])

class Student(models.Model):
    stud_id = models.CharField(max_length=20,primary_key=True)
    s_password = models.CharField(max_length=30)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=gender_choices,default='M')
    dob = models.DateField(max_length=8,null=True)
    age = models.IntegerField(default=17) 
    def __str__(self):
        today = datetime.date.today()
        delta = relativedelta(today, self.dob)
        return str(delta.years)
    
    Sphone_No = models.CharField(null=True,max_length=31)
    SEmail = models.EmailField(max_length = 254,null=True,blank=False,unique=True)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    
class Faculty(models.Model):
    fac_id = models.CharField(max_length=20,primary_key=True)
    f_password = models.CharField(max_length=30)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
   
class Course(models.Model):
    course_id = models.CharField(max_length=20,primary_key=True)
    course_name = models.CharField(max_length=50)
    credits = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])

class Attendance(models.Model):
    stud_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    fac_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    presence = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(1)])
   
   
    class Meta:
        unique_together = (("stud_id", "course_id","date"),)


class Teache(models.Model):
    fac_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    Tphone_No = models.CharField(null=False,max_length=31,blank=False,default='+91 77636 12343')
    TEmail = models.EmailField(max_length = 254,null=True,blank=True,unique=True)

    class Meta:
        unique_together = (("course_id", "class_id"),)
 