from django.contrib import admin
from .models import Catalogo


@admin.register(Catalogo)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "description", "author", "pub_date", "posted", "updated",)
