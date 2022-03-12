from django import template

from movies.models import Movie, Vote

register = template.Library()


@register.filter
def get_users_votes(user, movie):
    print(f"user: {user}, movie: {movie}")
    if not user.is_authenticated:
        return None

    try:
        return Vote.objects.get(user=user, movie=movie).is_upvote
    except Vote.DoesNotExist:
        return None
