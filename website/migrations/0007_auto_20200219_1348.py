# Generated by Django 3.0.3 on 2020-02-19 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20200218_2330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',), 'verbose_name': 'Новости', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='post',
            name='descriptions',
            field=models.CharField(max_length=400, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]
