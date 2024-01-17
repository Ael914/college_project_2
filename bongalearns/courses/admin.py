from django.contrib import admin
from modeltranslation.admin import (
    TranslationAdmin,
    TranslationStackedInline,
)

# from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from .models import Course, Module, Subject


# Register your models here.
@admin.register(Subject)
class SubjectAdmin(TranslationAdmin):
    list_display = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}


class ModuleInline(TranslationStackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    list_display = ["title", "subject", "created"]
    list_filter = ["created", "subject"]
    search_fields = ["title", "overview"]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ModuleInline]
