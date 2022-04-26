from django.urls import path
from . import views

app_name = 'answer'
urlpatterns = [
    path('a1/', views.a1),
    path('a2/', views.a2),
]