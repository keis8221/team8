from django.db import models

class Teacher(models.Model):
    subject_id = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=128)
    teacher_id = models.CharField(max_length=10)
    teacher_name = models.CharField(max_length=20)
    start_time = models.TimeField()
    finish_time = models.TimeField()
    attend_time = models.IntegerField()
    late_time = models.IntegerField()
    password = models.CharField(max_length=128)

# Create your models here.
