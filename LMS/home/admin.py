from django.contrib import admin
from .models import Book, book_issue
# Register your models here.

admin.site.register(Book)
admin.site.register(book_issue)
