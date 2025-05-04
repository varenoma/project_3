from django.db import models

# Create your models here.


class TeacherDb(models.Model):
    SUBJECT_CHOICES = [
        ('math', 'Math'),
        ('physics', 'Physics'),
        ('english', 'English'),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    experience_years = models.IntegerField()
    subject = models.CharField(max_length=25, choices=SUBJECT_CHOICES)
    
    def __str__(self):
        return self.name
    