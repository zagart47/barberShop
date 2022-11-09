from django.db import models
from django.urls import reverse


class Barber(models.Model):
    barber_name = models.CharField(max_length=25, db_index=True, verbose_name='Имя')
    content = models.TextField(verbose_name='Описание')
    grade = models.CharField(max_length=25, verbose_name='Категория барбера')
    clients_count = models.IntegerField(default=0, verbose_name='Всего клиентов')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.barber_name

    def get_absolute_url(self):
        return reverse('barberdetails', kwargs={'barber_id': self.id})  ##определение метода для возврата ссылки

    class Meta:
        verbose_name = 'Барбер'
        verbose_name_plural = 'Барберы'
        ordering = ['id']


class Client(models.Model):
    client_name = models.CharField(max_length=25, db_index=True, verbose_name='Имя')
    visits_count = models.IntegerField(default=0, verbose_name='Число посещений')
    phone = models.IntegerField(null=True, verbose_name='Номер телефона')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['id']


class Visit(models.Model):
    client = models.ForeignKey('Client', on_delete=models.PROTECT, null=True, verbose_name='Имя клиента')
    barber = models.ForeignKey('Barber', on_delete=models.PROTECT, null=True, verbose_name='Имя барбера')
    visit_time = models.DateTimeField(null=True, verbose_name='Дата и время визита в формате: 2022-12-24 17:00:00')

    def __str__(self):
        return self.barber, self.client, self.visit_time

    class Meta:
        verbose_name = 'Посещение клиента'
        verbose_name_plural = 'Посещения клиентов'
        ordering = ['id']
