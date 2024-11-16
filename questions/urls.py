from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_question, name='add_question'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
]
