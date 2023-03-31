
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,redirect
from .models import Course, Enrollment,Lesson
from email.message import EmailMessage
from mycourse import  settings
from django.contrib.auth.models import User
def home(request):
    return render(request, 'app/home.html')

def signup(request):
    
    if request.method =="POST":
        username = request.POST['username']
      
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist")
            return redirect('home')

        if User.objects.filter(email=email):

            messages.error(request,"email already exist")
            return redirect('home')
        if len(username)>10:
            messages.error(request,"Username must be less than 10 characters")
        if pass1 != pass2:
            messages.error('Password did not match')
        if not username.isalnum():
            messages.error('username must be alpha-numric!')
            return redirect('home')
        myuser= User.objects.create_user(username,email,pass1)
       
        
    

        
    

        myuser.save()
        


        messages.success(request,"Your account is created" )
       

        
       
       
       
        return redirect("login1")


    
    
    
    return render(request,"app/signup.html")
def login1(request):
    


    if request.method =="POST":

        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username= username, password= pass1)
        if user is not None:



            login(request,user)
            fname = user.username
            return render(request,"app/course_list.html",{'fname':fname})


        else:

            messages.error(request,"Bad credentials")
            return redirect('home')
   
   
   
   
   
    return render(request,"app/login.html")
def logout1(request):
    logout(request)
    return redirect('home')

def enroll(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)
    if created: 
        message = "You have successfully enrolled in {}.".format(course.name)
    else:
        message = "You are already enrolled in {}.".format(course.name)
    return render(request, 'app/enroll.html', {'course': course, 'message': message})


@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'app/course_list.html', {'courses': courses})


@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user, course=course)
    return render(request, 'app/course_detail.html',
                  {'course': course, 'enrollment': enrollment})


@login_required
def lesson_complete(request, enrollment_id, lesson_id):
    enrollment = get_object_or_404(Enrollment, pk=enrollment_id, user=request.user)
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    enrollment.completed_lessons.add(lesson)
    return redirect('course_detail', course_id=enrollment.course.pk)
@login_required
def profile(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, 'app/profile.html', {'enrollments': enrollments})
