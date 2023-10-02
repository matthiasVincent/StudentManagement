from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate
from .models import Department, Student, Subject, Level
from django.contrib.auth import login, logout
from django.contrib import messages

User = get_user_model()

def stulogin(request):
    if request.method == "POST":
        full_name=request.POST["full_name"]
        admin_no = request.POST["admin_no"]
        try:
            student = Student.objects.get(admin_no=admin_no)
            username = student.user.username
            user = User.objects.get(username=username)
            print(username, student,user)
            if user is not None:
                login(request, user)
                return redirect('stuhome')
            else:
                messages.info(request, "Invalid credentials: email, username or password not correct")
                return render(request, 'studentlogin.html')
        except Student.DoesNotExist:
            messages.info(request, "No record found!")
        """ user = authenticate(request, first_name=first_name, last_name=last_name)
        if user is not None:
            try:
                student = Student.objects.filter(full_name=full_name,admin_no=admin_no)
                login(request, user)
                return redirect('stuhome')
            except Student.DoesNotExist:
                messages.info(request, "wrong admission number for this student")
        else:
            messages.info(request, "Invalid credentials: email, username or password not correct")
            return render(request, 'studentlogin.html') """
    return render(request, 'studentlogin.html')
        

def stuhome(request):
    user = request.user
    student = Student.objects.get(user=user)
    course_mate = Student.objects.filter(StuClass=student.StuClass, dept_id=student.dept_id)
    class_mate = Student.objects.filter(StuClass=student.StuClass)
    print(class_mate)
    return render(request, 'studenthome.html', {'student':student, 'course_mate':course_mate, 'class_mate':class_mate})
def subject(request):
    pass
def class_mates(request):
    pass
def course(request):
    pass
def logout_student(request):
    logout(request)
    return redirect('stulogin')