from django.shortcuts import render

def home(request):
    devs = [
        {'name': 'Valentina (dev1)', 'url': 'dev1', 'description': 'Hoja de Vida - Valentina'},
        {'name': 'Angie (dev2)', 'url': 'dev2', 'description': 'Proyecto de Angie'},
        # Agregar más cuando estén listos
    ]
    return render(request, 'home/home.html', {'devs': devs})
