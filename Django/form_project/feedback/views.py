from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm

def index(request):
    form = FeedbackForm()
    context = {
        "form": form,
    }
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        # name = request.POST['name']
        # if len(name) == 0:
        #     return render(request, "feedback/feedback.html", context)
        # print(name)
            return HttpResponseRedirect("/done")
        form = FeedbackForm()
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