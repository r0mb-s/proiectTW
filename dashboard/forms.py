from django import forms
from .models import QuizClass, Student, Quiz, Question

class QuizClassForm(forms.ModelForm):
    class Meta:
        model = QuizClass
        fields = ['name', 'description']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'class_name']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'number_of_questions', 'questions', 'answers']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'answer_1', 'answer_2', 'answer_3', 'answer_4', 'correct_answer']
