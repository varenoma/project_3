from django.db import models

# Create your models here.
class StudentDb(models.Model):
    full_name = models.CharField(max_length=150)
    grade = models.IntegerField()
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'student'