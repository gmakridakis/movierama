from django.contrib import admin
from django.urls import include, path

import movies
from movies.views import index

urlpatterns = [
    path("movies", include("movies.urls")),
    path("admin/", admin.site.urls),
    path("", movies.views.index, name="index"),
]
