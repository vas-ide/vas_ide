from django.shortcuts import render

from youapp.models import Worker
from urllib import request

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView




class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["title"] = "Index"
        context["name"] = "Клуб дедов програмистов & Синьёр помидор"
        context["all_workers"] = Worker.objects.all()
        return context

    # def index_page(request):
    #     # new_worker = Worker(name="Иван", second_name="Болванов", salary=15500)
    #     # new_worker.save()
    #     # Worker.objects.create(name="Иван", second_name="Болванов", salary=15500)
    #     # worker_to_chenge = Worker.objects.get(id=5)
    #     # worker_to_chenge.second_name = "Дупgggлетов"
    #     # worker_to_chenge.save()
    #     # print(worker_to_chenge)
    #     # Worker.objects.get(id=5).delete()
    #     all_workers = Worker.objects.all()
    #     # print(all_workers)
    #     #
    #     # workers_filtered = Worker.objects.filter(salary=15000)
    #     # print(workers_filtered)
    #     # for i in all_workers:
    #     #     print(f"Фамилия-{i.second_name:>15},    Имя-{i.name:>10},    Оклад-{i.salary:>5}    ID{i.id}")
    #     return render(request, "index.html", {})