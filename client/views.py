from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import*
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from users.models import Userprofile
from trainer.models import *
from .models import *
from django.views import View
from django.http import HttpResponse
from .serializers import *
from django.db.models import Q
from adminfitness.models import Category
# Create your views here.

def client_viewprofile(request):
    print(request.session['user_id'][0])
    # ob=Trainer.objects.get(user=request.session['user_id'])
    ob = Clientprofile.objects.filter(user_id=request.session['user_id'][0]).first()
    print(ob)
    return render(request,'user/view profile.html',{'data':ob})


class Clientviewtrainers(View):
    def get(self, request):
        data = Trainer.objects.filter(is_active=True).all()
        print(data)
        return render(request, 'user/view trainers.html', {'dt': data})


class UserprofileCreateAPIView(APIView):
    permission_classes = [AllowAny]


    def get(self, request,pk=None):
        if pk is not None:
            try:
                client_profile = Clientprofile.objects.get(user=pk)
                serializer = ClientprofileSerializer(client_profile)

                client_profile1 = Userprofile.objects.get(id=pk)
                ser = UserprofileSerializer(client_profile1, context={'request': request})

                # Combine serializer data without keys
                response = {**serializer.data, **ser.data}

                return Response(response)
            except Clientprofile.DoesNotExist:
                return Response({"error":"Clientprofile does not exist"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error":"Clientprofile does not exist"},status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        client_serializer = ClientprofileSerializer(data=request.data)
        # print(user_data)
        print(request.data)
        # print(client_serializer,'client_serializer')
        user_serializer=UserprofileSerializer(data=request.data)
        # print(user_serializer,'user_serializer')
        client_valid = client_serializer.is_valid()
        user_valid = user_serializer.is_valid()

        if client_valid and user_valid:
            username=request.data['email']
            print(username)
            password=request.data['password']

            # Send the password through email
            send_mail(
                'Your New Account Password',
                f'Your password:{username} {password}',
                'from@example.com',
                [request.data['email']],
                fail_silently=False,
            )
            hashed_password=make_password(password)


            user = user_serializer.save(user_type="CLIENT",username=username,password=hashed_password)
            client_serializer.save(user=user)

            return Response(client_serializer.data, status=status.HTTP_201_CREATED)

        return Response({'client_errors': client_serializer.errors if not client_valid else None,
                         'user_errors': user_serializer.errors if not user_valid else None},
                        status=status.HTTP_400_BAD_REQUEST)

class Viewtrainers(APIView):
    def get(self, request):
        trainer_instances = Trainer.objects.filter(is_active=True).all()

        serializer = Trainerlistserializer(trainer_instances, many=True,context={'request': request})
        return Response(serializer.data)
class Viewvideoes(APIView):
    def get(self,request):
        video_instances= Posture.objects.filter(is_active=True).all()
        serializer=Videolistserializer(video_instances,many=True,context={'request': request})
        return Response(serializer.data)

class Viewdiet(APIView):
    def get(self,request):
        video_instances= Diet.objects.filter(is_active=True).all()
        serializer=Dietlistserializer(video_instances,many=True,context={'request': request})
        return Response(serializer.data)
class Viewdietbycategory(APIView):
    def get(self,request,data):
        video_instances= Diet.objects.filter(is_active=True,title=data).all()
        serializer=Dietlistserializer(video_instances,many=True,context={'request': request})
        return Response(serializer.data)

class Viewvideoesbycategory(APIView):
    def get(self,request,data):
        video_instances= Posture.objects.filter(is_active=True,category=data).all()
        serializer=Videolistserializer(video_instances,many=True,context={'request': request})
        return Response(serializer.data)
class Viewvideobyid(APIView):
    def get(self,request,data,id):
        video_instances=Posture.objects.filter(is_active=True,id=data).first()
        serializer=Videobyidserializer(video_instances)
        print(video_instances)
        video_likes = Videolike.objects.filter(video_id=video_instances,user=id).first()
        print(video_likes)
        like_serializer = VideolikeSerializer(video_likes)
        print(like_serializer)
        # Retrieve comments for the video
        video_comments = Videocomment.objects.filter(video_id=video_instances).all()
        print(video_comments)
        comment_serializer = VideocommentSerializer(video_comments, many=True)
        response_data = {
            'video': serializer.data,
            'likes': like_serializer.data,
            'comments': comment_serializer.data
        }
        return Response(response_data)

class Likevideoes(APIView):
    def post(self, request, data, id, status, format=None):
        if status == 'True':
            video_id = data
            user_id = id
            status=status
            print(status)

            # Combine URL values with request data
            request_data = request.data.copy()
            request_data['video_id'] = video_id
            request_data['user'] = user_id
            request_data['likestatus']=status
            serializer = VideolikeSerializer(data=request_data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Invalid request method for this URL."},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def delete(self, request, data,id, status, format=None):
        if status == 'False':
            try:
                # Retrieve the object
                obj = Videolike.objects.get(video_id=data,user=id)
            except Videolike.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            # Delete the object
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Invalid request method for this URL."},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
class Commentvideoes(APIView):
    def post(self,request):
        likeserializer=VideocommentSerializer(data=request.data)
        if likeserializer.is_valid():
            likeserializer.save()

            return Response(likeserializer.data,status=status.HTTP_201_CREATED)

    # def patch(self, request, id, data):
    #     try:
    #         # Retrieve the Videolike instance based on the provided id and user
    #         like_instance = Videocomment.objects.get(video_id=id, user=data, is_active=True)
    #     except Videolike.DoesNotExist:
    #         return Response({"message": "Videolike instance not found"}, status=status.HTTP_404_NOT_FOUND)
    #
    #     # Deserialize the request data into the Videolike instance
    #     likeserializer = VideocommentSerializerbyvideoid(instance=like_instance, data=request.data, partial=True)
    #     if likeserializer.is_valid():
    #         likeserializer.save()
    #         return Response(likeserializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(likeserializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Viewchallengesapiview(APIView):
    def get(self,request):
        challenge_instances=Challenges.objects.filter(is_active=True).all()
        # challenge_count = Challenges.objects.filter(is_active=True).count()
        serializer=Challengeserializer(challenge_instances,many=True, context={'request': request})
        return Response(serializer.data)
class Viewtaskapiview(APIView):
    def get(self,request):
        task_instances=Task.objects.filter(is_active=True).all()
        serializer=Taskserializer(task_instances,many=True)
        return Response(serializer.data)
class Viewfeedbackapiview(APIView):
    def get(self,request):
        feedback_instances=Feedback.objects.filter(is_active=True).all()
        serializer=Feedbackserializer(feedback_instances,many=True)
        return Response(serializer.data)
    def post(self,request):
        feedback=Feedbackserializer(data=request.data)
        print(request.data)
        if feedback.is_valid():
            feedback.save()
            return Response(feedback.data,status=status.HTTP_201_CREATED)
class Viewcomplaintapiview(APIView):
    def get(self,request,data):
        if data is not None:
            complaint_instances=Complaint.objects.filter(is_active=True,user=data)
            serializers=Complaintserializer(complaint_instances,many=True)
            return Response(serializers.data)
        else:
            complaint_instances=Complaint.objects.filter(is_active=True).all()
            serializer=Complaintserializer(complaint_instances,many=True)
        return Response(serializer.data)
    def post(self,request):
        complaint=Complaintserializer(data=request.data)
        if complaint.is_valid():
            complaint.save()
            return Response(complaint.data, status=status.HTTP_201_CREATED)

def client_viewposturevideo(request):
    res=Category.objects.all()
    return render(request,'user/view posture.html',{'data':res})
class Clientlikecommentvideobyapi(APIView):
    def get(self, request, data, id):
        try:
            videolikeinstance = Videolike.objects.get(video_id=data, user=id)
            print(videolikeinstance)
        except Videolike.DoesNotExist:
            videolikeinstance = None
            print(videolikeinstance)

        like = True if videolikeinstance else False
        print(like)

        videocommentinstance = Videocomment.objects.filter(video_id=data).all()
        print(videocommentinstance)
        serializer1 = Videocommentse(videocommentinstance,many=True)
        print(serializer1)

        response = {

            'like': like,
            'comments': serializer1.data
        }
        return Response(response)


class LikeVideoAPIView(APIView):
    def post(self, request, video_id,user_id, format=None):
        try:
            video = Posture.objects.get(id=video_id)
        except Posture.DoesNotExist:
            return Response({"detail": "Video not found"}, status=status.HTTP_404_NOT_FOUND)

        like_data = {'video_id': video_id, 'user': user_id}
        serializer = VideoLikeSerializer1(data=like_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnlikeVideoAPIView(APIView):
    def delete(self, request, video_id,user_id, format=None):
        try:
            like = Videolike.objects.get(video_id=video_id, user=user_id)
        except Videolike.DoesNotExist:
            return Response({"detail": "Like not found"}, status=status.HTTP_404_NOT_FOUND)

        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
def user_viewprofile(request):
    ob=Clientprofile.objects.get(user=request.session['user_id'][0])
    print("viekfkljsakjfaklj")
    print(ob)
    return render(request,'user/view profile.html',{'data':ob})

def user_viewposture(request):
    res = Category.objects.all()
    ob = Posture.objects.all()
    paid = "no"
    import datetime
    l=[]
    # for i in ob:
    #     from django.db.models import Avg
    #     a = Rating.objects.filter(POSTURE_id=i.id).aggregate(Avg('rating'))
    #     rating = a['rating__avg']
    #     if a['rating__avg']==None:
    #         rating=0_post
    #     l.append(
    #         {'id': i.id, 'CATEGORY': i.CATEGORY.categoryname, 'TRAINER': i.TRAINER.name, 'title': i.title, 'image': i.image,
    #          'video': i.video,'rating':float(rating)})
    if Payment.objects.filter(USER__LOGIN_id=request.session['lid'],validity_date__month=datetime.date.today().month).exists():
        paid="yes"

    return render(request,'user/view posture.html',{'data':res,'data1': l, "paid":paid})
def user_viewposture(request):
    data1=Category.objects.all()
    res = Posture.objects.all()
    return render(request,'user/view posture.html',{'data':res,'data1':data1})
def user_viewposture_post(request):
    res = Posture.objects.all()
    print(res)
    category = request.POST['select']
    ob = Posture.objects.filter(category__id__contains=category)
    print(res)
    return render(request, 'user/view posture.html', {'data1': l, 'data': res, "paid":paid})

def rating(request,id):
    b = Posture.objects.filter(id=id).first()
    print(b)
    rating_instances=Rating.objects.all()
    return render(request,'user/rating.html',{'data': b,'rating_instances':rating_instances})
def rating_post(request,id):

    Review=request.POST['textarea']
    # id=request.POST['id']
    rating=request.POST['rating']
    print(id)
    var = Rating()
    var.review = Review
    var.rating = rating
    user_profile = Userprofile.objects.get(pk=request.session['user_id'][0])
    var.user = user_profile
    var.posture = Posture.objects.get(id=id)
    var.save()
    return HttpResponse('''<script>alert('success');window.location='/client/user_homepage/'</script>''')


def user_playvideo(request):
    return render(request,'user/play video.html')

def user_sentcomplaint(request):
    return render(request,'user/sent complaint.html')
def user_sendcomplaint_post(request):
    complaint = request.POST['textarea']
    var=Complaint()
    var.status="pending"
    var.user=Userprofile.objects.get(id=request.session['user_id'][0])
    var.complaints=complaint
    var.reply='pending'
    var.save()
    return HttpResponse('''<script>alert('success');window.location='/client_homepage/'</script>''')

def user_viewcomplaintreply(request):


    b=Complaint.objects.filter(user=request.session['user_id'][0])
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
    var.discription=feedback

    var.user=Userprofile.objects.get(id=request.session['user_id'][0])
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
    amount = 250
    if Bank.objects.filter(user__first_name=ac_holdername,cvv=cvv,card_number=cardno,expiry_date=validity,balance__gte=amount).exists():
        from datetime import datetime
        var=Payment()


        var.validity_date=datetime.now().strftime('%Y-%m-%d')
        var.status="paid"
        var.amount=amount
        user_profile = Userprofile.objects.get(pk=request.session['user_id'][0])
        var.user = user_profile
        var.date=datetime.now().strftime('%Y-%m-%d')
        var.save()
        a=Bank.objects.get(user__first_name=ac_holdername, cvv=cvv, card_number=cardno, expiry_date=validity).balance-amount
        Bank.objects.filter(user__first_name=ac_holdername, cvv=cvv, card_number=cardno, expiry_date=validity).update(balance=a)
        return HttpResponse('''<script>alert('success');window.location='/client/user_homepage/'</script>''')
    return HttpResponse('''<script>alert('Invalid credentials/Insufficient Balance');window.location='/client/user_homepage/'</script>''')

def user_homepage(request):
    return render(request,'user/userhome_index.html')

def user_changepwd(request):
    return render(request,'user/changepwd.html')


def user_changepwd_post(request):
    oldpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    # Userprofile.objects.get(id=request.session['user_id'][0],password=oldpassword)
    if newpassword==confirmpassword:
        hash_pass=make_password(confirmpassword)
        Userprofile.objects.filter(id=request.session['user_id'][0]).update(password=hash_pass)
        return HttpResponse('''<script>alert('successfully updated');window.location='/'</script>''')
    else:
        return HttpResponse('''<script>alert('password change not success');window.location='/myapp/user_homepage/'</script>''')
def user_view_trainer(request):
    b = Trainer.objects.all()
    return render(request, 'user/view trainers.html', {'data': b})

def user_view_trainer_post(request):
    search=request.POST['textfield']
    data=Trainer.objects.filter(name__icontains=search)
    return render(request,'user/view trainers.html',{'data':data})




def chat(request, toid):
    qry = Userprofile.objects.get(id=toid)

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


    lid = request.session["user_id"]
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

def chat1(request, toid):
    qry = Userprofile.objects.get(id=toid)
    request.session['tolid']= toid
    return render(request, "user/chat.html", {'photo': qry.photo, 'name': qry.first_name, 'toid': toid})


def chat_view2(request, tid):
    # fromid = request.session["lid"]
    # toid = request.session['tolid']
    # qry =  Trainer.objects.get(LOGIN__id=tid)
    # from django.db.models import Q
    # res = Chat.objects.filter(Q(fromid=fromid, toid=toid) | Q(fromid=toid, toid=fromid))
    # l = []
    # for i in res:
    #     l.append({"id": i.id, "message": i.message,"date": i.created_at, "from": i.fromid})
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
class ChatView(APIView):
    def get(self, request,fromid,toid):

        chats = Chat.objects.filter(Q(from_id=fromid, to_id=toid) | Q(from_id=toid, to_id=fromid)).order_by('created_at')
        chats = chats.order_by('created_at')  # Order by created_at
        serializer = ChatSerializer(chats, many=True)
        return render(request, 'trainer/chattemplate2.html', {'chats': serializer.data,'to_id':toid})
class ChatView(APIView):
    def get(self, request,fromid,toid):

        chats = Chat.objects.filter(Q(from_id=fromid, to_id=toid) | Q(from_id=toid, to_id=fromid)).order_by('created_at')
        chats = chats.order_by('created_at')  # Order by created_at
        serializer = ChatSerializer(chats, many=True)
        return render(request, 'trainer/chattemplate2.html', {'chats': serializer.data,'to_id':toid})


class ChatViewPOST(APIView):
    def post(self, request):
        serializer = ChatPostSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.http import JsonResponse

def view_chat_history(request):
    if request.method == 'GET':
        fromid = request.GET.get('sender_id')
        print(fromid)
        toid = request.GET.get('recipient_id')
        print(toid)
        # Fetch chat history based on sender and recipient IDs
        chats = Chat.objects.filter(Q(from_id=fromid, to_id=toid) | Q(from_id=toid, to_id=fromid)).order_by('created_at')
        # You might want to order the chats by created_at or any other criteria
        serializer = ChatSerializer(chats, many=True)
        return render(request, 'trainer/chattemplate3.html', {'chats': serializer.data})