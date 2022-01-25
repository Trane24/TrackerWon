from django.views import generic

from .models import *


class IndexFile(generic.ListView):
    model = File
    template_name = "templates/main/main.html"

