import csv
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from login.models import Department,Class,Student,Faculty,Course,Attendance,Teache
from django.contrib import messages

# Create your views here.
stu=""
dep=""
cla=""
cou=""

def initial(stut,dept):
    global stu,dep
    stu=stut
    dep=dept
    return

def tial(clat,cout):
    global cla,cou
    cla=clat
    cou=cout
    print(clat)
    print(cout)
    return

def studlogin(request):
    if request.method=="POST":
        u,p=request.POST.get('email'),request.POST.get('password')
        stud=Student.objects.filter(stud_id=u)
        if stud.exists():
            if stud.get().s_password==p:
                d=stud.get().dept_id.dept_id
                initial(u,d)
                return studindex(request)
            else:
                
                return redirect('index')
        else:
            
            return redirect('index')
    else:
        
        return redirect('index')

def studindex(request):
    dept=Department.objects.filter(dept_id=dep)
    stud=Student.objects.filter(stud_id=stu)
    atte=Attendance.objects.all().filter(stud_id=stu).order_by('-date')
    cour,cou=[],[]
    for i in atte:
        if i.course_id not in cour:
            cour.append(i.course_id)
    for i in cour:
        cou.append([i.course_id,0,Attendance.objects.all().filter(stud_id=stu,course_id=i.course_id).count(),0,i.course_name])
    for i in atte:
        for j in range(len(cou)):
            if i.course_id.course_id==cou[j][0]:
                if i.presence:
                    cou[j][1]+=1
    for i in cou:
        i[3]=int(i[1]/i[2]*100)
    coud=[]
    for i in cou:
        if i[3]<=75:
            coud.append(i)
    return render(request,'studindex.html',{'stud':stud,'cou':coud})

def studadd(request):
    dept=Department.objects.filter(dept_id=dep)
    stud=Student.objects.filter(stud_id=stu)
    atte=Attendance.objects.all().filter(stud_id=stu).order_by('-date')
    cour,cou=[],[]
    for i in atte:
        if i.course_id not in cour:
            cour.append(i.course_id)
    for i in cour:
        cou.append([i.course_id,0,Attendance.objects.all().filter(stud_id=stu,course_id=i.course_id).count(),0,i.course_name])
    for i in atte:
        for j in range(len(cou)):
            if i.course_id.course_id==cou[j][0]:
                if i.presence:
                    cou[j][1]+=1
    for i in cou:
        i[3]=int(i[1]/i[2]*100)
    print(cou)
    return render(request,'studadd.html',{'stud':stud,'cou':cou})

