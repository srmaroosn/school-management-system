

from django.db import models

# Create your models here.
class Book(models.Model):
    name= models.CharField(max_length=220)
    author= models.CharField(max_length=220)
    date_of_borrowed= models.DateField()
    No_of_pages= models.IntegerField()
    
    def __str__(self):
        return self.name
   
