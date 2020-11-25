from django.db import models
from .utils.path_generator import ShortPath

class UrlMappings(models.Model):
    short_path = models.CharField(max_length=ShortPath.path_length)
    original_url = models.URLField("URL", unique=True)

    def __str__(self):
        return "%s => %s" % (self.original_url, self.short_path)