from django.urls import path
from .views import *

urlpatterns = [
    path("create_file/", CreateFile.as_view(), name="create_file"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("<str:slug>/<int:file_id>/", ShowFile.as_view(), name="file"),
    path("<str:slug>/", FileByCategory.as_view(), name="category"),
    path("", IndexFile.as_view(), name="main"),
]
