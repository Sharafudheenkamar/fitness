import string
from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from Fitnesspro import settings
from myapp.models import *
from django.core.mail import send_mail
from django.conf import settings


def login(request):
    return render(request,'newlogin.html')

def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    var=Login.objects.filter(username=username,password=password)
    if var.exists():
        Log=Login.objects.get(username=username,password=password)
        request.session['lid']=Log.id
        if Log.type=='Admin':
            return HttpResponse('''<script>alert('Login success');window.location='/myapp/admin_homepage/'</script>''')
        elif Log.type == 'trainer':
            return HttpResponse('''<script>alert('Login success');window.location='/myapp/trainer_homepage/'</script>''')
        elif Log.type == 'user':
            return HttpResponse('''<script>alert('Login success');window.location='/myapp/user_homepage/'</script>''')


        else:
            return HttpResponse('''<script>alert('invalid');window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid');window.location='/myapp/login/'</script>''')



def admin_addtrainers(request):
    import datetime
    dt = datetime.date.today()
    dt = str(dt.year - 18) + "-" + str(dt.month) + "-" + str(dt.day)
    return render(request,'admin/add trainers.html',{'dt':dt})
def admin_addtrainers_post(request):
    name=request.POST['textfield']
    gender=request.POST['RadioGroup1']
    dob=request.POST['textfield2']
    place=request.POST['textfield3']
    email=request.POST['textfield4']
    phone=request.POST['textfield5']

    certificate=request.FILES['fileField']
    from datetime import datetime
    date1 ="p1"+ datetime.now().strftime('%Y%M%D-%H%M%S') + '.jpg'
    fs1 = FileSystemStorage()
    fs1.save(date1, certificate)
    path1 = fs1.url(date1)

    photo=request.FILES['fileField2']
    date ="p2"+datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
    fs = FileSystemStorage()
    fs.save(date, photo)
    path = fs.url(date)

    ob=Login()
    ob.username=email
    ob.password=phone
    ob.type='trainer'
    ob.save()

    var=Trainer()
    var.LOGIN=ob
    var.name=name
    var.dob=dob
    var.gender=gender
    var.place=place
    var.email=email
    var.phone=phone
    var.certificate=path1
    var.photo=path
    var.save()
    return HttpResponse('''<script>alert('Added successfully');window.location='/myapp/admin_homepage/'</script>''')


def admin_viewtrainers(request):
    data=Trainer.objects.all()
    return render(request,'admin/view trainers.html',{'dt':data})
def admin_viewtrainers_post(request):
    search=request.POST['textfield']
    data=Trainer.objects.filter(name__icontains=search)
    return render(request,'admin/view trainers.html',{'dt':data})


def admin_updatetrainers(request,tid):
    a=Trainer.objects.get(id=tid)
    return render(request,'admin/update trainers.html',{'data':a})
def admin_updatetrainers_post(request):
    tid = request.POST['tid']
    name = request.POST['textfield']
    gender = request.POST['RadioGroup1']
    dob = request.POST['textfield2']
    place = request.POST['textfield3']
    email = request.POST['textfield4']
    phone = request.POST['textfield5']
    from datetime import datetime
    if 'fileField' in request.FILES:
        certificate = request.FILES['fileField']
        date1 = "p1" + datetime.now().strftime('%Y%M%D-%H%M%S') + '.jpg'
        fs1 = FileSystemStorage()
        fs1.save(date1, certificate)
        path1 = fs1.url(date1)
        obj=Trainer.objects.filter(id=tid).update(certificate=path1)
    elif    'fileField2' in request.FILES:
        photo = request.FILES['fileField2']
        date = "p2" + datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        obj = Trainer.objects.filter(id=tid).update(photo=path)
    obj = Trainer.objects.filter(id=tid).update(name=name,dob=dob,gender=gender,email=email,phone=phone,place=place)
    return HttpResponse('''<script>alert('updated successfully');window.location='/myapp/admin_viewtrainers/'</script>''')

def admin_deletetrainer(request,id):
    data=Trainer.objects.get(id=id)
    Login.objects.filter(id=data.LOGIN_id).delete()
    return HttpResponse('''<script>alert('deleted successfully');window.location='/myapp/admin_viewtrainers/'</script>''')


def admin_viewuser(request):
    data=User.objects.all()
    return render(request,'admin/view user.html',{'dt':data})
