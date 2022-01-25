from django.views import generic

from .models import *


class IndexListFiles(generic.ListView):
    model = File
    template_name = "templates/main/main.html"

