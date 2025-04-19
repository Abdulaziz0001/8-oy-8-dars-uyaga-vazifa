from rest_framework import serializers
from .models import Klass, Teacher, Student



class KlassSerializer(serializers.ModelSerializer):
    # tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    tracks = serializers.HyperlinkedModelSerializer(many=True, read_only=True)
    class Meta:
        model = Klass
        fields = ['id', 'name', 'tracks']


class TeacherSerializer(serializers.ModelSerializer):
    # tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    tracks = serializers.HyperlinkedModelSerializer(many=True, read_only=True)
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'price', 'tracks']



class StudentSerializer(serializers.ModelSerializer):
    # tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    tracks = serializers.HyperlinkedModelSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'tracks']