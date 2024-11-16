from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_class, name='create_class'),
    path('class/<int:class_id>/', views.class_detail, name='class_detail'),
    path('class/<int:class_id>/add_student/', views.add_student, name='add_student'),
    path('class/<int:class_id>/create_quiz/', views.create_quiz, name='create_quiz'),
]

