from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name = 'home'),
    path('update/<str:pk>/', update, name = 'update-task'),
    path('delete/<str:pk>/', delete, name = 'delete-task'),
    path('clear/',clear, name = 'clear-all')
]
