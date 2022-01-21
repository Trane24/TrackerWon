from django.shortcuts import render


def index(request):
    """main = main.objects.all()
    context = [

    ]"""
    return render(request, "main/main.html", context=context)
