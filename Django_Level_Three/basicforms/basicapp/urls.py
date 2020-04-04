from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='basicapp_index'),
    path('formpage/', views.form_name_view, name='basicapp_form')
]
