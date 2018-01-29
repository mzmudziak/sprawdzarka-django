import random

from django.shortcuts import render

from app.entity.Test import Test


def add(request):
    if request.method == "POST":
        # dodanie do bazy i zwrócenie
        t = createTest()
        return render(request, 'view/test/added.html', {'test': t})

    else:
        return render(request, 'view/test/add.html')


def createTest():
    t = Test()
    t.id = random.randint(0, 100)
    t.input_data = 'input data'
    t.output_data = 'output data'
