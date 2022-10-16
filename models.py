from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 20)
    company_name = models.CharField(max_length = 20)
    phone_number = models.CharField(max_length = 20)
    Enquiry = models.CharField(max_length = 100, default=None,blank=True,null=True)


    def __Str__(self):
        return str(self.id)+" "+self.name

class Seller(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    Enquiry = models.CharField(max_length = 100,default=None,blank = True,null=True)

