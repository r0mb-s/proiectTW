from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestionForm
from .models import Question
from io import BytesIO
from reportlab.pdfgen import canvas

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'questions/success.html')
    else:
        form = QuestionForm()
    return render(request, 'questions/add_question.html', {'form': form})

def generate_pdf(request):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setTitle("Generated Test")

    # Fetch all questions from the database
    questions = Question.objects.all()
    y = 800  # Y-coordinate for the text
    
    pdf.drawString(200, y, "Test Questions")
    y -= 50

    for question in questions:
        pdf.drawString(50, y, f"Q: {question.question_text}")
        y -= 20
        pdf.drawString(70, y, f"1. {question.answer_1}")
        y -= 20
        pdf.drawString(70, y, f"2. {question.answer_2}")
        y -= 20
        pdf.drawString(70, y, f"3. {question.answer_3}")
        y -= 20
        pdf.drawString(70, y, f"4. {question.answer_4}")
        y -= 40

    pdf.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')
