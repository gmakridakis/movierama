from django.db import IntegrityError
from django.shortcuts import redirect

from movies.models import Movie, Vote


def add_vote(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        movie_id = request.POST["movie_id"]
        is_upvote = request.POST["is_upvote"]

        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            print(f"There is no movie with ID {movie_id}")
            # messages.error(request, "Cannot find the requested movie")
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


def retract_vote(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        movie_id = request.POST["movie_id"]
        is_upvote = request.POST["is_upvote"]

        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            print(f"There is no movie with ID {movie_id}")
            # messages.error(request, "Cannot find the requested movie")
            return redirect(request.META["HTTP_REFERER"])

        try:
            vote = Vote.objects.get(user_id=user_id, movie_id=movie_id, is_upvote=is_upvote)
            if is_upvote == "True":
                movie.upvotes -= 1
            else:
                movie.downvotes -= 1
            vote.delete()
            movie.save()
        except Vote.DoesNotExist:
            print(f"User with ID {user_id} has not voted for movie with ID {movie_id}")
            # messages.error(request, "You have not voted for this movie")
            return redirect(request.META["HTTP_REFERER"])

    return redirect(request.META["HTTP_REFERER"])
