from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1256, blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title


class Vote(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_upvote = models.BooleanField()

    class Meta:
        unique_together = ("movie", "user")
