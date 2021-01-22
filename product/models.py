from django.db import models

# Create your models here.
from django.urls import reverse
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title=models.CharField(blank=True,max_length=255, verbose_name='Заголовок')
    text=models.TextField(blank=True,verbose_name='Текст')
    name_productions=models.CharField(blank=True,max_length=255, verbose_name='Продукты')
    created_date = models.DateTimeField(blank=True,default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'

class Animation(models.Model):
    photo=models.ImageField(upload_to='photo/', verbose_name='Фото')

    def get_absolute_url(self):
        return reverse('delete_photo', kwargs={'pk':self.pk})


class spisok(models.Model):
    title=models.CharField(max_length=255, verbose_name='Заголовок списка')
    text=models.TextField(verbose_name='Текст спика')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'


class product(models.Model):
    title_number=models.CharField(max_length=255, verbose_name='Номер продукта')
    product_name=models.CharField(max_length=255, verbose_name='Наименование продукта')
    product_photo=models.ImageField(upload_to='photo/',verbose_name='Фото продукта')
    spisok=models.ManyToManyField(spisok,  verbose_name='Перечень списка')
    created_date = models.DateTimeField(blank=True,default=timezone.now)

    def __str__(self):
        return self.title_number

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class MapCoordinates(models.Model):
    first_coordinate=models.CharField(max_length=255, verbose_name='Первый координат карты')
    second_coordinate=models.CharField(max_length=255, verbose_name='Первый координат карты')

