
# from os import uname
import json
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Student.forms import *
from Student.models import *
from tkinter import *
from tkinter import messagebox
from datetime import date
from django.contrib import messages


# Create your views here.




# def index(request):
#     if 'student' in request.session.keys():
#         return redirect('home1')
#     else:
#         return render(request,'index.html')

# def save(request):
#     if 'username' in request.session.keys():
#         s1=user(uname=request.POST['nm'],uemail=request.POST['em'],upass=request.POST['pswd'],uroll=request.POST['rm'])
#         s1.save()
#         return render(request,'home1.html',{'s1':s1})
#     else:
#         return redirect('/Student/signup')

#     # s1=user(uname=request.POST['nm'],uemail=request.POST['em'],upass=request.POST['pswd'])
#     # s1.save()
#     # return render(request,'home1.html',{'s1':s1})

# def check(request):
#     try:
#         if 'student' in request.session.keys():
#             std = request.session['student']
#             s1=user.objects.get(uemail=std)
#             return render(request,'home1.html',{'s1':s1})
#         else :
#             s1=user.objects.get(uemail=request.POST['em'])
#             if(s1.upass==request.POST['pswd']):
#                 request.session['student']=request.POST['em']
#                 return render(request,'home1.html',{'s1':s1})
#             else:
#                 root1=Tk()
#                 root1.withdraw()
#                 root1.attributes('-topmost',True)
#                 messagebox.showerror('incorrect password','The entered password does not match with the email')
#                 return redirect('/Student/index')
#     except Exception as e: 
#         root=Tk()
#         root.withdraw()
#         root.attributes('-topmost',True)
#         messagebox.showerror('invalid','this email is not registered with us')
#         return redirect('/Student/index')


# def signup(request):
#     request.session['username']='param'
#     return render(request,'signup.html')



def home(req):
    # if 'student' in req.session.keys():
    stu = Student.objects.get(uemail = "ash@gmail.com")
    att = Attendance.objects.filter(student_id = stu.uemail)
    present_count = att.filter(status='True').count()
    absent_count = att.filter(status='False').count()
    sub = Subject.objects.filter(course_id = stu.ucourse_id)
    print(sub)
    att_p=[]
    att_a=[]
    for i in sub:
        att_p.append(Attendance.objects.filter(status="True",student_id = stu.uemail, subject_id = i.id).count())
        att_a.append(Attendance.objects.filter(status="False",student_id = stu.uemail, subject_id = i.id).count())
    sub = Subject.objects.filter(course_id = stu.ucourse_id)
    attendData = {}
    for i in sub:
        attend = {}
        sub_att = Attendance.objects.filter(student_id = stu.uemail, subject_id = i.id)
        for att in sub_att:
            if att.status:
                attend[att.date.strftime("%B %d, %Y")] = "Present"
            else:
                attend[att.date.strftime("%B %d, %Y")] = "Absent"
        attendData[i.name] = attend
    print(attendData)
    sub = [sub.name for sub in sub]
    total =present_count+absent_count
    return render(req, 'home.html', {'stu': stu, 'p': present_count, 'a': absent_count, 'total':total, 'per':present_count*100/total, 'sub':sub, 'att_p':att_p,'att_a':att_a,'attendData':json.dumps(attendData)})
    

def staffHome(req):
    return render(req,'staffHome.html')

def adminHome(req):

    return render(req,'adminHome.html')

def addStaff(req):
    if req.method=='POST':
        name = req.POST.get('name')
        coid = req.POST.get('course_id')
        subid = req.POST.get('sub_id')
        mob = req.POST.get('mob')
        dob = req.POST.get('dob')
        doj = req.POST.get('doj')
        pswd =req.POST.get('pswd')
        cpswd =req.POST.get('cpswd')
        if(pswd==cpswd):
            s1 = Staff(name=name,mob=mob,dob=dob,doj=doj,pswd=pswd)
            s1.save()
        id = s1.id
        s = Staff_Subjects()

    # else:
    #     return redirect('index')
    





