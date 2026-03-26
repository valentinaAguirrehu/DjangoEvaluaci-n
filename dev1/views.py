from django.shortcuts import render

def index_valentina(request):
    # No incluyas "template" en la ruta
    return render(request, 'dev1/index_Valentina.html')