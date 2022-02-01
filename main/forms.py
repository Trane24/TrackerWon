from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = File
        fields = "__all__"
