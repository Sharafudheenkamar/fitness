from django.views import View
from .forms import *
from users.models import Userprofile
# from .models import Registration
from trainer.models import *
from .models import *
from django.shortcuts import render,redirect
from django.http import HttpResponse
from client.models import *
from django.contrib.auth.hashers import make_password

# Create your views here.
class Adminaddtrainers(View):
    def get(self,request):
        import datetime
        dt = datetime.date.today()
        dt = str(dt.year - 18) + "-" + str(dt.month) + "-" + str(dt.day)
        return render(request, 'admin/add trainers.html', {'dt': dt})

    def post(self,request):
        form = Registrationprofileform(request.POST,request.FILES)
        if form.is_valid():
            # utype=request.POST['user_type']
            # print(utype)
            Registration=form.save(commit=False)

            # print(request.POST['user_type'])
            print(request.POST['dob'])
            us = Userprofile.objects.create_user(
                user_type="TRAINER",
                username=request.POST['email'],
                password=request.POST['phoneno'],
                gender=request.POST['gender'],
                email=request.POST['email'],
                first_name=request.POST['first_name'],
                dob=request.POST['dob'],
                phoneno=request.POST['phoneno'],
                photo=request.FILES['photo'],
                place=request.POST['place'],
                status="ACTIVE",  # assuming you have a 'status' field in your form
            )
            # us=Userprofile.objects.create_user(user_type=request.POST['user_type'],username=request.POST['username'],password=request.POST['password'],email=request.POST['email'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],photo=request.FILES['photo'])
            Registration.user=us
            Registration.save()
            return HttpResponse('''<script>alert('updated successfully');window.location='/adminfitness/admin_addtrainers_post/'</script>''')



class Adminviewtrainers(View):
     def get(self,request):
         data = Trainer.objects.filter(is_active=True).all()
         print(data)
         return render(request, 'admin/view trainers.html', {'dt': data})
class Adminupdatetrainers(View):
    def get(self, request,data):
        print("sfdsdsdfsfd")
        registration=Trainer.objects.filter(id=data, is_active=True).first()
        print(registration)
        return render(request,'admin/update trainers.html',{'data':registration})

    def post(self,request,data):
        print("dsfdsfds")
        listinstance = Trainer.objects.filter(id=data, is_active=True).first()
        form = Registrationprofileform(request.POST, request.FILES, instance=listinstance)
        if form.is_valid():
            registration = form.save(commit=False)
            newimg = request.FILES.get("photo")
            user = registration.user

            if newimg:

                user.photo = newimg
            else:
                # print(listinstance.user.photo)
                # pass
                user.photo = listinstance.user.photo

            user.email = request.POST["email"]
            user.first_name = request.POST["first_name"]
            user.phoneno = request.POST["phoneno"]
            user.place=request.POST['place']
            user.gender=request.POST['gender']
            user.save()
            registration.save()

            return HttpResponse(
                '''<script>alert('updated successfully');window.location='/adminfitness/admin_viewtrainers/'</script>''')

class Admindeletetrainers(View):
    def get(self,request,data):
        Registration_instance = Trainer.objects.filter(id=data, is_active=True).first()

        if Registration_instance:
            Registration_instance.is_active = False
            Registration_instance.save()
            user = Registration_instance.user
            if user:
                user.is_active = False
                user.save()


            return HttpResponse(
        '''<script>alert('deleted successfully');window.location='/adminfitness/admin_viewtrainers/'</script>''')

class Admin_homepage(View):
    def get(self,request):
        return render(request,'admin/home_index.html')
class Adminaddsubscriptions(View):
    def get(self,request):

       return render(request, 'admin/adminaddsubscriptions.html',)

    def post(self,request):
        form = Subscriptionsform(request.POST)
        if form.is_valid():

            Registration=form.save(commit=False)

            # print(request.POST['user_type'])

            Registration.save()
            return HttpResponse('''<script>alert('updated successfully');window.location='/adminfitness/admin_viewsubscription/'</script>''')



class Adminviewsubscriptions(View):
     def get(self,request):
         data = Subscriptions.objects.filter(is_active=True).all()
         print(data)
         return render(request, 'admin/adminviewsubscription.html', {'dt': data})


class Adminviewsubscriptionspost(View):
    def post(self, request):
        search=request.POST['textfield']
        data = Subscriptions.objects.filter(is_active=True,subscriptionname__icontains=search).all()
        print(data)
        return render(request, 'admin/adminviewsubscription.html', {'dt': data})
class Adminupdatesubscriptions(View):
    def get(self, request,data):
        print("sfdsdsdfsfd")
        registration=Subscriptions.objects.filter(id=data, is_active=True).first()
        print(registration)
        return render(request,'admin/admineditsubscription.html',{'data':registration})

    def post(self,request,data):
        print("dsfdsfds")
        listinstance = Subscriptions.objects.filter(id=data, is_active=True).first()
        form = Subscriptionsform(request.POST, instance=listinstance)
        if form.is_valid():
            registration = form.save(commit=False)

            registration.save()

            return HttpResponse(
                '''<script>alert('updated successfully');window.location='/adminfitness/admin_viewsubscription/'</script>''')

class Admindeletesubscriptions(View):
    def get(self,request,data):
        Registration_instance = Subscriptions.objects.filter(id=data, is_active=True).first()

        if Registration_instance:
            Registration_instance.is_active = False
            Registration_instance.save()

            return HttpResponse(
        '''<script>alert('deleted successfully');window.location='/adminfitness/admin_viewsubscription/'</script>''')


