from django.db import models


# Create your models here.
class Book(models.Model):
    Title = models.CharField(max_length=100, verbose_name='タイトル')
    Author = models.CharField(max_length=50, verbose_name='著者')
    Category = models.CharField(max_length=50, verbose_name='カテゴリ')
    Registration_date = models.DateField(verbose_name='登録日')

    class Meta:
        verbose_name = '本'
        verbose_name_plural = '本'

    def __str__(self):
        return self.Title
