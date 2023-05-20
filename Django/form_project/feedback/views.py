from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "feedback/feedback.html", context)
