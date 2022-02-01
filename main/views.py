from django.urls import reverse_lazy
from django.views import generic

from .forms import AddPostForm
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


class ShowFile(generic.DetailView):
    model = File
    template_name = "main/post.html"
    pk_url_kwarg = "file_id"
    context_object_name = "file"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowFile, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class CreateFile(generic.CreateView):
    form_class = AddPostForm
    template_name = "main/create_file.html"
    success_url = reverse_lazy("main")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CreateFile, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context