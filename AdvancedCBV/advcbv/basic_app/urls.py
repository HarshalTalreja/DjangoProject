from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.IndexView.as_view()),
    path('list/', views.SchoolListView.as_view(),name='list'),
]
