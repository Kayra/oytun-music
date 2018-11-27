from django.shortcuts import render

from .models import Site, Song, Performance


def index(request):

    site_details = Site.objects.first()
    last_five_songs = Song.objects.order_by('order')[:site_details.number_of_songs_to_list]
    last_five_performances = Performance.objects.order_by('order')[:site_details.number_of_performances_to_list]

    index_template = 'music/index.html'
    template_context = {
        'site_title': site_details.title,
        'about_me': site_details.about_me,
        'last_five_songs': last_five_songs,
        'last_five_performances': last_five_performances
    }

    return render(request, index_template, template_context)
