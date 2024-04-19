import datetime
import os
import smtplib
from django.core.mail import send_mail

from django.core.files.storage import FileSystemStorage
from django.db.models import Avg
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from myapp.pred import Disease
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

try:
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 8000))
    print('Starting development server at http://'+s.getsockname()[0]+':8000/')
except Exception as e:
    pass

from myapp.models import *


def admin_home(request):
    return render(request,'admin/admin index.html')
def login(request):
    return render(request,'login index.html')

def logout(request):
    request.session['lid'] = ''
    return redirect('/myapp/login/')

def login_post(request):
    username=request.POST['uname']
    password=request.POST['psw']
    a=Login.objects.filter(username=username,password=password)
    if a.exists():
        b = Login.objects.get(username=username, password=password)
        request.session['lid']=b.id
        if b.type=="admin":
            return redirect('/myapp/admin_home/')
        elif b.type=="doctor":
            return redirect('/myapp/doctor_home/')
        else:
            return HttpResponse('''<script>alert(" Invalid email/password... ");history.back();</script>''')
    else:
        return HttpResponse('''<script>alert(" Invalid email/password... ");history.back();</script>''')



# def add_symptoms(request):
#     var=Diease.objects.all()
#     if 'submit' in request.POST:
#         symptoms=request.POST['textfield']
#         disease=request.POST['disease']
#     return render(request,'admin/remedies',{'data':var})



def remedies(request,id):
    request.session["did"]=id
    data=Symptoms.objects.filter(DISEASE_id=id)

    return render(request,"admin/remedies view.html",{"data":data})

def add_remedies(request):
    var=Diease.objects.all()
    if 'submit' in request.POST:
        disease=request.POST['disease']
        symptoms=request.POST['textfield']

        a=Symptoms()
        a.symptoms=symptoms
        a.DISEASE=Diease.objects.get(id=disease)
        a.save()
        return HttpResponse('''<script>alert(" Added ");history.back();</script>''')


    return render(request, "admin/remedies.html",{'data':var})


    

def view_symptoms(request):
    var=Symptoms.objects.all()
    return render(request, "admin/view symptoms.html",{'data':var})

def view_review(request):
    var=Review.objects.all()
    return render(request, "admin/view reviews.html",{'data':var})
#
# def approve_doctor(request,id):
#     var=Login.objects.filter(id=id).update(type='doctor')
#     var2=Doctor.objects.filter(LOGIN_id=id).update(status='approved')
#     return HttpResponse('''<script>alert(" Approved ");history.back();</script>''')





from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Login, Doctor
from django.conf import settings

def approve_doctor(request, id):
    login = Login.objects.filter(id=id).first()
    if login:
        login.type = 'doctor'
        login.save()

        doctor = Doctor.objects.filter(LOGIN_id=id).first()
        if doctor:
            doctor.status = 'approved'
            doctor.save()

            # Send email notification
            recipient_email = doctor.email
            # print(recipient_email,"0000000000000000000000000000000")
            subject = 'Your registration has been approved'
            message = 'Dear Doctor, your registration has been approved.'
            sender_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, sender_email, [recipient_email])

            return HttpResponse('<script>alert("Approved"); history.back();</script>')

    return HttpResponse('<script>alert("Failed to approve doctor"); history.back();</script>')













def reject_doctor(request,id):
    var=Login.objects.filter(id=id).update(type='pending')
    var2=Doctor.objects.filter(LOGIN_id=id).update(status='rejected')
    return HttpResponse('''<script>alert(" Rejected ");history.back();</script>''')

def symptoms_delete(request,id):
    res=Symptoms.objects.get(id=id)
    res.delete()
    return HttpResponse('''<script>alert(" Deleted ");history.back();</script>''')


def SYMPTOMS_edit(request,id):
    var=Diease.objects.all()
    a=Symptoms.objects.get(id=id)
    return render(request,'admin/remedyedit.html',{'data':a,'data2':var})

def symptoms_edit_post(request):
    id = request.POST['id']
    

    disease=request.POST['disease']
    symptoms=request.POST['textfield']

    a=Symptoms.objects.get(id=id)
    a.symptoms=symptoms
    a.DISEASE=Diease.objects.get(id=disease)
    a.save()

    return HttpResponse('''<script>alert(" Added ");history.back();</script>''')













def forgot(request):
    return render(request, 'forgot.html')

def forgot_post(request):
    username=request.POST['textfield']
    a=Login.objects.filter(username=username)
    if a.exists():
        import random
        np = str(random.randint(00000000,99999999))
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('safedore3@gmail.com', 'yqqlwlyqbfjtewam')
        sub = 'Password Reset Mail'
        body = 'Your new password is '+np
        msg = 'Subject: '+sub+'\n\n'+body
        server.sendmail('DermaCare', username, msg)
        server.quit()
        Login.objects.filter(username=username).update(password=np)
        return HttpResponse('''<script>alert(" Password has been sent to the provided mail ... ");window.location='/myapp/login/'</script>''')
    return HttpResponse('''<script>alert(" No mail found in database... ");history.back();</script>''')


def change_password(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    return render(request,'admin/change password.html')

def change_password_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    oldpassword=request.POST['textfield']
    newpassword= request.POST['textfield3']
    confirmpassword= request.POST['textfield2']
    a=Login.objects.filter(password=oldpassword,id=request.session['lid'])
    if a.exists():
        if newpassword==confirmpassword:
            b = Login.objects.filter(password=oldpassword, id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert(" Updated ... ");window.location='/myapp/logout/'</script>''')
        else:
            return HttpResponse('''<script>alert(" passwords do not match... ");history.back();</script>''')
    else:
        return HttpResponse('''<script>alert(" current password do not match... ");history.back();</script>''')



def complaint(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    a=Compliant.objects.all().order_by('-date')
    return render(request,'admin/complaint.html',{'data':a})
def complaint_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    fromdate=request.POST['textfield']
    todate=request.POST["textfield2"]
    res=Compliant.objects.filter(date__range=[fromdate,todate]).order_by('-date')
    return render(request,'admin/complaint.html',{'data':res})



def disease_edit(request,id):
    a=Diease.objects.get(id=id)
    return render(request,'admin/disease edit.html',{'data':a})


def disease_edit_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')

    diseasename=request.POST['textfield']
    details=request.POST['textarea']
    # symptoms=request.POST['textfield2']
    id=request.POST['id']

    obj = Diease.objects.get(id=id)
    if 'image' in request.FILES:
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'

        image = request.FILES['image']
        fs=FileSystemStorage()
        fs.save(date,image)
        path=fs.url(date)
        obj.image=path

    obj.dieasename = diseasename
    obj.details = details
    # obj.symtoms = symptoms
    obj.save()
    return HttpResponse('''<script>alert(" Updated ... ");window.location='/myapp/disease_view/'</script>''')


def disease_view(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    res=Diease.objects.all()
    return render(request,'admin/disease view.html',{'data':res})
def disease_delete(request,id):
    res=Diease.objects.get(id=id)
    res.delete()
    return HttpResponse('''<script>alert(" Deleted ");window.location='/myapp/disease_view/'</script>''')


def disease_view_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    diseasename=request.POST['textfield']
    res=Diease.objects.filter(dieasename__icontains=diseasename)
    return render(request,'admin/disease view.html',{'data':res})

def disease(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    return render(request,'admin/disease.html')

def disease_post(request):

    if request.session['lid'] == '':
        return redirect('/myapp/login/')

    image = request.FILES['image']
    diseasename = request.POST['textfield']
    details = request.POST['textarea']
    # symptoms = request.POST['textfield2']

    fs=FileSystemStorage()
    date=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.jpg'
    fs.save(date,image)
    path=fs.url(date)

    obj=Diease()
    obj. dieasename=diseasename
    obj.details=details
    obj.image=path
    obj.save()

    return HttpResponse('''<script>alert(" successfully added");window.location='/myapp/admin_home/'</script>''')


def deletedoctor(request,id):
    a=Doctor.objects.get(id=id)
    Login.objects.filter(id=a.LOGIN_id).delete()
    try:
        a.delete()
    except:
        pass
    return HttpResponse('''<script>alert(" successfully deleted");window.location='/myapp/view_doctor/'</script>''')

def doctor_edit(request,id):
    a=Doctor.objects.get(id=id)

    return render(request,'admin/doctor edit.html',{'data':a})

def doctor_edit_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    id=request.POST['id']
    name=request.POST['textfield2']
    place=request.POST['textfield']
    age=request.POST['textfield3']
    email=request.POST['textfield10']
    gender=request.POST['RadioGroup1']
    qualification=request.POST['textfield4']
    pin=request.POST['textfield5']
    city=request.POST['textfield6']
    houseno=request.POST['textfield7']
    housename=request.POST['textfield8']
    mobileno=request.POST['textfield9']

    obj=Doctor.objects.get(id=id)

    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']
        fs = FileSystemStorage()
        import datetime
        date = 'doctor/'+datetime.datetime.now().strftime("%Y%m%d-%H%M%S%f") + ".jpg"
        fn = fs.save(date, photo)
        obj.photo = fs.url(date)

    obj.name = name
    obj.place = place
    obj.age = age
    obj.email = email
    obj.gender = gender
    obj.qualification = qualification
    obj.pin = pin
    obj.city = city
    obj.houseno = houseno
    obj.housename = housename
    obj.mobileno = mobileno
    obj.save()


    return HttpResponse('''<script>alert(" successfully ");window.location='/myapp/view_doctor/'</script>''')


def doctor_signup(request):

    return render (request,'doctor.html')
def doctor_post(request):
    name = request.POST['textfield2']
    place = request.POST['textfield']
    age = request.POST['textfield3']
    email = request.POST['textfield10']
    if Login.objects.filter(username__icontains=email).exists():
        return HttpResponse('''<script>alert(" Email already exists... ");history.back();</script>''')
    gender = request.POST['RadioGroup1']
    qualification = request.POST['textfield4']
    pin = request.POST['textfield5']
    city = request.POST['textfield6']
    houseno = request.POST['textfield7']
    housename = request.POST['textfield8']
    mobileno = request.POST['textfield9']
    photo = request.FILES['fileField']
    password = request.POST['password']
    confirmpasswrd = request.POST['comfirmpassword']

    if password==confirmpasswrd:
        lobj = Login()
        lobj.username = email
        lobj.password = password
        lobj.type = 'pending'
        lobj.save()

        obj = Doctor()
        obj.name = name
        obj.place = place
        obj.age = age
        obj.email = email
        obj.gender = gender
        obj.qualification = qualification
        obj.pin = pin
        obj.city = city
        obj.houseno = houseno
        obj.housename = housename
        obj.mobileno = mobileno
        fs = FileSystemStorage()
        import datetime
        date = 'doctor/'+datetime.datetime.now().strftime("%Y%m%d-%H%M%S%f") + ".jpg"
        fn = fs.save(date, photo)
        obj.photo = fs.url(date)
        obj.LOGIN = lobj
        obj.save()
        return HttpResponse('''<script>alert(" successfully ");window.location='/myapp/login/'</script>''')
    return HttpResponse('''<script>alert(" Passwords do not match... ");history.back();</script>''')

def send_replay(request,id):
    res=Compliant.objects.get(id=id)
    return render(request,'admin/send reply.html',{'data':res})
def send_reply_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    reply=request.POST['textarea']
    did=request.POST['id1']
    obj=Compliant.objects.get(id=did)
    obj.reply=reply
    obj.status='replied'
    obj.save()
    return HttpResponse('''<script>alert(" successfully replied");window.location='/myapp/complaint/'</script>''')

def view_doctor(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    res=Doctor.objects.all()
    return render(request,'admin/view doctor.html',{'data':res})

def view_doctor_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    name=request.POST['textfield']
    res=Doctor.objects.filter(name__icontains=name)
    return render(request,'admin/view doctor.html',{'data':res})


def view_feedback(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    res=Feedback.objects.all()
    return render(request,'admin/view feedback.html',{'data':res})
def view_feedback_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    fromdate=request.POST['textfield']
    todate = request.POST['textfield2']
    a=Feedback.objects.filter(date__range=[fromdate,todate])
    return render(request,'admin/view feedback.html',{'data':a})




def VIEW_USER(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    res=User.objects.all()
    return render(request,'admin/VIEW USER.html',{'data':res})
def view_user_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    name=request.POST['textfield']
    res=User.objects.filter(name__icontains=name)
    return render(request,'admin/VIEW USER.html',{'data':res})

#================= doctor


def doctor_home(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    return render(request,'doctors/doctor index main.html')



def edit_profile(request):
    var=Doctor.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'doctors/edit profile.html',{'data':var})



def edit_profile_post(request):
    name = request.POST['textfield2']
    id=request.POST['id']
    place = request.POST['textfield']
    age = request.POST['textfield3']
    email = request.POST['textfield10']
   
    qualification = request.POST['textfield4']
    pin = request.POST['textfield5']
    city = request.POST['textfield6']
    houseno = request.POST['textfield7']
    housename = request.POST['textfield8']
    mobileno = request.POST['textfield9']
    

    

    obj = Doctor.objects.get(id=id)
    obj.name = name
    obj.place = place
    obj.age = age
    obj.email = email
    obj.qualification = qualification
    obj.pin = pin
    obj.city = city
    obj.houseno = houseno
    obj.housename = housename
    obj.mobileno = mobileno

    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']

        fs = FileSystemStorage()
        import datetime
        date = 'doctor/'+datetime.datetime.now().strftime("%Y%m%d-%H%M%S%f") + ".jpg"
        fn = fs.save(date, photo)
        obj.photo = fs.url(date)

    
    obj.LOGIN = Login.objects.get(id=request.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert(" successfully ");window.location='/myapp/view_profile/'</script>''')

def add_schedule(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    dt = datetime.date.today()
    return render(request,'doctors/add shedule.html',{'dt':str(dt)})
def add_shedule_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    date=request.POST['date']
    fromtime=request.POST['time']
    totime=request.POST['time2']
    if Schedule.objects.filter(fromtime=fromtime,totime=totime,date=date, DOCTOR=Doctor.objects.get(LOGIN=request.session['lid'])).exists():
        return HttpResponse('''<script>alert(" Schedule already exists... ");history.back();</script>''')
    sobj=Schedule()
    sobj.fromtime=fromtime
    sobj.totime=totime
    sobj.date=date
    sobj.DOCTOR=Doctor.objects.get(LOGIN=request.session['lid'])
    sobj.save()
    return HttpResponse('''<script>alert("Schedule Added Successfully ");window.location='/myapp/add_schedule/'</script>''')

def doctor_disease_view(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    res=Diease.objects.all()
    return render(request,'doctors/disease view.html',{'data':res})

def doctors_disease_view_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    name=request.POST['textfield']
    res = Diease.objects.filter(dieasename__icontains=name)
    return render(request, 'doctors/disease view.html', {'data': res})






def doctor_change_password(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    return render(request,'doctors/doctor change password.html')
def doctors_change_password_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    oldpassword=request.POST['textfield']
    newpassword= request.POST['textfield3']
    confirmpassword= request.POST['textfield2']
    a = Login.objects.filter(password=oldpassword, id=request.session['lid'])
    if a.exists():
        if newpassword == confirmpassword:
            b = Login.objects.filter(password=oldpassword, id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert(" Updated ... ");window.location='/myapp/logout/'</script>''')
        else:
            return HttpResponse('''<script>alert(" passwords do not match... ");history.back();</script>''')
    else:
        return HttpResponse('''<script>alert(" current password do not match... ");history.back();</script>''')


def delete_schedule(request,id):
    res = Schedule.objects.filter(pk=id).delete()
    return redirect('/myapp/view_schedule/')

def edit_shedule(request,id):
    res=Schedule.objects.get(pk=id)
    dt = datetime.date.today()
    return render(request,'doctors/edit shedule.html',{'data':res,'dt':str(dt)})

def edit_shedule_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    id=request.POST['id']
    date=request.POST['date']
    fromtime=request.POST['time']
    totime=request.POST['time2']
    sobj=Schedule.objects.get(pk=id)
    sobj.date=date
    sobj.fromtime=fromtime
    sobj.totime=totime
    sobj.save()
    return HttpResponse('''<script>alert(" Edit Schedule... ");window.location='/myapp/view_schedule/'</script>''')

def view_appointment(request,id):
    res=Appointment.objects.filter(SCHEDULE=id)
    request.session['sid']=id
    return render(request, 'doctors/view appointment.html',{'data':res})

def doctor_view_symptoms(request,id):
    vr=Symptoms.objects.filter(DISEASE=id)
    return render(request,'doctors/view symptom.html',{'data':vr})

def view_appointment_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    res = Appointment.objects.filter(SCHEDULE=request.session['sid'],date__range=[fromdate,todate])
    return render(request, 'doctors/view appointment.html',{'data':res})

def  view_schedule(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    res=Schedule.objects.filter(DOCTOR__LOGIN_id=request.session['lid'])
    return render(request, 'doctors/view schedule.html',{'data':res})

def view_schedule_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    res = Schedule.objects.filter(DOCTOR__LOGIN_id=request.session['lid'],date__range=[fromdate,todate])
    return render(request, 'doctors/view schedule.html', {'data': res})

def  view_reviews(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    res=Review.objects.filter(DOCTOR__LOGIN_id=request.session['lid'])
    return render(request, 'doctors/view reviews.html', {'data': res})

def view_review_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    res = Review.objects.filter(DOCTOR__LOGIN_id=request.session['lid'],date__range=[fromdate,todate])
    return render(request, 'doctors/view reviews.html', {'data': res})



#
# def terminate_doctor(request,id):
#     var=Login.objects.filter(id=id).update(type='pending')
#     var2=Doctor.objects.filter(id=id).update(status='pending')
#     return HttpResponse('''<script>alert(" rejected ");window.location='/myapp/view_profile/'</script>''')



from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Review, Doctor, Login


def terminate_doctor(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    doctor = review.DOCTOR

    doctor.status = 'pending'
    doctor.save()

    doctor_login = Login.objects.get(id=doctor.id)
    doctor_login.type = 'pending'
    doctor_login.save()

    return HttpResponse('''<script>alert("Doctor terminated");window.location='/myapp/view_review/'</script>''')


def view_profile(request):
    if request.session['lid'] == '':
        return redirect('/myapp/login/')
    res=Doctor.objects.get(LOGIN=request.session['lid'])
    return render(request, 'doctors/view_profile.html',{'data':res})


#
#
# Android
# @csrf_exempt
# def and_login(request):
#     username=request.POST['username']
#     password=request.POST['password']
#     a=Login.objects.filter(username=username,password=password)
#     if a.exists():
#         b = Login.objects.get(username=username, password=password)
#         if b.type=="user":
#             return JsonResponse({'status':'ok', 'lid':b.id})
#     return JsonResponse({'status': 'no'})


def and_login(request):
    username=request.POST['username']
    password=request.POST['password']

    var=Login.objects.filter(username=username,password=password)
    if var.exists():
        var2 = Login.objects.get(username=username, password=password)
        if var2.type=='user':
            return JsonResponse({'status': 'ok', 'lid': str(var2.id), 'type': var2.type})
      

        else:
            return JsonResponse({'status': 'not ok'})
    else:
        return JsonResponse({'status': 'not ok'})



@csrf_exempt
def and_signup(request):
    name=request.POST['name']
    age=request.POST['age']
    houseno=request.POST['houseno']
    housename=request.POST['house']
    place=request.POST['place']
    # gender=request.POST['gender']
    pin=request.POST['pin']
    email=request.POST['email']
    password=request.POST['password']
    phoneNumber=request.POST['phoneNumber']
    photo=request.POST['photo']
    if Login.objects.filter(username=email).exists():
        return JsonResponse({'status': 'no'})

    a=Login()
    a.username = email
    a.password = password
    a.type = 'user'
    a.save()

    b = User()
    b.LOGIN=a
    b.name = name
    b.age = age
    b.houseno = houseno
    b.housename = housename
    b.place = place
    # b.gender = _gender
    b.pin = pin
    b.email = email
    b.mobileno = phoneNumber
    import base64
    c = base64.b64decode(photo)
    dt = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')+'.jpg'
    open(r'D:\aiii\Disease_Expert\Disease_Expert\media\user\\'+dt, 'wb').write(c)
    
    b.photo = '/media/user/'+dt
    b.save()
    return JsonResponse({'status': 'ok'})

# @csrf_exempt
# def and_change_password(request):
#     lid=request.POST['lid']
#     current=request.POST['current']
#     newpass=request.POST['newpass']
#     a=Login.objects.filter(id=lid,password=current)
#     if a.exists():
#         Login.objects.filter(id=lid,password=current).update(password=newpass)
#         return JsonResponse({'status':'ok'})
#     return JsonResponse({'status': 'no'})


def user_changepassword(request):
    lid = request.POST['lid']
    old = request.POST['old']
    newpass = request.POST['new']
    confirm = request.POST['confirm']

    var = Login.objects.filter(id=lid, password=old)
    if var.exists():
        if newpass == confirm:
            var2 = Login.objects.filter(id=lid).update(password=confirm)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'Not ok'})
    else:
        return JsonResponse({'status': 'NoT Ok'})



def user_view_profile(request):
    lid=request.POST['lid']
    var=User.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok','name':var.name,'age':var.age,'houseno':var.houseno,

                         'contact':var.mobileno,'email':var.email,
                         'housename':var.housename,'place':var.place,'pin':var.pin,
                         'image':var.photo})




@csrf_exempt
def and_view_doctors(request):
    data = request.POST['data']
    res=Doctor.objects.filter()
    l = []
    for i in res:
        rt = 0
        ct = 0
        rev = Review.objects.filter(DOCTOR_id=i.id)
        if rev.exists():
            rt = rev.aggregate(Avg('Rating'))['Rating__avg']
            ct = len(rev)
        l.append({
            'id': i.id,
            'name': i.name,
            'photo': i.photo,
            'qualification': i.qualification,
            'rt': str(rt),
            'ct': str(ct),
        })
    return JsonResponse({'status': 'ok', 'data':l})

@csrf_exempt
def and_view_doctors_search(request):
    data = request.POST['data']
    res=Doctor.objects.filter(name__icontains=data)
    l = []
    for i in res:
        rt = 0
        ct = 0
        rev = Review.objects.filter(DOCTOR_id=i.id)
        if rev.exists():
            rt = rev.aggregate(Avg('Rating'))['Rating__avg']
            ct = len(rev)
        l.append({
            'id': i.id,
            'name': i.name,
            'photo': i.photo,
            'qualification': i.qualification,
            'rt': str(rt),
            'ct': str(ct),
        })
    return JsonResponse({'status': 'ok', 'data':l})

@csrf_exempt
def and_view_doctors_home(request):
    res=Doctor.objects.all()[0:4]
    l = []
    for i in res:
        rt = 0
        ct = 0
        rev = Review.objects.filter(DOCTOR_id=i.id)
        if rev.exists():
            rt = rev.aggregate(Avg('Rating'))['Rating__avg']
            ct = len(rev)
        l.append({
            'id': i.id,
            'name': i.name,
            'photo': i.photo,
            'qualification': i.qualification,
            'rt': str(rt),
            'ct': str(ct),
        })
    return JsonResponse({'status': 'ok', 'data':l})

@csrf_exempt
def and_view_schedules(request):
    did = request.POST['did']
    res=Schedule.objects.filter(DOCTOR_id=did, date__gte=datetime.date.today())
    l = []
    for i in res:
        l.append({
            'id': i.id,
            'date': i.date,
            'fromtime': i.fromtime,
            'totime': i.totime,
        })
    return JsonResponse({'status': 'ok', 'data':l})

@csrf_exempt
def and_take_appointment(request):
    lid = request.POST['lid']
    aid = request.POST['aid']
    a = Appointment()
    a.SCHEDULE_id = aid
    a.time = datetime.datetime.now().time()
    a.date = datetime.date.today()
    a.USER = User.objects.get(LOGIN_id=lid)
    a.save()
    return JsonResponse({'status': 'ok'})

@csrf_exempt
def and_view_appointments_today(request):
    lid = request.POST['lid']
    try:
        i=Appointment.objects.filter(USER__LOGIN_id=lid, SCHEDULE__date=datetime.date.today())[0]
        l = {
            'id': i.id,
            'doctor': i.SCHEDULE.DOCTOR.name,
            'qual': i.SCHEDULE.DOCTOR.qualification,
            'photo': i.SCHEDULE.DOCTOR.photo,
            'date': i.SCHEDULE.date,
            'fromtime': i.SCHEDULE.fromtime,
            'totime': i.SCHEDULE.totime,
        }
        print(l)
        return JsonResponse({'status': 'ok', 'data': l})
    except:
        return JsonResponse({'status': 'no'})


@csrf_exempt
def and_view_appointments(request):
    lid = request.POST['lid']
    res=Appointment.objects.filter(USER__LOGIN_id=lid).order_by('-SCHEDULE__date')
    l = []
    for i in res:
        l.append({
            'id': i.SCHEDULE.DOCTOR.LOGIN.id,
            'doctor': i.SCHEDULE.DOCTOR.name,
            'qual': i.SCHEDULE.DOCTOR.qualification,
            'photo': i.SCHEDULE.DOCTOR.photo,
            'date': i.SCHEDULE.date,
            'fromtime': i.SCHEDULE.fromtime,
            'totime': i.SCHEDULE.totime,
        })
    return JsonResponse({'status': 'ok', 'data':l})




@csrf_exempt
def and_view_profile(request):
    lid = request.POST['lid']
    i=User.objects.get(LOGIN_id=lid)
    l={
        'name': i.name,
        'place': i.place,
        'age': i.age,
        # 'gender': i.gender,
        'photo': i.photo,
        'pin': i.pin,
        'housename': i.housename,
        'houseno': i.houseno,
        'mobileno': i.mobileno,
        'email': i.email,
    }
    return JsonResponse({'status': 'ok', 'data':l})

@csrf_exempt

def and_edit_profile(request):
    _userName=request.POST['name']
    _age=request.POST['age']
    # _gender=request.POST['_gender']
    _hno=request.POST['houseno']
    _hname=request.POST['housename']
    _place=request.POST['place']
    _pin=request.POST['pin']
    _email=request.POST['email']
    _phoneNumber=request.POST['contact']
    photo=request.POST['image']
    lid=request.POST['lid']

    b = User.objects.get(LOGIN_id=lid)
    b.name = _userName
    b.age = _age
    # b.gender = _gender
    b.houseno = _hno
    b.housename = _hname
    b.place = _place
    b.pin = _pin
    b.email = _email
    b.mobileno = _phoneNumber
    if len(photo)>5:
        import base64
        c = base64.b64decode(photo)
        dt = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')+'.jpg'
        open(r'D:\disease 6-3-24\web part\Disease_Expert\media\user\\'+dt, 'wb').write(c)
        b.photo = '/media/user/'+dt
    b.save()
    return JsonResponse({'status': 'ok'})



@csrf_exempt
def and_send_complaint(request):
    lid = request.POST['lid']
    complaint = request.POST['complaint']
    a = Compliant()
    a.complain = complaint
    a.status = 'pending'
    a.reply = 'pending'
    a.time = datetime.datetime.now().time()
    a.date = datetime.date.today()
    a.USER = User.objects.get(LOGIN_id=lid)
    a.save()
    return JsonResponse({'status': 'ok'})

@csrf_exempt
def and_send_feedback(request):
    lid = request.POST['lid']
    feedback = request.POST['feedback']
    a = Feedback()
    a.feeedback = feedback
    a.time = datetime.datetime.now().time()
    a.date = datetime.date.today()
    a.USERNAME = User.objects.get(LOGIN_id=lid)
    a.save()
    return JsonResponse({'status': 'ok'})

@csrf_exempt
def and_view_complaints(request):
    lid = request.POST['lid']
    res=Compliant.objects.filter(USER__LOGIN_id=lid).order_by('-id')
    l = []
    for i in res:
        l.append({
            'id': i.id,
            'date': i.date,
            'complain': i.complain,
            'reply': i.reply,
            'status': i.status,
        })
    return JsonResponse({'status': 'ok', 'data':l})

@csrf_exempt
def and_view_diseases(request):
    lid = request.POST['lid']
    res=Diease.objects.filter().order_by('dieasename')
    l = []
    for i in res:
        l.append({
            'id': i.id,
            'dieasename': i.dieasename,
            'details': i.details,
            'symtoms': i.symtoms,
        })
    return JsonResponse({'status': 'ok', 'data':l})

@csrf_exempt
def and_file_upload(request):
    photo = request.POST['photo']

    import time
    import base64

    timestr = time.strftime("%Y%m%d%H%M%S")
    a = base64.b64decode(photo)
    fh = open(r"C:\Users\saik1\PycharmProjects\DERMA_CARE\media\disease_prediction\\" + timestr + ".jpg", "wb")
    fh.write(a)
    fh.close()



    md = r"C:\Users\saik1\PycharmProjects\DERMA_CARE\media\disease_prediction\\" + timestr + ".jpg"
    import numpy as np
    from skimage import io, color, img_as_ubyte

    from skimage.feature import graycomatrix, graycoprops

    rgbImg = io.imread(md)
    grayImg = img_as_ubyte(color.rgb2gray(rgbImg))

    distances = [1, 2, 3]
    angles = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]
    properties = ['energy', 'homogeneity']

    glcm = graycomatrix(grayImg,
                            distances=distances,
                            angles=angles,
                            symmetric=True,
                            normed=True)

    feats = np.hstack([graycoprops(glcm, 'homogeneity').ravel() for prop in properties])
    feats1 = np.hstack([graycoprops(glcm, 'energy').ravel() for prop in properties])
    feats2 = np.hstack([graycoprops(glcm, 'dissimilarity').ravel() for prop in properties])
    feats3 = np.hstack([graycoprops(glcm, 'correlation').ravel() for prop in properties])
    feats4 = np.hstack([graycoprops(glcm, 'contrast').ravel() for prop in  properties])
    k = np.mean(feats)
    l = np.mean(feats1)
    m = np.mean(feats2)
    n = np.mean(feats3)
    o = np.mean(feats4)

    test = [[k, l, m, n, o]]
    res = Dataset.objects.all()

    attribut = []
    lables = []

    for i in res:
        features = [float(i.homogeneity), float(i.energy), float(i.dissimilarity), float(i.correlation), float(i.contrast)]

        lables.append(i.disease)
        attribut.append(features)

    attribut = np.array(attribut)
    lables = np.array(lables)



    from sklearn.ensemble import RandomForestClassifier
    rnd = RandomForestClassifier()
    rnd.fit(attribut, lables)
    k = rnd.predict(np.array(test))

    diseaseName = k[0]
    res2=Diease.objects.get(dieasename__icontains=diseaseName)

    if res is not None:
        return JsonResponse({"status":"ok", "diseasesname":res2.dieasename, "details":res2.details, "symtoms":res2.symtoms})
    else:
        return JsonResponse({"status":"no"})


def chat(request,id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = User.objects.get(LOGIN=cid)

    return render(request, "doctors/Chat.html", {'photo': qry.photo, 'name': qry.name, 'toid': cid})

def chat_view(request):
    fromid = request.session['lid']
    toid = request.session["userid"]
    qry = User.objects.get(LOGIN=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid)).order_by('id')
    l = []

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TOID_id, "date": i.date, "from": i.FROMID_id})

    return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.name, 'toid': request.session["userid"]})

def chat_send(request, msg):
    lid = request.session['lid']
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TOID_id = toid
    chatobt.FROMID_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})


# @csrf_exempt
# def User_sendchat(request):
#     FROM_id=request.POST['from_id']
#     TOID_id=request.POST['to_id']
#     msg=request.POST['message']

#     from  datetime import datetime
#     c=Chat()
#     c.FROMID_id=FROM_id
#     c.TOID_id=TOID_id
#     c.message=msg
#     c.date=datetime.now()
#     c.save()
#     return JsonResponse({'status':"ok"})


@csrf_exempt
# def User_viewchat(request):
#     fromid = request.POST["from_id"]
#     toid = request.POST["to_id"]
#     from django.db.models import Q

#     res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid)).order_by('id')
#     l = []

#     for i in res:
#         l.append({"id": i.id, "msg": i.message, "from": i.FROMID_id, "date": i.date, "to": i.TOID_id})

#     return JsonResponse({"status":"ok",'data':l})

@csrf_exempt
def User_send_review(request):
    lid=request.POST['lid']
    did=request.POST['did']
    Reviews=request.POST['review']
    Rating=request.POST['rating']

    from  datetime import datetime
    c=Review()
    c.USER=User.objects.get(LOGIN_id=lid)
    c.DOCTOR_id=did
    c.Review=Reviews
    c.Rating=Rating
    c.date=datetime.now().date()
    c.time=datetime.now().time()
    c.save()
    return JsonResponse({'status':"ok"})



def User_appointmentsend_review(request):
    lid=request.POST['lid']
    did=request.POST['did']
    Reviews=request.POST['review']

    from  datetime import datetime
    c=AppoinmentReview()
    c.USER=User.objects.get(LOGIN_id=lid)
    c.APPOINTMENT_id=did
    c.Review=Reviews
    c.date=datetime.now().date()
    c.save()
    return JsonResponse({'status':"ok"})




@csrf_exempt
def User_view_review(request):
    did = request.POST["did"]

    res = Review.objects.filter(DOCTOR_id=did)
    l = []

    for i in res:
        l.append({
            "id": i.id,
            "USER": i.USER.name,
            "photo": i.USER.photo,
            "Review": i.Review,
            "Rating": i.Rating,
            "date": i.date,
            "time": i.time,
          })

    return JsonResponse({"status":"ok",'data':l})




def user_view_doctor(request):
    var=Doctor.objects.all()
    l=[]

    for i in var:
        l.append({'id':i.id,'name':i.name,'photo':i.photo,'qualification':i.qualification,'login_id':i.LOGIN_id})
    print(l)
    return JsonResponse({"status":"ok",'data':l})


def view_doctor_schedule(request):
    sid=request.POST['did']

    var=Schedule.objects.filter(DOCTOR_id=sid)
    l = []

    for i in var:
        l.append({'id': i.id, 'date': i.date, 'fromtime': i.fromtime, 'totime': i.totime})
    return JsonResponse({"status": "ok", 'data': l})


def take_appointment(request):
    lid=request.POST['lid']
    aid=request.POST['aid']

    a=Appointment.objects.filter(SCHEDULE_id=aid,USER__LOGIN_id=lid)
    if a.exists():
        return JsonResponse({"status": "Not ok"})



    var=Appointment()
    var.SCHEDULE=Schedule.objects.get(id=aid)
    var.USER=User.objects.get(LOGIN_id=lid)
    var.date=datetime.datetime.now().today().date()
    var.time=datetime.datetime.now().time()
    var.save()
    return JsonResponse({"status": "ok"})



def send_feedback(request):
    lid=request.POST['lid']
    feeedback=request.POST['feedback']
    var=Feedback()
    var.USER=User.objects.get(LOGIN_id=lid)
    var.feeedback=feeedback
    var.date=datetime.datetime.now().today().date()
    var.time=datetime.datetime.now().time()
    var.save()
    return JsonResponse({"status": "ok"})


def view_appointments(request):
    lid=request.POST['lid']
    var=Appointment.objects.filter(USER__LOGIN_id=lid)
    l = []

    for i in var:
        l.append({'id': i.id, 'DOCTOR': i.SCHEDULE.DOCTOR.name, 'fromtime': i.SCHEDULE.fromtime, 
            'dlid': i.SCHEDULE.DOCTOR.LOGIN_id,
                   'totime': i.SCHEDULE.totime,'date':i.SCHEDULE.date,'Adate':i.date,'photo':i.SCHEDULE.DOCTOR.photo})
    return JsonResponse({"status": "ok", 'data': l})




def User_sendchat(request):
    FROM_id=request.POST['from_id']
    TOID_id=request.POST['to_id']
    print(FROM_id)
    print(TOID_id)
    msg=request.POST['message']
    # res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid))

    from  datetime import datetime
    c=Chat()
    c.FROMID_id=FROM_id
    c.TOID_id=TOID_id
    c.message=msg
    c.date=datetime.now()
    c.save()
    return JsonResponse({'status':"ok"})

from django.db.models import Q

def User_viewchat(request):
    fromid = request.POST["from_id"]
    toid = request.POST["to_id"]
    # lmid = request.POST["lastmsgid"]    from django.db.models import Q

    # res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid))
    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid)).order_by('id')
    l = []

    for i in res:
        l.append({"id": i.id, "msg": i.message, "from": i.FROMID_id, "date": i.date, "to": i.TOID_id})

    return JsonResponse({"status":"ok",'data':l})


def predict_symptoms(request):
    symptoms=request.POST['symptoms']
    d=symptoms.split(",")
    s=""
    for i in d:
        if i!="":
            if s!="":
                s+=","+i
            else:
                s=i
    d=Disease()
    res=d.predictDisease(s)
    category=""
    specialization={
                "Fungal infection": "Dermatology",
                "Allergy":"Allergist and Clinical Immunologist",
                "Diabetes":"Endocrinologist",
                "Bronchial Asthma":"Pulmonologist",
                "Hypertension ":"Cardiology",
                "Migraine":"Neurology",
                "Malaria":"General Physician/ Internal Medicine",
                "Chicken pox":"General Physician/ Internal Medicine",
                "Drug Reaction":"General Physician/ Internal Medicine",
                "Dengue":"General Physician/ Internal Medicine",
                "Typhoid":"General Physician/ Internal Medicine",
                "Common Cold":"General Physician/ Internal Medicine",
                "Pneumonia":"Pulmonology/ Respiratory Medicine",
                "Heart attack":"Cardiology",
                "VaricoseD veins":"Pain Management",
                "Gastroenteritis":"Endocrinology ",

            }
    try:
        category=specialization[res]
    except Exception as ex:
        category="Common issues"
    if res=="GERD":
        img="/static/project_folder/20220729140350.jpg"
        consult="Consult Endocrinology"
    elif res=="Fungal infection":
        img="/static/project_folder/20220714120052.jpg"
        consult="Consult Dermatologist"
    else:
        img="/static/project_folder/20220729140350.jpg"
        consult="Consult General medicine"
    return JsonResponse({"status":"ok",'result':res,'category':category,'consult':consult,'img':img})




#
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.models import load_model
# import numpy as np
#
#
#
#
# # Load the trained model
# loaded_model = load_model("D:\\aiii\\Disease_Expert\\Disease_Expert\\new__model_new.h5",compile=False)  # Use the path where you saved your trained model
# print("patnilla")
# # Function to preprocess the image for prediction
# def preprocess_image(image_path):
#     img = image.load_img(image_path, target_size=(150, 150))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0  # Normalize the image
#     predictions = loaded_model.predict(img_array)
#     class_labels = ['Akne','Benign','Ekzama','Enfeksiyonel','Malign','Pigment']
#     predicted_class_index = np.argmax(predictions)
#     predicted_class_label = class_labels[predicted_class_index]
#     print(predicted_class_label,';;;;;;;;;;;;;;;;;;;;;;;;;')
#     return predicted_class_label
#

# Example usage:


# Make predictions

# Map predicted class index to label
# class_labels = ['Akne','Benign','Ekzama','Enfeksiyonel','Malign','Pigment']
# predicted_class_index = np.argmax(predictions)
# predicted_class_label = class_labels[predicted_class_index]

# print("Predicted Class:", predicted_class_label)

# preprocess_image(r"D:\aiii\Disease_Expert\Disease_Expert\media\disease_prediction\20240129-233342.jpg")


# def predict_skin(request):
#
#     image=request.POST['photo']
#     path="D:\\aiii\\Disease_Expert\\Disease_Expert\\media\\disease_prediction\\a.jpg"
#     import base64
#
#     ba=base64.b64decode(image)
#     with open(path,"wb") as f:
#         f.write(ba)
#         f.close()
#     res="ok"
#     print(path,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#     res=preprocess_image(path)
#     print(res,'//////////////////////////////////////////////////')
#     return JsonResponse({'status':'ok','result':res})