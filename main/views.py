from django.shortcuts import render
from django.views import generic

from .models import *


class IndexFile(generic.ListView):
    template_name = "main/main.html"
    context_object_name = "file"
    queryset = File.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexFile, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class FileByCategory(generic.ListView):
    template_name = "main/main.html"
    context_object_name = "file"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FileByCategory, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

    def get_queryset(self):
        slug = self.kwargs["slug"]
        return File.objects.filter(category__slug=slug, is_published=True)
