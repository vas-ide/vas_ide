from django.shortcuts import render

from youapp.models import Worker


def index_page(request):

    all_workers = Worker.objects.all()


    return render(request, "index.html")