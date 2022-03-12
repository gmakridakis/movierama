from django.contrib import admin

from movies.models import Movie, Vote


class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "upvotes", "downvotes")
    list_filter = ("title", "description")
    list_display_links = ["title"]
    list_editable = ("description", "upvotes", "downvotes")  # TODO: remove upvotes & downvotes from editable
    search_fields = ("title", "description")
    list_per_page = 20


admin.site.register(Movie, MovieAdmin)


class VoteAdmin(admin.ModelAdmin):
    list_display = ("user", "movie", "vote")
    list_filter = ("user", "movie")
    list_display_links = ("user", "movie")
    search_fields = ("user", "movie")
    list_per_page = 20

    def vote(self, obj):
        if obj.is_upvote:
            return "Like"
        return "Hate"

    def has_add_permission(self, request):
        return False


admin.site.register(Vote, VoteAdmin)
