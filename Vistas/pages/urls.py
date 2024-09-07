from django.urls import path
from pages.views import saludo, NuevoSaludo

urlpatterns = [
    path('saludo/', saludo, name='saludo'),
    #path('saludo/<str:nombre>/', saludo, name='saludo'),
    path('nuevosaludo/', NuevoSaludo.as_view(), name='nuevo saludo'),
    #path('nuevosaludo/<str:nombre>/', NuevoSaludo.as_view(), name='nuevo saludo'),
]