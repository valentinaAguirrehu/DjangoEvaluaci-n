"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dev1 import views as dev1_views
from dev2 import views as dev2_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # página principal
    path('dev1/', dev1_views.index_valentina, name='dev1'),
    path('dev2/', dev2_views.index_Angie, name='dev2'),
    # Agregar dev3 y dev4 cuando estén listos
]