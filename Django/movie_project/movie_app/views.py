from django.shortcuts import render

from .models import Movie

def show_all_movies(request):
    content = {
        'movies': Movie.objects.all()
    }
    return render(request, "movie_app/all_movies.html", content)




