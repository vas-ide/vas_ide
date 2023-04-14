
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView





# class Leo(View):
#     def get(self, request):
#         ip = request.META.get("REMOTE_ADDR")
#         return render(request, "leo.html", {})
def monday(request):
    return HttpResponse("Сделать КТ, Погулять с ребенком.")

def tuesday(request):
    return HttpResponse("Узнать результаты КТ, Поехать в Ростов.")