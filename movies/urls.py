from django.urls import path

from movies import views

urlpatterns = [
    path("add_movie", views.add_movie, name="add_movie"),
    path("user_movies/<int:user_id>", views.user_movies, name="user_movies"),
    path("add_vote", views.add_vote, name="add_vote"),
    path("retract_vote", views.retract_vote, name="retract_vote"),
]
