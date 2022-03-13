from django.contrib import admin
from django.urls import include, path

import movies
from movies.views import index

urlpatterns = [
    path("movies/", include("movies.urls")),
    path("accounts/", include("accounts.urls")),
    path("admin/", admin.site.urls),
    path("movies", movies.views.index, name="index"),
    path("movies/<str:order>", movies.views.index, name="index"),
]
