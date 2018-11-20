from django.db import models


class Site(models.Model):

    title = models.CharField(max_length=200)
    about_me = models.TextField()

    def __str__(self):
        return self.title
