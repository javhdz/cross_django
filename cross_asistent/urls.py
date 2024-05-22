from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('preguntas-frecuentes/', views.faq, name='faq'),
    path('blog-eventos/', views.blog, name='blog'),
    path('mapa/', views.map, name='map'),
    path('administracion/inicio/', views.formsAdmin),
]
