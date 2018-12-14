from urllib.parse import quote

from django.shortcuts import render

from .models import Site, Song, Performance


def index(request):

    site_details = Site.objects.first()
    songs_to_display = Song.objects.order_by('display_order')[:site_details.number_of_songs_to_display]
    performances_to_display = Performance.objects.order_by('display_order')[:site_details.number_of_performances_to_display]

    for performance in performances_to_display:
        formatted_address = '+'.join(performance.venue_address.split())
        full_google_maps_url = "https://www.google.com/maps/place/" + formatted_address
        performance.google_maps_url = full_google_maps_url

    index_template = 'music/index.html'
    template_context = {
        'site_title': site_details.title,
        'about_me': site_details.about_me,
        'songs_to_display': songs_to_display,
        'performances_to_display': performances_to_display
    }

    return render(request, index_template, template_context)
