from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Klass, Teacher, Student
from .serializer import KlassSerializer, TeacherSerializer, StudentSerializer


# Create your views here.

class KlassViewSet(ModelViewSet):
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer



class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer