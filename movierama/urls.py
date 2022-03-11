from django.contrib import admin
from django.urls import include, path

import movies

urlpatterns = [
    path("movies", include("movies.urls")),
    path("admin/", admin.site.urls),
    path("", movies.views.index, name="index"),
]
