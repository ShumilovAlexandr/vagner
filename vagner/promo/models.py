from django.db import models


class PhotoNasa(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Название фото')
    image = models.ImageField(
        upload_to='image/',
        default=None,
        blank=False,
        null=False,
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['id']

