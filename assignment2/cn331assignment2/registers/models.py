from pickle import TRUE
from django.db import models
from multiprocessing import Semaphore
# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length=64,primary_key=TRUE)
    course_name = models.CharField(max_length=64)
    semester = models.CharField(max_length=64)
    year = models.CharField(max_length=64)
    seat = models.IntegerField(default=0)
    current_seat = models.IntegerField(default=0)
    q_status = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.course_id} : {self.course_name} : {self.current_seat} / {self.seat} : {self.q_status}"


class Student(models.Model):
    student_id = models.CharField(max_length=64,primary_key=TRUE)
    student_name = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.student_id} : {self.student_name}"


class Apply(models.Model):
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_apply")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_apply")

    def __str__(self):
        return f"{self.course} : {self.student}"

class Complete(models.Model):
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_complete")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_complete")

    def __str__(self):
        return f"{self.course} : {self.student}"