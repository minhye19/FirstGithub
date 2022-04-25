from django.urls import path

from . import views

app_name = 'question'
urlpatterns = [
    path('', views.q1),
    path('q2', views.q2),
]