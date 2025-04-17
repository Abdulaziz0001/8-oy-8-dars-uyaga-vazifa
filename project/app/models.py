from django.db import models

# Create your models here.

class Klass(models.Model):
    name = models.CharField(max_length=100)



class Student(models.Model):
    full_name = models.CharField(max_length=100)
    class_name = models.ForeignKey(Klass, on_delete=models.CASCADE)



class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    klass = models.ManyToManyField(Klass)