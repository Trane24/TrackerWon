from django.urls import path
from .views import *

urlpatterns = [
    path("", IndexFile.as_view(), name="main"),
    path("category/<str:slug>/", FileByCategory.as_view(), name="category"),
    path("category/<str:slug>/<int:file_id>/", ShowFile.as_view(), name="file"),
    path("create_file/", CreateFile.as_view(), name="create_file"),
]
