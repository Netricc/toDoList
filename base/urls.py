from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tasks/<int:qk>', views.tasks, name='tasks'),
    path('Create-List/', views.createList, name='createList'),
]
