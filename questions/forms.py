from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'answer_1', 'answer_2', 'answer_3', 'answer_4', 'correct_answer']