def admin_viewuser_post(request):
    search=request.POST['textfield']
    data=User.objects.filter(name__icontains=search)
    return render(request,'admin/view user.html',{'dt':data})


def admin_viewusermoredetails(request,id):
    data=User.objects.get(id=id)
    return render(request,'admin/view users more detailss.html',{'dt':data})


def admin_addcategory(request):
    return render(request,'admin/add category.html')
def admin_addcategory_post(request):
    categoryname=request.POST['textfield']

    var = Category()
    var.categoryname=categoryname
    var.save()
    return HttpResponse('''<script>alert('Added successfully');window.location='/myapp/admin_homepage/'</script>''')


def admin_viewcategory(request):
    data=Category.objects.all()
    return render(request,'admin/view category.html',{'dt':data})


def admin_viewcategory_post(request):
    search=request.POST['textfield']
    data=Category.objects.filter(categoryname__icontains=search)
    return render(request,'admin/view category.html',{'dt':data})



def admin_editcategory(request,cid):
    a=Category.objects.get(id=cid)
    return render(request,'admin/edit category.html',{'data':a})
def admin_editcategory_post(request):
    cid=request.POST['cid']
    categoryname=request.POST['textfield']
    obj = Category.objects.filter(id=cid).update(categoryname=categoryname)
    return HttpResponse('''<script>alert('updated successfully');window.location='/myapp/admin_viewcategory/'</script>''')

def admin_deletecategory(request,id):
    data=Category.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert('deleted successfully');window.location='/myapp/admin_viewcategory/'</script>''')


def admin_viewusercomplaint(request):
    b=Complaint.objects.all()
    return render(request,'admin/view user complaint.html',{'data':b})
def admin_viewusercomplaint_post(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    a=Complaint.objects.filter(date__range=[fromdate,todate])
    return render(request,'admin/view user complaint.html',{'data':a})



def admin_usercomplaintreply(request,id):
    res=Complaint.objects.get(id=id)
    return render(request,'admin/sent complaint reply.html',{'data':res})

def admin_usercomplaintreply_post(request):
    reply=request.POST['textarea']
    cid=request.POST['id']
    print(cid)
    robj=Complaint.objects.filter(id=cid).update(reply=reply,status='replied')
    return HttpResponse('''<script>alert('success');window.location='/myapp/admin_viewusercomplaint/'</script>''')


def admin_viewfeedback(request):
    a=Feedback.objects.all()
    return render(request,'admin/view feedback.html',{'data':a})
def admin_viewfeedback_post(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    a=Feedback.objects.filter(date__range=[fromdate,todate])
    return render(request,'admin/view feedback.html',{'data':a})



def admin_viewpayment(request):
    res=Payment.objects.all()
    return render(request,'admin/view payment.html',{'data':res})

def admin_viewpayment_post(request):
    fromdate = request.POST['from']
    todate = request.POST['to']
    res=Payment.objects.filter(date__range=[fromdate,todate])
    return render(request, 'admin/view payment.html',{'data':res})


def admin_viewposturevideo(request,tid):
    res=Category.objects.all()
    return render(request,'admin/view posture video.html',{'data':res,'tid':tid})

def admin_viewposturevideo_post(request):
    res=Category.objects.all()
    tid=request.POST['tid']
    categoryname=request.POST['select']
    ob=Posture.objects.filter(CATEGORY__id__contains=categoryname,TRAINER=tid)
    return render(request,'admin/view posture video.html',{'data1':ob,'data':res,'tid':tid})


def admin_changepwd(request):
    return render(request,'admin/changepwd.html')
def admin_changepwd_post(request):
    oldpassword=request.POST['textfield']
    newpassword=request.POST['textfield2']
    confirmpassword=request.POST['textfield3']
    var=Login.objects.filter(id=request.session['lid'],password=oldpassword)
    if var.exists():
        if newpassword==confirmpassword:
            var1=Login.objects.filter(id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert('successfully updated');window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert('password change not success');window.location='/myapp/admin_homepage/'</script>''')
    else:
        return HttpResponse('''<script>alert('password change not success');window.location='/myapp/admin_homepage/'</script>''')


def admin_logout(request):
    return render(request,'newlogin.html')



def admin_homepage(request):
    return render(request,'admin/home_index.html')





def trainer_viewprofile(request):
    ob=Trainer.objects.get(LOGIN=request.session['lid'])
    return render(request,'trainer/view profile.html',{'data':ob})



