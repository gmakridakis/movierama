from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1256, blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.title
