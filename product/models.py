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
    product_photo=models.ImageField(upload_to='photo/product',verbose_name='Фото продукта')
    spisok=models.ForeignKey(spisok, on_delete=models.CASCADE, verbose_name='Перечень списка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'



