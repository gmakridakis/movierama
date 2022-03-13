from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

SECONDS_TO_HOURS = 3600
MINUTES_TO_HOURS = 60


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1256, blank=True)
    date_added = models.DateTimeField(default=now)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title

    @property
    def age(self) -> str:
        movie_age = now() - self.date_added
        if movie_age.days:
            return f"{movie_age.days} days ago"
        elif int(movie_age.seconds / SECONDS_TO_HOURS):
            return f"{int(movie_age.seconds/SECONDS_TO_HOURS)} hours ago"
        elif int(movie_age.seconds / MINUTES_TO_HOURS):
            return f"{int(movie_age.seconds / MINUTES_TO_HOURS)} minutes ago"
        else:
            return "Just now"


class Vote(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_upvote = models.BooleanField()

    class Meta:
        unique_together = ("movie", "user")
