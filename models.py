from django.db import models

# Create your models here.

class Contact(models.Model):
    service_type = [
        ('creat web','Create a website'),
        ('online ads','Create an advertisement'),
    ]

    username = models.CharField(max_length=50 , null=True , blank=True)
    email = models.CharField(max_length=50 , null=True , blank=True)
    service = models.CharField(max_length=15, choices = service_type , null=True , blank=True )
    text = models.CharField(max_length = 2000 , null=True , blank=True)
    def __str__(self):
      return self.username
    