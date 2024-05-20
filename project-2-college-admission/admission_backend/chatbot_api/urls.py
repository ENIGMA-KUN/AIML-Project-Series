from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_admission_info, name='admission_info'),
]