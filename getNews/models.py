from django.db import models


# Create your models here.
class Source(models.Model):
    source_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    category = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    urlsToLogos_small = models.CharField(max_length=1000)
    urlsToLogos_medium = models.CharField(max_length=1000)
    urlsToLogos_large = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class News(models.Model):
    author = models.CharField(max_length=1000, null=True, blank=True)
    title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    url = models.CharField(max_length=1000, null=True, blank=True)
    urlToImage = models.CharField(max_length=1000, null=True, blank=True)
    publishedDate = models.DateTimeField('Published Date', null=True, blank=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
