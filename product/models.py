from django.db import models

# Create your models here.

class post(models.Model):
    title=models.CharField(max_length=255, verbose_name='Заголовок')
    photo=models.ImageField(upload_to='photo', verbose_name='Слайдер')
    text=models.TextField(verbose_name='Текст')
    name_productions=models.CharField(max_length=255, verbose_name='Продукты')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'


