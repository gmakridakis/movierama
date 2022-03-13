from django.urls import path

from movies import views, votes

urlpatterns = [
    path("add_movie", views.add_movie, name="add_movie"),
    path("add_vote", votes.add_vote, name="add_vote"),
    path("retract_vote", votes.retract_vote, name="retract_vote"),
]
