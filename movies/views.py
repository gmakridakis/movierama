from django.shortcuts import render

from movies.models import Movie


def index(request):
    movies = Movie.objects.all().order_by("-date_added")
    context = {"movies": movies}
    return render(request, "movies/index.html", context)
