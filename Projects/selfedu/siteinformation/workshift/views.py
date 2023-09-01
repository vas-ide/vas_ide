from django.shortcuts import render

# Create your views here.
def all_information(request):


    content = {

    }
    return render(request, "workshift/index.html", content)


# employee
def employee_information(request):


    content = {

    }
    return render(request, "workshift/employee_info.html", content)
