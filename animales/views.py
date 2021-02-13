from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')


def add_animal(request):
    print(request.POST['especie'])
    return HttpResponse('Animal agregado')
