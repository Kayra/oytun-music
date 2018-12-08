from django.db import models


class Site(models.Model):

    title = models.CharField(max_length=200)
    about_me = models.TextField(null=True, blank=True)
    number_of_songs_to_display = models.IntegerField(default=5)
    number_of_performances_to_display = models.IntegerField(default=5)

    def __str__(self):
        return self.title


class Song(models.Model):

    title = models.CharField(max_length=200)
    external_link = models.CharField(max_length=200)
    display_order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Performance(models.Model):

    venue_name = models.CharField(max_length=200)
    venue_address = models.CharField(max_length=400)
    start_time = models.DateTimeField(null=True, blank=True)
    external_link = models.CharField(max_length=200, null=True, blank=True)
    display_order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.venue_name
