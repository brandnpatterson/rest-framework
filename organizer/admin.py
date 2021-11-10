from django.contrib import admin

from .models import NewsLink, Startup, Tag

admin.site.register(NewsLink)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
