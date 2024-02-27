from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def all_information(request):
    content = {

    }
    return render(request, "workshift/index.html", content)


# employee
def employee_information(request, employee_id):
    content = {
        'employee_id': employee_id
    }
    return render(request, "workshift/employee_info.html", content)


def employee_information_slug(request, employee_slug):
    content = {
        'employee_slug': employee_slug
    }
    return render(request, "workshift/employee_info_slug.html", content)


def archive_year(request, year):
    content = {
        'archive_year': year

    }
    return render(request, "workshift/archive.html", content)


# def page_not_found(request, exception):
#     return HttpResponseNotFound(f"<h1> ____ Page not Found _____<h1>")

def page_not_found(request, exception):
    content = {
    }
    return render(request, "workshift/page_not_found.html", content)


