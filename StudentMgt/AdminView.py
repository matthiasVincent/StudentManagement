from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Student, Level, Department, Subject

#Custom admin login
@login_required(login_url='admin_login')
def admin_page(request):
    user = request.user
    student = Student.objects.all()
    just_added = student[len(student)-1]
    return render(request, 'admin_page.html', {'user':user, 'student': student})

def admin_login(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request, username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_page')
        else:
            messages.info(request, "Invalid credentials: email, username or password not correct")
            return render(request, 'cust_admin.html')
        

    return render(request, 'cust_admin.html')
def logout_admin(request):
    logout(request) 
    return redirect('admin_login')

def add_user(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        first_name = request.POST['first']
        last_name = request.POST['last']
        depart_name = request.POST['dept_name']
        class_name = request.POST['stuclass']
        admin_no = request.POST['admin_no']
        sex=request.POST['sex']
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'username taken')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'email already taken')
        else:
            user =User.objects.create_user(username=username, email=email,first_name=first_name,last_name=last_name)
            user.save()
            dept = Department.objects.get(name=depart_name)
            stuclass = Level.objects.get(name=class_name)
            student=Student.objects.create(user=user,id_user=user.id, dept_id=dept,StuClass=stuclass,admin_no=admin_no, sex=sex)
            student.save()
            student = Student.objects.all()
            just_added = student[len(student)-1]
            if "another" in request.POST:
                return render(request, 'adduser.html', {'just_added':just_added})
            else:
                return render(request, 'admin_page.html', {'student':student, 'just_added':just_added})
                #return redirect('admin_page', args=(just_added,))
            #return render(request, 'admin_page.html')
            #return redirect('admin_page')
    return render(request, 'adduser.html')
def save_add(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        first_name = request.POST['first']
        last_name = request.POST['last']
        depart_name = request.POST['dept_name']
        class_name = request.POST['stuclass']
        admin_no = request.POST['admin_no']
        sex=request.POST['sex']
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'username taken')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'email already taken')
        else:
            user =User.objects.create_user(username=username, email=email,first_name=first_name,last_name=last_name)
            user.save()
            dept = Department.objects.get(name=depart_name)
            stuclass = Level.objects.get(name=class_name)
            student=Student.objects.create(user=user,id_user=user.id, dept_id=dept,StuClass=stuclass,admin_no=admin_no, sex=sex)
            student.save()
            student = Student.objects.all()
            just_added = student[len(student)-1]
            return render(request, 'add_user.html', {'just_added': just_added})