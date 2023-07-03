from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    salary = models.CharField(max_length=10, blank=True, null=None)
    address= models.CharField(max_length=100, blank=True, null=None)  
 

# Create your models here.
