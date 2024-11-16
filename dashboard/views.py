from django.shortcuts import render, redirect, get_object_or_404
from .models import QuizClass
from .forms import QuizClassForm, QuizForm, StudentForm

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
