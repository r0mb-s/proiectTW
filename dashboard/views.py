from django.shortcuts import render, redirect, get_object_or_404
from .models import QuizClass, Question
from .forms import QuizClassForm, QuizForm, StudentForm, QuestionForm
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas


def dashboard(request):
    classes = QuizClass.objects.all()
    return render(request, 'dashboard/dashboard.html', {'classes': classes})

def create_class(request):
    if request.method == 'POST':
        form = QuizClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = QuizClassForm()

    return render(request, 'dashboard/create_class.html', {'form': form})

def class_detail(request, class_id):
    class_obj: QuizClass = get_object_or_404(QuizClass, id=class_id)
    students = class_obj.students.all()
    quizes = class_obj.quizes.all()
    return render(request, 'dashboard/class_detail.html', {'class': class_obj, 'students': students, 'quizes': quizes})

def add_student(request, class_id):
    class_obj = get_object_or_404(QuizClass, id=class_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.class_name = class_obj
            student.save()
            return redirect('class_detail', class_id=class_id)
    else:
        form = StudentForm()

    return render(request, 'dashboard/add_student.html', {'form': form, 'class': class_obj})

def create_quiz(request, class_id):
    class_obj = get_object_or_404(QuizClass, id=class_id)
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.class_name = class_obj
            student.save()
            return redirect('class_detail', class_id=class_id)
    else:
        form = QuizForm()

    return render(request, 'dashboard/create_quiz.html', {'form': form, 'class': class_obj})

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
