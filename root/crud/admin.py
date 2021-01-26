from django.contrib import admin
from .models import Book, Site


class SitesInline(admin.TabularInline):
    model = Site
    extra = 3


class BookAdmin(admin.ModelAdmin):
    inlines = [SitesInline]


admin.site.register(Book, BookAdmin)
admin.site.register(Site)
