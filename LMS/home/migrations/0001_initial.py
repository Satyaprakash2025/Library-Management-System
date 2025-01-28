# Generated by Django 5.0.7 on 2024-08-27 09:58

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('book_name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=40)),
                ('isbn_no', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='book_issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('approve', models.IntegerField(default=0)),
                ('regd_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.student_master')),
                ('isbn_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.books')),
            ],
        ),
    ]
