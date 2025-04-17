from django.contrib import admin
from .models import Klass, Teacher, Student

# Register your models here.

admin.site.register(Klass)
admin.site.register(Teacher)
admin.site.register(Student)