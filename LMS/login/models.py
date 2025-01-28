from django.db import models

# Create your models here.
class admin_master(models.Model):
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.email