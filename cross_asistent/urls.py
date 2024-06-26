from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('preguntas-frecuentes/', views.faq, name='faq'),
    path('blog-eventos/', views.blog, name='blog'),
    path('mapa/', views.map, name='map'),
    path('administracion/acceder/', views.singinpage, name='singin'),
    path('administracion/registro/', views.singuppage, name='singup'),
    path('administracion/', views.dashbAdmin, name='dashb_admin'),
    path('administracion/tarea/<int:tarea_id>/', views.tareaView, name='tareaView'),
    path('logout/', views.singoutpage, name='singout'),
]