def trainer_addposture(request):
    a=Category.objects.all()
    return render(request,'trainer/add posture.html',{'data':a})


def trainer_addposture_post(request):
    category=request.POST['select']
    print(category)
    title=request.POST['textfield']
    image=request.FILES['fileField']
    video=request.FILES['fileField2']

    date = "p2" + datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
    fs = FileSystemStorage()
    fs.save(date, image)
    path = fs.url(date)

    date1 = "video" + datetime.now().strftime('%Y%m%d-%H%M%S') + '.mp4'
    fs1 = FileSystemStorage()
    fs1.save(date1, video)
    path1 = fs.url(date1)


    var=Posture()
    cc=Category.objects.get(id=category)
    var.CATEGORY=cc
    var.title=title
    var.image=path
    var.video=path1
    var.TRAINER=Trainer.objects.get(LOGIN__id=request.session['lid'])
    var.save()

    return HttpResponse('''<script>alert('Added successfully');window.location='/myapp/trainer_homepage/'</script>''')
def trainer_viewposture(request):
    cat=Category.objects.all()
    res=Posture.objects.filter(TRAINER__LOGIN__id=request.session['lid'])
    return render(request,'trainer/view posture.html',{"cat":cat,"data":res})

def trainer_viewposture_post(request):
    categoryname=request.POST['select']
    print(categoryname)
    cat = Category.objects.all()
    res = Posture.objects.filter(TRAINER__LOGIN__id=request.session['lid'],CATEGORY__id=categoryname)
    return render(request, 'trainer/view posture.html', {"cat": cat, "data": res})


def trainer_playvideo(request):
    return render(request,'trainer/play video.html')

def trainer_editposture(request,id):
    ob=Posture.objects.get(id=id)
    a=Category.objects.all()
    return render(request,'trainer/edit posture.html',{'data':ob,'data2':a})
def trainer_editposture_post(request):
    category=request.POST['select']
    title=request.POST['textfield']
    id=request.POST['id']
    if 'fileField' in request.FILES:
        image = request.FILES['fileField']
        date = "p2" + datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs = FileSystemStorage()
        fs.save(date, image)
        path = fs.url(date)
        var = Posture.objects.get(id=id)
        cc = Category.objects.get(id=category)
        var.CATEGORY = cc
        var.title = title
        var.image = path
        var.TRAINER = Trainer.objects.get(LOGIN__id=request.session['lid'])
        var.save()

        return HttpResponse(
            '''<script>alert('Added successfully');window.location='/myapp/trainer_viewposture/'</script>''')
    if 'fileField2' in request.FILES:
        video = request.FILES['fileField2']

        date1 = "video" + datetime.now().strftime('%Y%m%d-%H%M%S') + '.mp4'
        fs1 = FileSystemStorage()
        fs1.save(date1, video)
        path1 = fs1.url(date1)

        var = Posture.objects.get(id=id)
        cc = Category.objects.get(id=category)
        var.CATEGORY = cc
        var.title = title
        var.video = path1
        var.TRAINER = Trainer.objects.get(LOGIN__id=request.session['lid'])
        var.save()

        return HttpResponse('''<script>alert('Added successfully');window.location='/myapp/trainer_viewposture/'</script>''')
    else:
        var = Posture.objects.get(id=id)
        cc = Category.objects.get(id=category)
        var.CATEGORY = cc
        var.title = title
        var.TRAINER = Trainer.objects.get(LOGIN__id=request.session['lid'])
        var.save()

        return HttpResponse(
            '''<script>alert('Added successfully');window.location='/myapp/trainer_viewposture/'</script>''')


