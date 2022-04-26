from django.urls import path
from . import views

app_name = 'survey'
urlpatterns = [
    path('q1/', views.q1),
    path('q2/', views.q2),
    path('list/', views.SVlist),
    path('save_survey', views.save_survey),
    path('show_result', views.show_result),
]