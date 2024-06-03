from django.core.cache import cache
from django.conf import settings
from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    count_views = models.PositiveIntegerField()
    position = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if cache.get(settings.ADVERTISEMENT_CACHE):
            cache.delete(settings.ADVERTISEMENT_CACHE)

        return super().save(*args, **kwargs)