# def attendance(request):
#     # if 'student' in request.session.keys():
#         # n=request.GET['srr']
#         # s1=user.objects.get(uname=n)
#         # if s1.jm!="dict":
#         #     m=s1.jm.keys()
#         #     mv=s1.jm.values()
#         # else:
#         #     m=[]
#         #     mv=[]

#         # if s1.jp!="dict":
#         #     p=s1.jp.keys()
#         #     pv=s1.jp.values()
#         # else:
#         #     p=[]
#         #     pv=[]

#         # if s1.jc!="dict":
#         #     c=s1.jc.keys()
#         #     cv=s1.jc.values()
#         # else:
#         #     c=[]
#         #     cv=[]

#         # if s1.jel!="dict":
#         #     el=s1.jel.keys()
#         #     elv=s1.jel.values()
#         # else:
#         #     el=[]
#         #     elv=[]

#         # if s1.jex!="dict":
#         #     ex=s1.jex.keys()
#         #     exv=s1.jex.values()
#         # else:
#         #     ex=[]
#         #     exv=[]


#         # return render(request,'attendance.html',{'m':m,'p':p,'c':c,'el':el,'ex':ex,'mv':mv,'pv':pv,'cv':cv,'elv':elv,'exv':exv})
#     # else :
#     #     return redirect("./index")
    
#     email = request.GET['stu']
#     print(email)
#     stu = Student.objects.get(uemail = email)
#     sub = Subject.objects.filter(course_id = stu.ucourse_id)
#     attendData = {}
#     for i in sub:
#         attend = {}
#         sub_att = Attendance.objects.filter(student_id = stu.uemail, subject_id = i.id)
#         for att in sub_att:
#             if att.status:
#                 attend[att.date.strftime("%B %d, %Y")] = "Present"
#             else:
#                 attend[att.date.strftime("%B %d, %Y")] = "Absent"
#         attendData[i.name] = attend
#     print(attendData)
#     return render(request,'attendance.html',{'stu':stu,'attendData':json.dumps(attendData)})

# def teacher(request):
#     # if 'email' in request.session.keys():
#         s1=user.objects.all().values()
#         return render(request,'teacher.html',{'s':s1})
#     # else:
#     #     return redirect("./tlogin")


# def deleteS(request):
#     roll=request.GET['sr']
#     s1=user.objects.filter(uroll=roll)
#     s1.delete()
#     return redirect('/Student/teacher')

# def updateS(request):
#     roll=request.GET['sr1']
#     s1=user.objects.get(uroll=roll)
#     return render(request,'updateS.html',{'s':s1})

# def updateSR(request):
#     n=request.GET['sr1']
#     s1=user.objects.get(uname=n)
#     return render(request,'updateSR.html',{'s':s1})


# def upsave(request):
#     # if request.method == 'POST':
#        roll = request.POST.get('r')
#        s1=user.objects.get(uroll=roll)
#        s1.uname=request.POST.get('n')
#        s1.uemail=request.POST.get('e')
#        s1.umob=request.POST.get('m')
#        s1.ubranch=request.POST.get('b')
#        s1.upaid=request.POST.get('p')
#        s1.ufine=request.POST.get('f')
#        s1.save()
#        print(request.POST.get('m'))
#        return redirect('/Student/teacher')

# def upsaveSR(request):
#     if request.method == 'POST':
#        n = request.POST.get('n')
#        s1=user.objects.get(uname=n)
#        s1.um=request.POST.get('m')
#        s1.uphy=request.POST.get('p')
#        s1.uchem=request.POST.get('c')
#        s1.uelec=request.POST.get('el')
#        s1.uelex=request.POST.get('ex')
#        s1.um2=request.POST.get('m2')
#        s1.uphy2=request.POST.get('p2')
#        s1.uchem2=request.POST.get('c2')
#        s1.uelec2=request.POST.get('el2')
#        s1.uelex2=request.POST.get('ex2')
#        s1.am=request.POST.get('ma')
#        s1.aphy=request.POST.get('pa')
#        s1.achem=request.POST.get('ca')
#        s1.aelec=request.POST.get('ela')
#        s1.aelex=request.POST.get('exa')
#        s1.save()
#        return redirect('/Student/teacher')


