from django.shortcuts import render

def home(request):
    devs = [
        {'name': 'Valentina (dev1)', 'url': 'dev1', 'description': 'Hoja de Vida - Valentina'},
        {'name': 'Angie (dev2)', 'url': 'dev2', 'description': 'Proyecto de Angie'},
        {'name': 'Kevin (dev3)', 'url': 'dev3', 'description': 'Portafolio - Kevin'},
        {'name': 'Dania (dev4)', 'url': 'dev4', 'description': 'Proyecto de Dania'},
    ]
    return render(request, 'home/home.html', {'devs': devs})
