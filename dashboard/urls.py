from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_class, name='create_class'),
    path('add/', views.add_question, name='add_question'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('class/<int:class_id>/', views.class_detail, name='class_detail'),
    path('class/<int:class_id>/add_student/', views.add_student, name='add_student'),
    path('class/<int:class_id>/create_quiz/', views.create_quiz, name='create_quiz'),
]

