from django.shortcuts import render



def show_all_movies(request):
    content = {


    }
    return render(request, "movie_app/all_movies.html", content)




