from django.db import models

# Create your models here.
class student_master(models.Model):
    name=models.CharField(max_length=30)
    regd_no=models.AutoField(primary_key=True)
    branch=models.CharField(max_length=20)
    year=models.CharField(max_length=5)
    sec=models.CharField(max_length=5)
    mob=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name
