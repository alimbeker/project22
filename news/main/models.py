from tabnanny import verbose
from django.db import models
from .validators import file_size
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Sport(models.Model):
    name = models.CharField( max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    

class MenPrize(models.Model):
    fullnames = models.CharField(max_length=50)
    medaltype= models.CharField(max_length=50)

class Men(models.Model):
    fullname = models.CharField(max_length=50)
    photo = models.CharField(max_length=10000)
    text = models.CharField(max_length=10000)

class Women(models.Model):
    fullname = models.CharField(max_length=50)
    photo = models.CharField(max_length=10000)
    text = models.CharField(max_length=10000)




class Articles(models.Model):
    title = models.CharField('Name', max_length=250)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Statya')

    def get_absolute_url(self):
        return f'/news/{self.id}'


class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новость'


class Mvideo(models.Model):
    mcountry = models.CharField(max_length=50)
    mtext = models.TextField(max_length=5000)
    msportsmen=models.CharField(max_length=50)
    mcaption = models.CharField(max_length=100)
    mvideo = models.FileField(upload_to="video/%y", validators=[file_size])
    def __str__(self):
        return self.mcaption


