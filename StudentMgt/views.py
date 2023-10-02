from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#Create your views here.
#from .models import Department, Subject, Student, Level

def index(request):
    return render(request, 'base.html')
    """ try:
        admin_no = request.session['admin_no']
        student = Student.objects.get(admin_no=admin_no)
        return render(request, 'base.html', {'admin_no' : admin_no, 'student':student})
    except KeyError:
        return render(request, 'base.html') """
"""
def login(request):
    return render(request, 'StuLogin.html')

def login(request):
    if request.method=='POST':
        name = request.POST['name']
        admin_no = request.POST['admin_no']
        try:
            student = Student.objects.get(admin_no=admin_no)
        except Student.DoesNotExist:
            error= "No record found!"
            return render(request, 'StuLogin.html', {'error':error, 'name':name, 'admin_no':admin_no})
        else:
            if name!=student.name:
                error="Name incorrect"
                return render(request, 'StuLogin.html', {'error':error})
            else:
                request.session['admin_no'] = admin_no
                return HttpResponseRedirect(reverse('stuhome', args=(admin_no,)))
    return render(request, 'StuLogin.html')

def stuhome(request, admin_no):
     
     try:
        getSec=request.session["admin_no"]
        if getSec == admin_no:
            student = Student.objects.get(admin_no=admin_no)
            return render(request, 'StuHome.html', {'student':student, 'admin_no':admin_no} )
        else:
            error = "login required"
            logout(request)
            del request.session['admin_no']
            return redirect('index')
     except KeyError:
        error = "You must be logged in first to access the requested page"
        return render(request, 'StuLogin.html', {'error':error})
     else:
        return render(request, 'StuHome.html', {'student':student, 'admin_no':admin_no} )
def subject(request, admin_no):
     admin_no = request.session["admin_no"]
     student = Student.objects.get(admin_no=admin_no)
     return render(request, 'StuSubject.html',{'student':student, 'admin_no' : admin_no} )

def course(request, admin_no):
     admin_no = request.session["admin_no"]
     me = Student.objects.get(admin_no=admin_no)
     cl = me.StuClass
     dept = me.dept_id
     student = Student.objects.filter(StuClass=cl, dept_id=dept)

     return render(request, 'mate_dept.html',{'student':student, 'admin_no' : admin_no} )
def classMates(request, admin_no):
     admin_no = request.session['admin_no']
     me = Student.objects.get(admin_no=admin_no)
     cl = me.StuClass
     student = Student.objects.filter(StuClass=cl)
     return render(request, 'mate_class.html',{'student':student, 'admin_no' : admin_no} )
@login_required(login_url='login')
def logout(request):
    try:
        del request.session['admin_no']
    except KeyError:
        pass
     return HttpResponse('<h3> you just loggged out<h3>') 
    return redirect ('/')
         


            
 """