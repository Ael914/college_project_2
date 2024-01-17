# -*- coding: utf-8 -*-

from modeltranslation.translator import TranslationOptions, register

from .models import Course, Module, Subject


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ("title", "overview")


@register(Subject)
class SubjectTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(Module)
class ModuleTranslationOptions(TranslationOptions):
    fields = ("title", "description")
