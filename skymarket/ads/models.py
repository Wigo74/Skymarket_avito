from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название товара")
    price = models.PositiveIntegerField(verbose_name="Цена товара")
    description = models.CharField(blank=True, null=True, max_length=1000, verbose_name="Описание товара")
    image = models.ImageField(
        upload_to="images/",
        verbose_name="фото",
        null=True,
        blank=True,
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               verbose_name="Автор объявления",
                               related_name='ad',
                               on_delete=models.CASCADE,
                               )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания объявления",)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']


class Comment(models.Model):
    text = models.TextField(max_length=1000, verbose_name="Комментарий",)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               verbose_name="Автор комментария",
                               related_name='comment',
                               on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, related_name='comments', verbose_name="Объявление", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания комментария")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ('-created_at',)
