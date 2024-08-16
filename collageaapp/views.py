from django.shortcuts import render,redirect
from collageaapp.models import Addcourse
from collageaapp.models import Student
from collageaapp.models import Teacher
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.
def admin(request):
    return render(request,'adminhome.html')
@login_required(login_url='admin')
def adminnhomepage(request):
    return render(request,'adminnhomepage.html')
def signup(request):
    course=Addcourse.objects.all()
    return render(request,'signup.html',{'c':course})

@login_required(login_url='admin')
def addcourse(request):
    return render(request,'addcourse.html')
@login_required(login_url='admin')
def addcoursedb(request):
    if request.method=='POST':
        coursename=request.POST.get('coursename')
        coursefee=request.POST.get('coursefee')
        Course=Addcourse(coursename=coursename,coursefee=coursefee)
        Course.save()
        return redirect('addstudent')
@login_required(login_url='admin')
def addstudent(request):
    courses=Addcourse.objects.all()
    return render(request,'addstudent.html',{'course':courses})
@login_required(login_url='admin')
def addstudentdb(request):
    if request.method=='POST':
        studentname=request.POST['studentname']
        Address=request.POST['Address']
        Age=request.POST['Age']
        Date=request.POST['Date']
        ok=request.POST['ok']
        course1=Addcourse.objects.get(id=ok)
        sttudent=Student(studentname=studentname,Address=Address,Age=Age,Date=Date,course=course1)
        sttudent.save()
        return redirect('showstudents')
@login_required(login_url='admin')
def showstudents(request):
    sttudent=Student.objects.all()
    return render(request,'showstudents.html',{'students':sttudent})


@login_required(login_url='admin')
def edit(request,pk):
    studentt=Student.objects.get(id=pk)
    courses=Addcourse.objects.all()
    
    return render(request,'edit.html',{'s':studentt,'k':courses})
@login_required(login_url='admin')
def edit_db(request,pk):
    if request.method=='POST':
      studentt=Student.objects.get(id=pk)
      studentt.studentname=request.POST.get('studentname')
      studentt.Address=request.POST.get('Address')
      studentt.Age=request.POST.get('Age')
      studentt.Date=request.POST.get('Date')
      ok=request.POST.get('ok')
      studentt.course=Addcourse.objects.get(id=ok)
      studentt.save()
      return redirect('showstudents')
    return render(request,'edit.html')
@login_required(login_url='admin')
def delete(request,pk):
    e=Student.objects.get(id=pk)
    e.delete()
    return redirect('showstudents')
def addsignup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpasswrd=request.POST['cpasswrd']
        Address=request.POST['Address']
        Age=request.POST['Age']
        email=request.POST['email']
        Contactnumber=request.POST['Contactnumber']
        ok=request.POST['ok']
        img=request.FILES.get('img')
        if password==cpasswrd:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exist!')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                 first_name=first_name,
                 last_name=last_name,
                 username=username,
                 password=password,
                 email=email)
                user.save()
                courses=Addcourse.objects.get(id=ok)
                u=User.objects.get(id=user.id)
                r=Teacher(Address=Address,Age=Age,Contactnumber=Contactnumber,course=courses,img=img,user=u)
                r.save()
                return redirect('admin')
        else:
            messages.info(request,'incorrect password')
            return redirect('/')
def loginn(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        User=auth.authenticate(username=username,password=password)
        if User is not None:
            if User.is_staff:
                login(request,User)
                return redirect('adminnhomepage')
              
            
            else:
                login(request,User)
                auth.login(request,User)
                messages.info(request,f'Welcome {username}')
                return redirect('teacherprofilehome')
        else:
            messages.info(request,'invalid username& password')
            return redirect('admin')
    return render(request,'adminhome.html')
            
@login_required(login_url='admin')
def logout(request):
      auth.logout(request)
      return redirect('admin')
@login_required(login_url='admin')
def teacherprofilehome(request):
    return render(request,'teacherprofile.html')
@login_required(login_url='admin')
def showteacher(requst):
    teacher=Teacher.objects.all()
    return render(requst,'showteacher.html',{'teach':teacher})
@login_required(login_url='admin')
def dlttch(request,pk):
    teach=Teacher.objects.get(user=pk)
    teach.delete()
    auth_user=User.objects.get(id=pk)
    auth_user.delete()
    return redirect('showteacher')
@login_required(login_url='admin')
def edittch(request):
    teach=Teacher.objects.get(user=request.user)
    courses=Addcourse.objects.all()
    
    return render(request,'edittch.html',{'te':teach,'k':courses})
@login_required(login_url='admin')
def edittchdb(request,pk):
    if request.method=='POST':
      teach=Teacher.objects.get(user=pk)
      user=User.objects.get(id=pk)
      user.first_name=request.POST.get('first_name')
      user.last_name=request.POST.get('last_name')
      user.username=request.POST.get('username')
      user.email=request.POST.get('email')
      teach.Address=request.POST.get('Address')
      teach.Age=request.POST.get('Age')
      teach.Contactnumber=request.POST.get('Contactnumber')
      ok=request.POST.get('ok')
      course=Addcourse.objects.get(id=ok)
      teach.course=course
      if 'img' in request.FILES:
          teach.img=request.FILES['img']
      teach.save()
      user.save()
    
     
     
      return redirect('viewpr')




    
   

@login_required(login_url='admin')
def viewpr(request):
    current_user=request.user.id
    user1=Teacher.objects.get(user_id=current_user)
    return render(request,'viewtprofile.html',{'users':user1})

    

