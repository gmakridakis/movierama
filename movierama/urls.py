from django.contrib import admin
from django.urls import include, path

import movies
from movies.views import movies_list

urlpatterns = [
    path("movies/", include("movies.urls")),
    path("accounts/", include("accounts.urls")),
    path("admin/", admin.site.urls),
    path("movies/<int:user_id>/<str:order>", movies.views.movies_list, name="index"),
    path("movies/<int:user_id>", movies.views.movies_list, name="index"),
    path("movies/<str:order>", movies.views.movies_list, name="index"),
    path("movies", movies.views.movies_list, name="index"),
]