def trainer_deletetposture(request,id):
    data=Posture.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert('deleted successfully');window.location='/myapp/trainer_viewposture/'</script>''')




def trainer_viewuser(request):
    data=User.objects.all()
    return render(request,'trainer/view user.html',{'dt':data})
def trainer_viewuser_post(request):
    search=request.POST['textfield']
    data=User.objects.filter(name__icontains=search)
    return render(request, 'trainer/view user.html', {'dt': data})


def trainer_viewusermoredetails(request,id):
    data=User.objects.get(id=id)
    return render(request,'trainer/view users more details.html',{'dt':data})

def trainer_adddietplan(request):
    return render(request,'trainer/add diet plan.html')
def trainer_adddietplan_post(request):
    title=request.POST['textfield']
    file=request.FILES['fileField']
    date = "p2" + datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
    fs = FileSystemStorage()
    fs.save(date, file)
    path = fs.url(date)
    var=Diet()
    var.title=title
    var.file=path
    var.TRAINER=Trainer.objects.get(LOGIN__id=request.session['lid'])
    var.save()
    return HttpResponse('''<script>alert('Added successfully');window.location='/myapp/trainer_homepage/'</script>''')


def trainer_viewdietplan(request):
    data = Diet.objects.filter(TRAINER__LOGIN__id=request.session['lid'])
    return render(request,'trainer/view diet plan.html',{'dt':data})

def trainer_viewdietplan_post(request):
    search=request.POST['s']
    data=Diet.objects.filter(TRAINER__LOGIN__id=request.session['lid'],title__icontains=search)
    return render(request,'trainer/view diet plan.html',{'dt':data})

def trainer_editdietplan(request,id):
    a=Diet.objects.get(id=id)
    return render(request,'trainer/edit diet plan.html',{'data':a})

def trainer_editdietplan_post(request):
    id=request.POST['id']
    title = request.POST['textfield']
    if 'fileField' in request.FILES:
        file = request.FILES['fileField']
        date = "p2" + datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs = FileSystemStorage()
        fs.save(date, file)
        path = fs.url(date)
        res=Diet.objects.filter(id=id).update(title=title,file=path)
    res = Diet.objects.filter(id=id).update(title=title)
    return HttpResponse('''<script>alert('Update successfully');window.location='/myapp/trainer_viewdietplan/'</script>''')


def trainer_deletetdiet(request,id):
    data=Diet.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert('deleted successfully');window.location='/myapp/trainer_viewdietplan/'</script>''')


def trainer_querychat(request):
    return render(request,'trainer/query chat(trainer and user).html')

def trainer_changepwd(request):
    return render(request,'trainer/changepwd.html')
def trainer_changepwd_post(request):
    oldpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    var=Login.objects.get(id=request.session['lid'],password=oldpassword)
    if newpassword == confirmpassword:
        var1 = Login.objects.filter(id=request.session['lid']).update(password=confirmpassword)
        return HttpResponse('''<script>alert('successfully updated');window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert('password change not success');window.location='/myapp/trainer_homepage/'</script>''')

def trainer_logout(request):
    return render(request,'newlogin.html')

def trainer_homepage(request):
    return render(request,'trainer/trainerhome_index.html')



def user_signup(request):
    import datetime
    dt=datetime.date.today()
    dt=str(dt.year-18)+"-"+str(dt.month)+"-"+str(dt.day)
    return render(request,'user/signup_index.html',{'dt':dt})
def user_signup_post(request):
    name = request.POST['textfield']
    gender = request.POST['RadioGroup1']
    dob = request.POST['textfield3']
    place = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    height = request.POST['textfield7']
    weight = request.POST['textfield8']
    password = request.POST['textfield9']
    confirmpassword = request.POST['textfield10']


    res=Login.objects.filter(username=email)
    if res.exists():
        return HttpResponse('''<script>alert('Email Already Exist');window.location='/myapp/user_signup/'</script>''')
    else:

        if password==confirmpassword:

            lobj=Login()
            lobj.username=email
            lobj.password=password
            lobj.type='user'
            lobj.save()

            photo = request.FILES['fileField']
            date = "user" + datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
            fs = FileSystemStorage()
            fs.save(date, photo)
            path = fs.url(date)




            uobj=User()
            uobj.name=name
            uobj.phone=phone
            uobj.gender=gender
            uobj.email=email
            uobj.dob=dob
            uobj.place=place
            uobj.height=height
            uobj.weight=weight
            uobj.photo= path
            uobj.LOGIN=lobj
            uobj.save()

            return HttpResponse('''<script>alert('success');window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert('password mismatch');window.location='/myapp/user_signup/'</script>''')


def user_viewprofile(request):
    ob=User.objects.get(LOGIN=request.session['lid'])
    return render(request,'user/view profile.html',{'data':ob})

