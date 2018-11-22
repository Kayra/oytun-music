from django.db import models


class Site(models.Model):

    title = models.CharField(max_length=200)
    about_me = models.TextField()

    def __str__(self):
        return self.title


class Song(models.Model):

    title = models.CharField(max_length=200)
    external_link = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Performance(models.Model):

    venue_name = models.CharField(max_length=200)
    venue_address = models.CharField(max_length=400)
    start_time = models.DateTimeField()
    external_link = models.CharField(max_length=200)

    def __str__(self):
        return self.venue_name
