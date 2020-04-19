from django.db import models

# Create your models here.

# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
import uuid

SIZES = (('Маленького размера', 'small'), ('Среднего размера', 'medium'), ('Крупного размера', 'large'),)

UNITS = (('мес.', 'month'), ('г.', 'year'),)

HAIR = (('короткая шерсть', 'short'), ('длинная шерсть', 'long'), ('без шерсти', 'hairless'),)

SEX = (('М', 'boy'), ('Ж', 'girl'),)

BREEDS = (('Метис', 'mongrel'),
          ('Йоркширский терьер', 'york'),
          ('Такса', 'taksa'),
          ('Лабрадор-ретривер', 'labritriever'),
          ('Чихуахуа', 'chihuahua'),
          ('Пудель', 'poodle'),
          ('Бишон', 'bishon'),)

class DogBreed(models.Model):

    name = models.CharField(default="",  max_length=40)
    desc = models.TextField(default="Perfect breed for..", max_length=5000)
    photo = models.URLField(blank=True, max_length=500)
    size = models.CharField(max_length=30, choices=SIZES, default='Среднего размера')
    hair = models.CharField(max_length=50, choices=HAIR, default='короткая шерсть')
    country = models.CharField(max_length=50,  default='')
    number = models.IntegerField(blank=True,  null=True)


class Kennel(models.Model):

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=50, blank=True)
    breeds = models.ManyToManyField(DogBreed, related_name='kennel_breeds')
    about = models.CharField(verbose_name="О нас", max_length=1000, default="")
    photo = models.URLField(blank=True, max_length=500)
    city = models.CharField(default="", max_length=50, blank=True)


class Dog(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, default="Малыш")
    sex = models.CharField(max_length=50, choices=SEX, default='Ж')
    size = models.CharField(max_length=30, choices=SIZES, default='Среднего размера', null=True)
    age = models.IntegerField(blank=True, null=True, default=0)
    units = models.CharField(max_length=30, choices=UNITS, default='Год')
    photo = models.URLField(blank=True, max_length=500, default='', null=True)
    hair = models.CharField(max_length=50, choices=HAIR, default='короткая шерсть', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    breed = models.CharField(choices=BREEDS, max_length=50, blank=True, null=True)
    kennel = models.ForeignKey(Kennel, on_delete=models.CASCADE, null=True)


class Ad(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE,  null=True)
    kennel = models.ForeignKey(Kennel, on_delete=models.CASCADE,null=True)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1000, blank=True, default="")
    price = models.IntegerField(blank=True)

    class Meta:
        ordering = ('created_at',)
