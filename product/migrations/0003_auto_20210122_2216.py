# Generated by Django 3.1.5 on 2021-01-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210121_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapCoordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_coordinate', models.CharField(max_length=255, verbose_name='Первый координат карты')),
                ('second_coordinate', models.CharField(max_length=255, verbose_name='Первый координат карты')),
            ],
        ),
        migrations.AlterField(
            model_name='animation',
            name='photo',
            field=models.ImageField(upload_to='photo/', verbose_name='Фото'),
        ),
    ]