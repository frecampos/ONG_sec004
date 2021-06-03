from django.contrib import admin
from django.urls import path
#from .views import index, perros, gatos, scooby, coraje, patan
from webAyudaPeludo import views # todo


urlpatterns = [
    path('',views.index,name='INDEX'),
    path('perros/',views.perros,name='PERROS'),
    path('gatos/',views.gatos,name='GATOS'),
    path('scooby/',views.scooby,name='SCOOBY'),
    path('patan/',views.patan,name='PATAN'),
    path('coraje/',views.coraje,name='CORAJE'),
    path('tom/',views.tom,name='TOM'),
    path('doraemon/',views.doraemon,name='DORAEMON'),
    path('garfield/',views.garfield,name='GARFIELD'),
]

# {% url '<nombre>' %} --> lengueje DJANGO TEMPLATE