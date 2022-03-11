from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1256, blank=True)
    date_added = models.DateField(default=datetime.now)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.title
