from rest_framework import serializers
from .models import Student, Subject, Grade

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    grades = GradeSerializer(many=True, read_only=True)
    class Meta:
        model = Subject
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = '__all__'
