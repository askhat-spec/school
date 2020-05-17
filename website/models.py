from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    descriptions = models.CharField(max_length=400, verbose_name='Краткое описание')
    cover = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='Картинка')
    publish = models.DateTimeField(verbose_name='Дата публикации')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug':self.slug})    


class Timetable(models.Model):
    grade =  models.CharField(max_length=30, verbose_name='Класс')
    slug = models.SlugField(max_length=30, unique=True, verbose_name='ID')
    cover = models.ImageField(upload_to='timetable/%Y/%m/', verbose_name='Картинка')
    
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписании'

    def __str__(self):
        return self.grade


class Teachers(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    place = models.CharField(max_length=300, verbose_name='Должность')
    cover = models.ImageField(upload_to='teachers/%Y/%m', verbose_name='Фото')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
    
    def __str__(self):
        return self.name


class Awards(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    medalist = models.CharField(max_length=600, verbose_name='Достижении')
    cover = models.ImageField(upload_to='awards/%Y/%m', verbose_name='Фото')

    class Meta:
        verbose_name = 'Призёр'
        verbose_name_plural = 'Призёры'
    
    def __str__(self):
        return self.name