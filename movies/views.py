from django.db import IntegrityError
from django.shortcuts import redirect, render

from movies.models import Movie, Vote


def index(request):
    movies = Movie.objects.all().order_by("-date_added")
    context = {"movies": movies}
    return render(request, "movies/index.html", context)


def user_movies(request, user_id):
    movies = Movie.objects.filter(user_id=user_id).order_by("-date_added")
    votes = Vote.objects.filter(movie__in=movies)
    context = {"movies": movies}
    return render(request, "movies/index.html", context)


def add_movie(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        user_id = request.POST["user_id"]

        if Movie.objects.filter(title=title).exists():
            print(f"There is already a movie with title: {title}")
            # messages.error(request, f"There is already a movie with title: {title}")
            return redirect("add_movie")

        movie = Movie.objects.create(title=title, description=description, user_id=user_id)
        movie.save()

        print(f'Your movie "{title}" has been registered to Movierama!')
        # messages.success(request, f"Your movie \"{title}\" has been registered to Movierama!")

        return redirect("index")

    else:
        return render(request, "movies/add_movie.html")


def add_vote(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        movie_id = request.POST["movie_id"]
        is_upvote = request.POST["is_upvote"]

        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            print(f"User with ID {user_id} has already voted for movie with ID {movie_id}")
            # messages.error(request, "You have already voted for this movie")
            return redirect(request.META["HTTP_REFERER"])

        try:
            vote = Vote.objects.create(user_id=user_id, movie_id=movie_id, is_upvote=is_upvote)
            if is_upvote == "True":
                movie.upvotes += 1
            else:
                movie.downvotes += 1
            vote.save()
            movie.save()
        except IntegrityError:
            print(f"User with ID {user_id} has already voted for movie with ID {movie_id}")
            # messages.error(request, "You have already voted for this movie")
            return redirect(request.META["HTTP_REFERER"])

    return redirect(request.META["HTTP_REFERER"])
