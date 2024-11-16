from django import forms
from .models import QuizClass, Student, Quiz

class QuizClassForm(forms.ModelForm):
    class Meta:
        model = QuizClass
        fields = ['name', 'description']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'number_of_questions', 'questions', 'answers']
