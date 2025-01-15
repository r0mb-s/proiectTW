from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.landingpage, name='landingpage'),
    path('create/', views.create_class, name='create_class'),
    path('class/<int:class_id>/', views.class_detail, name='class_detail'),
    path('class/<int:class_id>/add_student/', views.add_student, name='add_student'),
    path('class/<int:class_id>/create_quiz/', views.create_quiz, name='create_quiz'),
    path('class/<int:class_id>/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('class/<int:class_id>/<int:quiz_id>/generate_pdf', views.generate_pdf, name='generate_pdf'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('profile/', views.profile_view, name='profile_view'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('grade/<int:class_id>/', views.grade, name='grade'),
    path('takegrade/', views.takegrade, name='takegrade'),
]

