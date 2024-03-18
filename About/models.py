from django.db import models


class Backround_image(models.Model):
    image = models.ImageField(upload_to='Backround_image/%Y/%m/%d')

    class Meta:
        verbose_name = 'Backround_image'
        verbose_name_plural = 'Backround_images'

class About_model(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    text = models.TextField(max_length=255)


    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'About_model'
        verbose_name_plural = 'About_models'