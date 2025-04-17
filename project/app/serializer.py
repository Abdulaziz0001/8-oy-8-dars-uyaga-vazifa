from rest_framework import serializers
from .models import Klass, Teacher, Student



class KlassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klass
        fields = '__all__'



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klass
        fields = '__all__'



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klass
        fields = '__all__'