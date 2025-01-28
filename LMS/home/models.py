from django.db import models
from register.models import student_master
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=100)
    author=models.CharField(max_length=40)
    isbn_no=models.CharField(max_length=50,primary_key=True)

    def __str__(self):
        return self.book_name
class book_issue(models.Model):
    regd_no=models.ForeignKey(student_master,on_delete=models.CASCADE)
    isbn_no=models.ForeignKey(Book,on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now)
    approve=models.IntegerField(default=0)