# Generated by Django 3.0.3 on 2020-05-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20200318_1543'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',), 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.RemoveField(
            model_name='awards',
            name='medalist_en',
        ),
        migrations.RemoveField(
            model_name='awards',
            name='medalist_kk',
        ),
        migrations.RemoveField(
            model_name='awards',
            name='medalist_ru',
        ),
        migrations.RemoveField(
            model_name='awards',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='awards',
            name='name_kk',
        ),
        migrations.RemoveField(
            model_name='awards',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='post',
            name='descriptions_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='descriptions_kk',
        ),
        migrations.RemoveField(
            model_name='post',
            name='descriptions_ru',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_kk',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='name_kk',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='place_en',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='place_kk',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='place_ru',
        ),
        migrations.AlterField(
            model_name='timetable',
            name='cover',
            field=models.ImageField(null=True, upload_to='timetable/%Y/%m/', verbose_name='Картинка'),
        ),
    ]
