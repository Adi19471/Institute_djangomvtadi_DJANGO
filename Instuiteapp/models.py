from django.db import models
from django.db.models.enums import Choices

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



class Contact(models.Model):

    Feedback_CHOICE = {
       ('python','Narayana'),
       ('ui','Python Narayan'),
       ('rest-api','Srinivas'),
       ('c','Jyothi'),
       ('django-doutes','DJANGO-ADI'),
       ('Englis','Ratnakumar'),

    }

    COURSE_DATA ={
        ('1','python'),
        ('2','ui'),
        ('3','rest-api'),
        ('4','c'),
        ('5','django-doutes'),
        ('6','English'),
   
    }
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    mobile_number = models.BigIntegerField()
    enquiry_data = models.TextField()
    doute_triner = models.CharField(choices=Feedback_CHOICE,max_length=150)
    doute_course = models.CharField(choices=COURSE_DATA,max_length=120)
    date_of_post = models.DateTimeField()


    def __str__(self) -> str:
        return self.doute_triner
    

