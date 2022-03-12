from django.shortcuts import redirect, render

from movies.models import Movie


def index(request):
    movies = Movie.objects.all().order_by("-date_added")
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