class Admin_Category(View):
    def get(self,request):
        return render(request,'admin/add category.html')
    def post(self,request):
        form = Categoryform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                '''<script>alert('Added successfully');window.location='/adminfitness/admin_viewcategory/'</script>''')
        return render(request,'admin/add category.html',{'form':form})
class Adminviewcategory(View):
     def get(self,request):
         data = Category.objects.all()
         return render(request, 'admin/view category.html', {'dt': data})


class Adminviewcategorypost(View):
    def post(self, request):
        search=request.POST['textfield']
        data = Category.objects.filter(title=search,is_active=True).all()
        return render(request, 'admin/view category.html', {'dt': data})


class Admineditcategory(View):
    def get(self,request,cid):
        a=Category.objects.get(id=cid)
        return render(request, 'admin/edit category.html', {'data': a})
    def post(self,request,cid):
     data = Category.objects.filter(is_active=True,id=cid).first()
     form=Categoryform(request.POST,instance=data)
     if form.is_valid():
         form.save()
         return HttpResponse('''<script>alert('uated successfully');window.location='/adminfitness/admin_viewcategory/'</script>''')

class Admindeletecategory(View):
    def get(self,request,id):
        data=Category.objects.get(id=id)
        data.delete()
        return HttpResponse(
            '''<script>alert('deleted successfully');window.location='/adminfitness/admin_viewcategory/'</script>''')


def admin_addcategory_post(request):
    categoryname=request.POST['textfield']

    var = Category()
    var.categoryname=categoryname
    var.save()
    return HttpResponse('''<script>alert('Added successfully');window.location='/myapp/admin_homepage/'</script>''')

def admin_viewtrainers_post(request):
    search=request.POST['textfield']
    data=Trainer.objects.filter(first_name__icontains=search)
    return render(request,'admin/view trainers.html',{'dt':data})

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

def admin_viewuser(request):
    data=Clientprofile.objects.filter(is_active=True).all()
    return render(request,'admin/view user.html',{'dt':data})
def admin_viewuser_post(request):
    search=request.POST['textfield']
    data=Clientprofile.objects.filter(user__first_name__icontains=search,is_active=True).all()

    return render(request,'admin/view user.html',{'dt':data})


def admin_viewtrainer_post(request):
    search = request.POST['textfield']
    data = Trainer.objects.filter(user__first_name__icontains=search,is_active=True).all()

    return render(request, 'admin/view trainers.html', {'dt': data})
def admin_viewusermoredetails(request,id):
    data=Clientprofile.objects.get(id=id)
    return render(request,'admin/view users more detailss.html',{'dt':data})

def admin_viewusercomplaint(request):
    b=Complaint.objects.all()
    return render(request,'admin/view user complaint.html',{'data':b})
def admin_viewusercomplaint_post(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    a=Complaint.objects.filter(created_at__range=[fromdate,todate])
    return render(request,'admin/view user complaint.html',{'data':a})



def admin_usercomplaintreply(request,id):
    res=Complaint.objects.get(id=id)
    return render(request,'admin/sent complaint reply.html',{'data':res})

def admin_usercomplaintreply_post(request):
    reply=request.POST['textarea']
    cid=request.POST['id']
    print(cid)
    Complaint.objects.filter(id=cid).update(reply=reply,status='replied')
    return HttpResponse('''<script>alert('success');window.location='/adminfitness/admin_viewusercomplaint/'</script>''')


def admin_viewfeedback(request):
    a=Feedback.objects.all()
    return render(request,'admin/view feedback.html',{'data':a})
def admin_viewfeedback_post(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    a=Feedback.objects.filter(created_at__range=[fromdate,todate])
    return render(request,'admin/view feedback.html',{'data':a})



def admin_viewpayment(request):
    res=Payment.objects.all()
    return render(request,'admin/view payment.html',{'data':res})

def admin_viewpayment_post(request):
    fromdate = request.POST['from']
    todate = request.POST['to']
    res=Payment.objects.filter(created_at__range=[fromdate,todate])
    return render(request, 'admin/view payment.html',{'data':res})


def admin_viewposturevideo(request,tid):
    res=Category.objects.all()
    return render(request,'admin/view posture video.html',{'data':res,'tid':tid})
def admin_trainerviewposturevideo(request,tid):
    res=Posture.objects.filter(trainer=tid)
    print(res)
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
    oldpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    # Userprofile.objects.get(id=request.session['user_id'][0],password=oldpassword)
    if newpassword == confirmpassword:
        hash_pass = make_password(confirmpassword)
        Userprofile.objects.filter(id=request.session['user_id'][0]).update(password=hash_pass)
        return HttpResponse('''<script>alert('successfully updated');window.location='/'</script>''')
    else:
        return HttpResponse(
            '''<script>alert('password change not success');window.location='/adminfitness/user_homepage/'</script>''')


def admin_logout(request):
    return render(request,'newlogin.html')
def admin_viewchallenges(request):
    challenge_instances=Challenges.objects.filter(is_active=True).all
    return render(request,'admin/adminviewchallenges.html',{"ch":challenge_instances})
def admin_viewtasks(request):
    task_instances=Task.objects.filter(is_active=True).all()
    return  render(request,'admin/adminviewtasks.html',{"ta":task_instances})