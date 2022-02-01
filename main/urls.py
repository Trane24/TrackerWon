from django.urls import path
from .views import *

urlpatterns = [
    path("", IndexFile.as_view(), name="main"),
    path("category/<str:slug>/", FileByCategory.as_view(), name="category"),
]
