from django.db import models

# Create your models here.


class CourseDetailes(models.Model):
    course_name = models.CharField(max_length=100)
    course_fees = models.IntegerField()
    start_time = models.DateField()
    duration = models.CharField(max_length=100)
    triner_name = models.CharField(max_length=100)
    triner_experiecnce = models.CharField(max_length=120)
    Institute_Address = models.CharField(max_length=100)
    profiles = models.ImageField(upload_to=None ,blank=True, null=True)
    
    def __str__(self):
        return self.course_name