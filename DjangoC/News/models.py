from django.db import models

# Create your models here.

class News(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    photo=models.ImageField(upload_to='media/%Y/%m/%d')
    is_published=models.BooleanField(default=True)

class Human(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    hage=models.IntegerField()
    passp=models.CharField(max_length=100, blank=False)