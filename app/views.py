from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.

def registration_form(request):
    data=User.objects.all()
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname') 
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        val=0
        for i in data:
            if i.username == uname:
                val=1
                return HttpResponse("Username already exists")
            
        if val==0:
            obj=User()
            obj.first_name=fname
            obj.last_name=lname
            obj.username=uname
            obj.password=password
            obj.save()
            return redirect('log')           
    return render(request,'registration.html',{'dataa':data})
def login_form(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        user=User.objects.filter(username=name,password=password).first()
        if user is not None:
            request.session['username']=user.username
            request.session['password']=user.password
            return redirect('dashh')
        else:
            return HttpResponse('Invalid username or password')
    else:
        return render(request,'login.html')

def dash(request):
    count=Students.objects.count()
    recent=Students.objects.order_by('-id')[:5]
    return render(request,'dashboard.html',{'count':count,'recent':recent})

def student_details(request):
    data=Students.objects.all()
    return render(request,'student.html',{'data':data})

def class_details(request):
    data=Classes.objects.all()
    return render(request,'class.html',{'data':data})

def logout_user(request):
    logout(request)
    return redirect('log')

def addStudent(request):
    data=Classes.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name')
        no=request.POST.get('no')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        obj=Students()
        obj.name=name
        obj.roll_number=no
        obj.email=email
        obj.date_of_birth=dob
        obj.student_class=Classes.objects.get(id=request.POST.get('cls'))
        obj.save()
        return redirect('students')
    return render(request,'add_student.html',{'data':data})
def editStudent(request,id):
    obj=Students.objects.get(id=id)
    cl=Classes.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name')
        no=request.POST.get('no')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        obj.name=name
        obj.roll_number=no
        obj.email=email
        obj.date_of_birth=dob
        obj.student_class=Classes.objects.get(id=request.POST.get('cls'))
        obj.save()
        return redirect('students')
    return render(request,'edit_student.html',{'data':cl,'obj':obj})
def deleteStudent(request,id):
    data=Students.objects.get(id=id)
    data.delete()
    return redirect('students')


def addClass(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        sec=request.POST.get('sec')
        teacher=request.POST.get('teacher')
        obj=Classes()
        obj.class_name=name
        obj.section=sec
        obj.class_teacher=teacher
        obj.save()
        return redirect('classs')
    return render(request,'add_class.html')
def editClass(request,id):
    obj=Classes.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        sec=request.POST.get('sec')
        teacher=request.POST.get('teacher')
        obj.class_name=name
        obj.section=sec
        obj.class_teacher=teacher
        obj.save()
        return redirect('classs')
    return render(request,'edit_class.html',{'obj':obj})
def deleteClass(request,id):
    data=Classes.objects.get(id=id)
    data.delete()
    return redirect('classs')