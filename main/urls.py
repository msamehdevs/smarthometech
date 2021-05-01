from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/updatestate/', views.updatestate, name='updatestate')
]