# def insert(request):
#     s1=user(uroll=request.POST['roll'],uname=request.POST['name'],uemail=request.POST['email'],umob=request.POST['contact'])
#     s1.save()
#     return redirect("/Student/teacher")
    

# def assign(req):
#     if 'student' in req.session.keys():
#         return render (req,'assignment.html') 
#     else :
#         return redirect("./index")

# def profile(request):
#     print("profile")
#     return render(request,'profile.html')

# def ajax2(req):
#     v=req.GET['val']
#     s1=user.objects.get(uname=v)
#     return render(req,'ajax.html',{'s1':s1})

# def result(request):
#     if 'student' in request.session.keys():
#         n=request.GET['srr']
#         return render(request,'result.html',{'n':n})
#     else :
#         return redirect("./index")

# def ajax2res(req):
#     v=req.GET['val']
#     v1=req.GET['val1']
#     s1=user.objects.get(uname=v1)
#     if (v=="Test 1"):
#         return render(req,'ajax2res.html',{'v':v,'s1':s1})
#     else:
#         return render(req,'ajax2res2.html',{'v':v,'s1':s1})

# def tlogin(req):
#     if 'email' in req.session.keys():
#         s1=teacherr.objects.get(temail = req.session['email'])
#         return redirect('/Student/teacher?s1=s1')
#     else :        
#         return render(req,'tlogin.html')

# def tcheck(request):
#     try:
#         t=request.POST['em']
#         s1=teacherr.objects.get(temail=request.POST['em'])
#         if(s1.tpass==request.POST['pswd']):
#             request.session['email'] = request.POST['em']
#             return redirect('/Student/teacher?s1=s1')
#         else:
#             messages.error(request, 'Incorrect password. Please try again.')
#             return redirect('/Student/tlogin')
#     except Exception as e: 
#         messages.error(request, 'This email is not registered with us.')
#         return redirect('/Student/tlogin')

# def fees(req):
#     if 'student' in req.session.keys():
#         n=req.GET['srr']
#         s1=user.objects.get(uname=n)
#         s1.upending=107325-s1.upaid
#         s1.save()
#         return render(req,'fees.html',{'s1':s1})
#     else :
#         return redirect("./index")

# def tsave(req):
#     obj=savee()
#     return render(req,'tsave.html',{'obj':obj})

# def ss(req):
#     s1=teacherr(temail=req.POST['email'],tpass=req.POST['password'])
#     s1.save()
#     return HttpResponse('done')

# def upattend(req):
#     if 'email' in req.session.keys():
#         s1=user.objects.all().values()
#         today=date.today()
#         return render(req,'upattend.html',{'s':s1,'today':today})
#     else:
#         return redirect("./tlogin")

# def attendsave(req):
#     s1=user.objects.all()
#     n=req.POST["1"]
#     for record in s1:
#         r=str(record.uroll)
#         attend=req.POST[r]
#         if attend=='p':
#             d=req.POST["date"]
#             if n=="submit1":
#                 record.jm[d]="Present"
#             elif n=="submit2":
#                 record.jp[d]="Present"
#             elif n=="submit3":
#                 record.jc[d]="Present"
#             elif n=="submit4":
#                 record.jel[d]="Present"
#             elif n=="submit5":
#                 record.jex[d]="Present"
#         else:
#             record.uattendance="Absent"
#             d=req.POST["date"]
#             if n=="submit1":
#                 record.jm[d]="Absent"
#             elif n=="submit2":
#                 record.jp[d]="Absent"
#             elif n=="submit3":
#                 record.jc[d]="Absent"
#             elif n=="submit4":
#                 record.jel[d]="Absent"
#             elif n=="submit5":
#                 record.jex[d]="Absent"
#         record.save()
#     return redirect('/Student/teacher')



# def logout(req):
#     if 'student' in req.session.keys():
#         del req.session['student']
#         return redirect('./index')
#     return redirect('./index')

# def tlogout(req):
#     if 'email' in req.session.keys():
#         del req.session['email']
#         return redirect('./tlogin')
#     return redirect('./tlogin')

