from django.shortcuts import render

# Vista para la página principal
def index(request):
    return render(request, 'dev3/index_kevin.html')