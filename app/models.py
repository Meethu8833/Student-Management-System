from django.db import models

# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=16)
    def __str__(self):
        return self.username
    
class Classes(models.Model):
    class_name=models.CharField(max_length=100)
    section=models.CharField(max_length=100)
    class_teacher=models.CharField(max_length=100)
    def __str__(self):
        return self.class_name
    
class Students(models.Model):
    name=models.CharField(max_length=100)
    roll_number=models.IntegerField()
    student_class=models.ForeignKey(Classes,on_delete=models.CASCADE)
    email=models.EmailField()
    date_of_birth=models.DateField()
    