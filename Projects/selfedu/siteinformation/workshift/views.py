from django.shortcuts import render

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












