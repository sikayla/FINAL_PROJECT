from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return f"{self.name} - {self.student.name}"

class Grade(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')
    activity = models.FloatField()
    quiz = models.FloatField()
    exam = models.FloatField()

    def __str__(self):
        return f"{self.subject.name}: A:{self.activity} Q:{self.quiz} E:{self.exam}"

