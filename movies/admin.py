from django.contrib import admin

from movies.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    list_filter = ("title", "description")
    list_display_links = ["title"]
    list_editable = ["description"]
    search_fields = ("title", "description")
    list_per_page = 20


admin.site.register(Movie, MovieAdmin)
