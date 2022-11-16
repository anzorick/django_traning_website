from django.db import models

# Create your models here.
class TeleSetings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')