def user_viewposture(request):
    res = Category.objects.all()
    ob = Posture.objects.all()
    paid = "no"
    import datetime
    l=[]
    for i in ob:
        from django.db.models import Avg
        a = Rating.objects.filter(POSTURE_id=i.id).aggregate(Avg('rating'))
        rating = a['rating__avg']
        if a['rating__avg']==None:
            rating=0
        l.append(
            {'id': i.id, 'CATEGORY': i.CATEGORY.categoryname, 'TRAINER': i.TRAINER.name, 'title': i.title, 'image': i.image,
             'video': i.video,'rating':float(rating)})
    if Payment.objects.filter(USER__LOGIN_id=request.session['lid'],validity_date__month=datetime.date.today().month).exists():
        paid="yes"

    return render(request,'user/view posture.html',{'data':res,'data1': l, "paid":paid})
def user_viewposture_post(request):
    res = Category.objects.all()
    category = request.POST['select']
    ob = Posture.objects.filter(CATEGORY__id__contains=category)
    import datetime

    l = []
    for i in ob:
        from django.db.models import Avg
        a = Rating.objects.filter(POSTURE_id=i.id).aggregate(Avg('rating'))
        rating = a['rating__avg']
        if a['rating__avg'] == None:
            rating = 0
        l.append(
            {'id': i.id, 'CATEGORY': i.CATEGORY.categoryname, 'TRAINER': i.TRAINER.name, 'title': i.title,
             'image': i.image,
             'video': i.video, 'rating': float(rating)})
    paid = "no"
    if Payment.objects.filter(USER__LOGIN_id=request.session['lid'], validity_date__month=datetime.date.today().month).exists():
        paid = "yes"

    return render(request, 'user/view posture.html', {'data1': l, 'data': res, "paid":paid})


def rating(request,id):
    b = Rating.objects.filter(POSTURE_id=id)
    return render(request,'user/rating.html',{'id':id,'data': b})
def rating_post(request):
    Review=request.POST['textarea']
    id=request.POST['id']
    rating=request.POST['rating']

    from datetime import datetime
    var = Rating()
    var.review = Review
    var.rating = rating
    var.date = datetime.now().strftime('%Y-%m-%d')
    var.USER = User.objects.get(LOGIN_id=request.session['lid'])
    var.POSTURE_id = id
    var.save()
    return HttpResponse('''<script>alert('success');window.location='/myapp/user_homepage/'</script>''')


def user_playvideo(request):
    return render(request,'user/play video.html')

def user_sentcomplaint(request):
    return render(request,'user/sent complaint.html')
def user_sendcomplaint_post(request):
    complaint = request.POST['textarea']
    var=Complaint()
    var.status="pending"
    var.USER_id=User.objects.get(LOGIN=request.session['lid']).id
    var.complaint=complaint
    var.reply='pending'
    import datetime
    date=datetime.datetime.now().date()
    var.date=date
    var.save()
    return HttpResponse('''<script>alert('success');window.location='/myapp/user_homepage/'</script>''')

def user_viewcomplaintreply(request):
    b=Complaint.objects.filter(USER_id=User.objects.get(LOGIN=request.session['lid']).id)
    return render(request,'user/view complaint reply.html',{'data':b})

def user_viewcomplaintreply_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    a=Complaint.objects.filter(USER__LOGIN__id=request.session['lid'],date__range=[fromdate,todate])
    return render(request, 'user/view complaint reply.html', {'data': a})



def user_sentfeedback(request):
    return render(request,'user/sent feedback.html')

def user_sentfeedback_post(request):
    feedback = request.POST['textarea']
    var=Feedback()
    var.feedback=feedback
    var.date=datetime.now().date()
    var.USER=User.objects.get(LOGIN__id=request.session['lid'])
    var.save()
    return HttpResponse('''<script>alert('success');window.location='/myapp/user_homepage/'</script>''')

def user_viewdietplan(request):
    dobj=Diet.objects.all()
    return render(request,'user/view diet plan.html',{"data":dobj})
def user_viewdietplan_post(request):
    search=request.POST['textfield']
    dobj=Diet.objects.filter(title__icontains=search)
    return render(request, 'user/view diet plan.html', {"data": dobj})


def user_sendquery(request):
    return render(request,'user/send query chat.html')

def user_payment(request):
    return render(request,'user/payment.html')

