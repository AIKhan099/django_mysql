from django.db import models

# Create your models here.
class Courses(models.Model):
    course1= models.CharField(max_length=255)
    subject1= models.CharField(max_length=255)
    ratting1=models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return self.course1