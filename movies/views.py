from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from movies.models import Movie

ORDER_OPTIONS = {
    "date": ["-date_added", "-upvotes", "downvotes"],
    "likes": ["-upvotes", "downvotes", "-date_added"],
    "hates": ["-downvotes", "upvotes", "-date_added"],
}


def movies_list(request, user_id=None, order="date"):
    if order not in ORDER_OPTIONS.keys():
        print(f"Invalid order option: {order}")
        messages.error(request, f"Invalid order option")
        return HttpResponseRedirect(reverse("index"))
    movies = Movie.objects.all()
    current_url = "/movies"

    if user_id:
        movies = movies.filter(user_id=user_id)
        current_url = f"{current_url}/{user_id}"

    movies = movies.order_by(ORDER_OPTIONS[order][0], ORDER_OPTIONS[order][1], ORDER_OPTIONS[order][2])
    context = {"movies": movies, "current_url": current_url}
    return render(request, "movies/index.html", context)


def add_movie(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        user_id = request.POST["user_id"]

        if user_id == "None":
            return HttpResponseRedirect(reverse("index"))

        if Movie.objects.filter(title=title).exists():
            print(f"There is already a movie with title: {title}")
            messages.error(request, f"There is already a movie with title: {title}")
            return HttpResponseRedirect(reverse("add_movie"))
        movie = Movie.objects.create(title=title, description=description, user_id=user_id)
        movie.save()

        print(f'Movie "{title}" added')
        messages.success(request, f'Your movie "{title}" has been registered to Movierama!')
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "movies/add_movie.html")
