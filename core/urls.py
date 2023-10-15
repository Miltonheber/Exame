from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('options/', options, name='options'),
    path('form/<int:id>', form, name='form'),
    path('download/', download, name='download'),
    path('sobre/', sobre, name='sobre'),
    path('contacto/', contacto, name='contacto')
]
