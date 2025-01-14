from django.shortcuts import render, redirect, get_object_or_404
from .models import QuizClass, Quiz
from .forms import QuizClassForm, QuizForm, StudentForm
from django.http import HttpResponse
from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# from reportlab.pdfgen import canvas

from googleapiclient.discovery import build
import dashboard.authhelper as authhelper

def get_teacher_classes(service):
    """Fetch all classes where the user is a teacher."""
    results = service.courses().list().execute()  # Fetch courses
    courses = results.get('courses', [])
    return courses


def google_classroom_classes(request):
    """View to display Google Classroom classes for the logged-in teacher."""
    service = authhelper.authenticate_user()
    classes = get_teacher_classes(service)
    return render(request, 'classroom_classes.html', {'classes': classes})

def landingpage(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == 'login' :
            email = request.POST.get('email1')
            password = request.POST.get('password1')
            
            user = authenticate(request, username=email, password=password)
            if user is not None :
                login(request, user)
                return redirect('dashboard')
            else : 
                messages.error(request, 'Invalid login credentials')
                return render(request, 'dashboard/landingpage.html')
        
        elif form_type == "signin" :
            email = request.POST.get('email2')
            password = request.POST.get('password2')
            confirm_password = request.POST.get('confirmPassword')
            
            if password != confirm_password :
                messages.error(request, 'Password and confirm password are different')
            elif User.objects.filter(username=email).exists():
                messages.error(request, 'Username already taken')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered')
            else:
                # Create new user
                User.objects.create_user(username=email, email=email, password=password)
                messages.success(request, 'Account created successfully! You can now log in.')
                return redirect('landingpage')
            
            return render(request, 'dashboard/landingpage.html')
            
                    
    return render(request, 'dashboard/landingpage.html')

def dashboard(request):
    if not request.user.is_authenticated:
        # Redirect to login page if the user is not authenticated
        return redirect('http://127.0.0.1:8000/auth/login/google-oauth2/')  # Replace 'login' with the correct name of your login URL

    # If authenticated, proceed with the normal flow
    classes = QuizClass.objects.filter(account_mail = request.user.email)
    return render(request, 'dashboard/dashboard.html', {'classes': classes})

def create_class(request):
    if request.method == 'POST':
        form = QuizClassForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.account_mail = request.user.email;
            instance.save()
            return redirect('dashboard')
    else:
        form = QuizClassForm()
        classes = QuizClass.objects.filter(account_mail = request.user.email)

    return render(request, 'dashboard/create_class.html', {'form': form, 'classes': classes})

def class_detail(request, class_id):
    class_obj: QuizClass = get_object_or_404(QuizClass, id=class_id)
    students = class_obj.students.all()
    quizes = class_obj.quizes.all()
    classes = QuizClass.objects.filter(account_mail = request.user.email)
    return render(request, 'dashboard/class_detail.html', {'class': class_obj, 'students': students, 'quizes': quizes, 'classes': classes})

def add_student(request, class_id):
    class_obj = get_object_or_404(QuizClass, id=class_id)
    classes = QuizClass.objects.filter(account_mail = request.user.email)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.class_name = class_obj
            student.save()
            return redirect('class_detail', class_id=class_id)
    else:
        form = StudentForm()

    return render(request, 'dashboard/add_student.html', {'form': form, 'class': class_obj, 'classes': classes})

def create_quiz(request, class_id):
    class_obj = get_object_or_404(QuizClass, id=class_id)
    classes = QuizClass.objects.filter(account_mail = request.user.email)
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.class_name = class_obj
            student.save()
            return redirect('class_detail', class_id=class_id)
    else:
        form = QuizForm()

    return render(request, 'dashboard/create_quiz.html', {'form': form, 'class': class_obj, 'classes': classes})

def quiz_detail(request, class_id, quiz_id):
    class_obj = get_object_or_404(QuizClass, id=class_id)
    quiz_obj = get_object_or_404(Quiz, id=quiz_id)
    classes = QuizClass.objects.filter(account_mail = request.user.email)
    return render(request, 'dashboard/quiz_detail.html', {'class': class_obj, 'quiz': quiz_obj, 'classes': classes})

def generate_pdf(request, class_id, quiz_id):
    #    buffer = BytesIO()
    #    pdf = canvas.Canvas(buffer)
    #    pdf.setTitle("Generated Test")
    #
    #    questions = Question.objects.all()
    #    y = 800
    #    
    #    pdf.drawString(200, y, "Test Questions")
    #    y -= 50
    #
    #    for question in questions:
    #        pdf.drawString(50, y, f"Q: {question.question_text}")
    #        y -= 20
    #        pdf.drawString(70, y, f"1. {question.answer_1}")
    #        y -= 20
    #        pdf.drawString(70, y, f"2. {question.answer_2}")
    #        y -= 20
    #        pdf.drawString(70, y, f"3. {question.answer_3}")
    #        y -= 20
    #        pdf.drawString(70, y, f"4. {question.answer_4}")
    #        y -= 40
    #
    #    pdf.save()
    #    buffer.seek(0)
    #    return HttpResponse(buffer, content_type='application/pdf')
    return render(request, 'dashboard/idk.html')




from django.shortcuts import render, redirect

def profile_view(request):
    if not request.user.is_authenticated:
        # Redirect to login page if the user is not authenticated
        return redirect('http://127.0.0.1:8000/auth/login/google-oauth2/')  # or replace 'login' with the appropriate login URL name

    # If authenticated, proceed with the normal flow
    user = request.user
    return render(request, 'dashboard/profile.html', {
        'username': user.username,
        'email': user.email,
        'google_picture': getattr(user, 'google_picture_url', None),
    })

def custom_logout(request):
    logout(request)  # Django's built-in logout function
    return redirect('/')  # Redirect to home or any page you prefer