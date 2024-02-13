from django.db import models

# Create your models here.

class News(models.Model):
    title=models.CharField(max_length=150, verbose_name='Заголовок')
    content=models.TextField(blank=True, verbose_name='Содержимое')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at=models.DateTimeField(auto_now=True)
    photo=models.ImageField(upload_to='media/%Y/%m/%d',verbose_name='Фото')
    is_published=models.BooleanField(default=True, verbose_name='Опубликовано')
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering=['-created_at']

class Human(models.Model):
    fname=models.CharField(max_length=20, verbose_name='Имя')
    lname=models.CharField(max_length=20, verbose_name='Фамилия')
    hage=models.IntegerField(verbose_name='Возраст')
    passp=models.CharField(max_length=15, blank=False)
    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering=['hage']

