from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    context = {}
    if request.method == "POST":
        name = request.POST['name']
        print(name)
        return HttpResponseRedirect("/done")
    return render(request, "feedback/feedback.html", context)

def done(request):
    return render(request, "feedback/done.html")



def hello(request):
    pass
#     name = request.GET["name"]
#     surname = request.GET["surname"]
#     login = request.GET["login"]
#     passwd = request.GET["passwd"]
#     feedback = request.GET["feedback"]
#     context = {
#         "name": name,
#         "surname": surname,
#         "login": login,
#         "passwd": passwd,
#         "feedback": feedback,
#     }
#     return render(request, "feedback/feedback.html", context)
    # return HttpResponseRedirect("/")