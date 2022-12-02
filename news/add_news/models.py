from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Articles(models.Model):
    STATUS_CHOICES = [
        ('T', 'True'),
        ('F', 'False'),
    ]
    title = models.CharField(max_length=100, verbose_name='Заголовок статьи')
    anons = models.CharField(max_length=250, verbose_name='Анонс')
    text_news = models.TextField(max_length=2000, verbose_name='Текст новости')
    date_add = models.DateTimeField(verbose_name='Дата публикации')
    update_date = models.DateTimeField(verbose_name='Дата редактирования')
    activity = models.BooleanField(default=True)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='a')

    def __str__(self):
        return self.title


    def get_absolute_url(self): return reverse('detail_news', kwargs={'pk': self.pk})
    #def get_absolute_url(self):
    #    return reverse('news_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comments(models.Model):
    STATUS_CHOICES = [
        ('a', 'activity'),
        ('d', 'delete'),
    ]
    username = models.CharField(max_length=20, verbose_name='Имя')
    text_comment = models.TextField(verbose_name='Комментарий')
    news = models.ForeignKey('Articles', null=True, on_delete=models.CASCADE, verbose_name='Новость',
                             related_name='comment_news')
    #user = models.ForeignKey('Articles', null=True, on_delete=models.CASCADE,
    #                         related_name='user')
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, null=True, blank=True, verbose_name='имя')
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='a')


    def __str__(self):
        return self.text_comment

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


