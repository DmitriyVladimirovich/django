from django.db import models

class Human(models.Model):
    fname=models.CharField(max_length=20, verbose_name='Имя')
    lname=models.CharField(max_length=20, verbose_name='Фамилия')
    hage=models.IntegerField(verbose_name='Возраст')
    passp=models.CharField(max_length=15, blank=False, verbose_name='Паспорт')
    profs = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True, verbose_name='Профессия')
    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering=['hage']

class Profession(models.Model):
    title=models.CharField(max_length=30, db_index=True, verbose_name='Профессия')
    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        ordering=['title']