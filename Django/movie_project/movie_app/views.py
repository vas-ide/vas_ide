from django.shortcuts import render, get_object_or_404

from .models import Movie


def show_all_movies(request):
    movies = Movie.objects.all()
    for slug in movies:
        slug.save()

    content = {
        'movies': Movie.objects.all(),
    }
    return render(request, "movie_app/all_movies.html", content)


def show_one_movie(request, slug_movie: str):
    error404 = get_object_or_404(Movie, slug=slug_movie)
    content = {
        'movies': Movie.objects.all(),
        'movie': Movie.objects.get(slug=slug_movie),
    }
    return render(request, "movie_app/one_movie.html", content)
