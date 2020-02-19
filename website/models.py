from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    descriptions = models.CharField(max_length=400, verbose_name='Краткое описание')
    cover = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='Картинка')
    publish = models.DateField(verbose_name='Дата публикации')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug':self.slug})    