from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/updatestate/', views.updatestate, name='updatestate'),
    # re_path(r'^data/(?P<pl_slug>.+)/$', views.displayBoardData, name='displayBoardData'),
    path('data/<int:board>/', views.displayBoardData, name='displayBoardData'),
]