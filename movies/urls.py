from django.urls import path

from movies import views

urlpatterns = [path("add_movie", views.add_movie, name="add_movie")]
