from django.urls import path
from app1 import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns=[
    path('', views.start, name='start'),
    path('employee/', views.employeelist.as_view()),
    ]