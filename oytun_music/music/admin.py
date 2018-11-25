from django.contrib import admin

from music.models import Site, Song, Performance


admin.site.register([Site, Song, Performance])