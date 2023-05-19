from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Min, Max, Count, Avg, Value
from .models import Movie, Director, Actor


def show_all_movies(request):
    movies = Movie.objects.all()

    for slug in movies:
        slug.save()

    content = {
        # 'movies': Movie.objects.all(),
        # 'movies': Movie.objects.order_by('name'),
        # 'movies': Movie.objects.order_by('-rating', 'budget'),
        # 'movies': Movie.objects.order_by('-name')[:5],
        # 'movies': Movie.objects.order_by(F('budget').asc()),
        # 'movies': Movie.objects.order_by(F('budget').desc(nulls_last=True)),
        # 'movies': Movie.objects.order_by(F('budget').desc(nulls_first=True)),
        'movies': Movie.objects.annotate(
            # true_bool=Value(True),
            # false_bool=Value(False),
            # string_annotate=Value('Movie'),
            # int_annotate=Value('8654'),
            rub_budget=F('budget') * 75
        ),
        'total_and_max': movies.aggregate(Avg('budget'), Avg('rating'), Count('id'))
    }
    return render(request, "movie_app/all_movies.html", content)


def show_one_movie(request, slug_movie: str):
    error404 = get_object_or_404(Movie, slug=slug_movie)
    content = {
        'movies': Movie.objects.all(),
        'movie': Movie.objects.get(slug=slug_movie),
    }
    return render(request, "movie_app/one_movie.html", content)


# django-debug_toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/index.html


def show_all_directors(request):
    directors = Director.objects.all()
    content = {
        'directors': Director.objects.all(),
    }
    return render(request, "movie_app/all_directors.html", content)


def show_one_director(request, slug_director: str):
    error404 = get_object_or_404(Director, slug=slug_director)
    content = {
        'directors': Director.objects.all(),
        'director': Director.objects.get(slug=slug_director),
    }
    return render(request, "movie_app/one_director.html", content)

def show_all_actors(request):
    actors = Actor.objects.all()
    content = {
        'actors': Actor.objects.all(),
    }
    return render(request, "movie_app/all_actors.html", content)


def show_one_actor(request, slug_actor: str):
    error404 = get_object_or_404(Actor, slug=slug_actor)
    content = {
        'directors': Actor.objects.all(),
        'director': Actor.objects.get(slug=slug_actor),
    }
    return render(request, "movie_app/one_actor.html", content)
