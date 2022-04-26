from django.urls import path
from . import views

app_name = 'survey'
urlpatterns = [
    path('q1/', views.q1),
    path('q2/', views.q2),
    path('list/', views.SVlist),
]