from django.urls import path

from . import views

urlpatterns = [
    path('', views.studentInfo),
    path('delete/<int:pk>/', views.RejectStudent)
]
