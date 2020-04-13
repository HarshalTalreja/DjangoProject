from django.urls import path
from basic_app import views

# app_name = 'basic_app'

urlpatterns = [
    path('',views.IndexView.as_view(), name = 'homepage'),
    path('list/', views.SchoolListView.as_view(), name='schoollist'),
    path('slist/', views.StudentListView.as_view(), name='studentlist'),
    path("sdetail/<int:pk>/",views.StudentDetailView.as_view(), name='studentdetail'),
    path('detail/<int:pk>/',views.SchoolDetailView.as_view(), name='schooldetail'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path("update/<int:pk>/", views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/',views.SchoolDeleteView.as_view(), name='delete')
]
