# postkon/postkon_webapp/models.py
'''
Данный модуль описывает модели, используемые в проекте в качестве сущностей, данные о которых хранятся в БД.

Архаров Никита Михайлович
arharov.n@edu.narfu.ru
'''
from distutils.command.upload import upload
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.urls import reverse


class User(models.Model):
    '''
    Данный класс предстваляет собой модель пользователя сайта.
    
    :param models.Model: класс фреймворка Django, описывающий модель. Каждый атрибут модели представляет поле базы данных.
    :type models.Model: <class 'django.db.models.base.ModelBase'>   
    '''
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    avatar_img = models.ImageField(upload_to='images_uploaded', null=True)
    slug = models.SlugField(default='', null=False, db_index=True)

    def get_url(self):
         '''
         Функция возвращает url пользователя на основе slug записи его username

         :return: str
         '''
        return reverse('one_user', args=[self.slug])

    def get_settings_url(self):
        return reverse('user_settings', args=[self.slug])

    def __str__(self):
         '''
         Функция переопределяет магический метод __str__ для читабельного строчного отображения экземпляра класса.
         '''
        return f'{self.username}'


class Post(models.Model):
    '''
    Данный класс предстваляет собой модель поста на сайте.
    :param models.Model: класс фреймворка Django, описывающий модель. Каждый атрибут модели представляет поле базы данных.
    :type models.Model: <class 'django.db.models.base.ModelBase'>   
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_uploaded = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=500)

    def __str__(self):
         '''
         Функция переопределяет магический метод __str__ для читабельного строчного отображения экземпляра класса.
         '''
        return f'{self.user.username} - {self.date_uploaded}'