def user_payment_post(request):
    ac_holdername = request.POST['textfield']
    cvv = request.POST['textfield2']
    cardno = request.POST['cardno']
    validity = request.POST['textfield3']
    amount = 500
    if Bank.objects.filter(acholdername=ac_holdername,cvv=cvv,card_number=cardno,expiry_date=validity,balance__gte=amount).exists():
        from datetime import datetime
        var=Payment()
        var.acholdername=ac_holdername
        var.cvv=cvv
        var.validity_date=datetime.now().strftime('%Y-%m-%d')
        var.status="paid"
        var.amount=amount
        var.USER=User.objects.get(LOGIN_id=request.session['lid'])

        var.date=datetime.now().strftime('%Y-%m-%d')
        var.save()
        a=Bank.objects.get(acholdername=ac_holdername, cvv=cvv, card_number=cardno, expiry_date=validity).balance-amount
        Bank.objects.filter(acholdername=ac_holdername, cvv=cvv, card_number=cardno, expiry_date=validity).update(balance=a)
        return HttpResponse('''<script>alert('success');window.location='/myapp/user_homepage/'</script>''')
    return HttpResponse('''<script>alert('Invalid credentials/Insufficient Balance');window.location='/myapp/user_homepage/'</script>''')


def user_changepwd(request):
    return render(request,'user/changepwd.html')
def user_changepwd_post(request):
    oldpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    var=Login.objects.get(id=request.session['lid'],password=oldpassword)
    if newpassword==confirmpassword:
        var1=Login.objects.filter(id=request.session['lid']).update(password=confirmpassword)
        return HttpResponse('''<script>alert('successfully updated');window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert('password change not success');window.location='/myapp/user_homepage/'</script>''')

def user_logout(request):
    return render(request,'newlogin.html')

def user_homepage(request):
    return render(request,'user/userhome_index.html')


def forget_password(request):
    return render(request,'forgot password.html')

def forget_password_post(request):
    em = request.POST['textfield']
    import random
    ch=string.ascii_letters + string.digits + string.punctuation
    password=''.join(random.choice(ch)for i in range(8))
    log = Login.objects.filter(username=em)
    if log.exists():
        logg = Login.objects.get(username=em)
        message = 'temporary password is ' + str(password)
        send_mail(
            'temp password',
            message,
            settings.EMAIL_HOST_USER,
            [em, ],
            fail_silently=False
        )
        logg.password = password
        logg.save()
        return HttpResponse('<script>alert("success");window.location="/myapp/login/"</script>')
    else:
        return HttpResponse('<script>alert("invalid email");window.location="/myapp/login/"</script>')

def user_view_trainer(request):
    b = Trainer.objects.all()
    return render(request, 'user/view trainers.html', {'data': b})

def user_view_trainer_post(request):
    search=request.POST['textfield']
    data=Trainer.objects.filter(name__icontains=search)
    return render(request,'user/view trainers.html',{'data':data})




def chat(request, toid):
    qry = User.objects.get(LOGIN_id=toid)

    request.session['tolid']= toid
    return render(request, "trainer/Chat.html", {'photo': qry.photo, 'name': qry.name, 'toid': toid})


def chat_view(request, tid):
    fromid = request.session["lid"]
    toid = request.session['tolid']
    qry = User.objects.get(LOGIN__id=tid)
    from django.db.models import Q
    res = Chat.objects.filter(Q(FROM_ID_id=fromid, TO_ID_id=toid) | Q(FROM_ID_id=toid, TO_ID_id=fromid))
    l = []
    for i in res:
        l.append({"id": i.id, "message": i.message,"date": i.date, "from": i.FROM_ID_id})

    return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.name, 'toid': tid})


def chat_send(request, msg, tid):


    lid = request.session["lid"]
    toid =request.session['tolid']
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TO_ID_id = toid
    chatobt.FROM_ID_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})



#######################





def chat1(request, toid):
    qry = Trainer.objects.get(LOGIN_id=toid)
    request.session['tolid']= toid
    return render(request, "user/Chat.html", {'photo': qry.photo, 'name': qry.name, 'toid': toid})


def chat_view2(request, tid):
    fromid = request.session["lid"]
    toid = request.session['tolid']
    qry =  Trainer.objects.get(LOGIN__id=tid)
    from django.db.models import Q
    res = Chat.objects.filter(Q(FROM_ID_id=fromid, TO_ID_id=toid) | Q(FROM_ID_id=toid, TO_ID_id=fromid))
    l = []
    for i in res:
        l.append({"id": i.id, "message": i.message,"date": i.date, "from": i.FROM_ID_id})
    return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.name, 'toid': tid})


def chat_send2(request, msg, tid):
    lid = request.session["lid"]
    toid =request.session['tolid']
    message = msg
    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TO_ID_id = toid
    chatobt.FROM_ID_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})
