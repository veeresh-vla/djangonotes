from django.db import models

# Create your models here.
from django.urls import reverse
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    pages = models.IntegerField()
    price = models.FloatField()

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
