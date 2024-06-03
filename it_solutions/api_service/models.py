from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    count_views = models.PositiveIntegerField()
    position = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title
