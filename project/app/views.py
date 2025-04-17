from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework import permissions
from .models import Klass
from .serializer import KlassSerializer, TeacherSerializer, StudentSerializer


# Create your views here.



class KlassViewSet(ViewSet):
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer
    permission_classes = [permissions.IsAuthenticated]



class TeacherViewSet(ViewSet):
    queryset = Klass.objects.filter()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]



class StudentViewSet(ViewSet):
    queryset = Klass.objects.filter()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]