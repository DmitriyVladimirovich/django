from django.db import models
from django.urls import reverse_lazy


class Human(models.Model):
    fname=models.CharField(max_length=20, verbose_name='Имя')
    lname=models.CharField(max_length=20, verbose_name='Фамилия')
    hage=models.IntegerField(verbose_name='Возраст')
    passp=models.CharField(max_length=15, blank=False, verbose_name='Паспорт')
    profs = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True, verbose_name='Профессия')

    def get_absolute_url(self):
        return reverse_lazy('view_human',kwargs={'human_id':self.pk})

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering=['hage']

class Profession(models.Model):
    title=models.CharField(max_length=30, db_index=True, verbose_name='Профессия')

    def get_absolute_url(self):
        return reverse_lazy('Profession',kwargs={'profession_id':self.pk})

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        ordering=['title']