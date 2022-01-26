from django.contrib import admin
from .models import *


@admin.register(File)
class FileAdmin(admin.ModelAdmin):  # Разобраться с генеральной категорией
    list_display = (
        "pk",
        "title",
        "category",
        "date_published",
        "date_updated",
        "is_published",
    )
    list_display_links = ("title", "pk")
    list_filter = ("category",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "general_category", "title")


@admin.register(GeneralCategory)
class GeneralCategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
