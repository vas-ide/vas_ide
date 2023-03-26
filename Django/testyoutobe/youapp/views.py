from django.shortcuts import render

from youapp.models import Worker


def index_page(request):

    all_workers = Worker.objects.all()
    print(all_workers)

    workers_filtered = Worker.objects.filter(salary=15000)
    print(workers_filtered)
    for i in all_workers:
        print(f"Фамилия-{i.second_name:>15},    Имя-{i.name:>10},    Оклад-{i.salary:>5}    ID{i.id}")


    return render(request, "index.html")