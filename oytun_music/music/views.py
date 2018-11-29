from django.shortcuts import render

from .models import Site, Song, Performance


def index(request):

    site_details = Site.objects.first()
    songs_to_display = Song.objects.order_by('order')[:site_details.number_of_songs_to_list]
    performances_to_display = Performance.objects.order_by('order')[:site_details.number_of_performances_to_list]

    index_template = 'music/index.html'
    template_context = {
        'site_title': site_details.title,
        'about_me': site_details.about_me,
        'songs_to_display': songs_to_display,
        'performances_to_display': performances_to_display
    }

    return render(request, index_template, template_context)
