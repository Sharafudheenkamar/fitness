from django.shortcuts import render
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from .models import *
from adminfitness.models import *
from django.http import HttpResponse
from users.models import Userprofile
from rest_framework.views import APIView
from rest_framework import status
from.serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from.forms import *
from client.models import Clientprofile
from django.db.models import Q
from client.models import Chat

from django.shortcuts import get_object_or_404
# Create your views here.
import datetime
def trainer_viewprofile(request):
    print(request.session['user_id'][0])
    # ob=Trainer.objects.get(user=request.session['user_id'])
    ob = Trainer.objects.filter(user__id=request.session['user_id'][0]).first()
    print(ob)
    return render(request,'trainer/view profile.html',{'data':ob})



def trainer_addposture(request):
    a=Category.objects.all()
    return render(request,'trainer/add posture.html',{'data':a})


from PIL import Image
from moviepy.video.io.VideoFileClip import VideoFileClip
def generate_thumbnail(video_path, thumbnail_path):
    clip = VideoFileClip(video_path)
    thumbnail = clip.get_frame(0)
    thumbnail_image = Image.fromarray(thumbnail)
    thumbnail_image.save(thumbnail_path)
    return thumbnail_path  # Return the path of the generated thumbnail

def trainer_addposture_post(request):
    import os
    from django.conf import settings

    if request.method == 'POST':
        category = request.POST.get('select')
        title = request.POST.get('textfield')
        image = request.FILES.get('fileField')
        video = request.FILES.get('fileField2')

        # Save the uploaded files
        # fs = FileSystemStorage()
        #
        # # Save image
        # date_image = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        # image_path = fs.save(date_image, image)
        #
        # # Save video
        # date_video = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.mp4'
        # video_path = fs.save(date_video, video)

        # Get category and trainer
        category_obj = Category.objects.get(id=category)
        trainer_obj = Userprofile.objects.get(id=request.session['user_id'][0])

        # Create new posture instance
        posture = Posture.objects.create(
            category=category_obj,
            trainer=trainer_obj,
            title=title,
            image=image,
            video_file=video
        )

        # Generate thumbnail for the video
        # thumbnail_name = os.path.splitext(video)[0] + '.jpg'
        # thumbnail_path = os.path.join(settings.MEDIA_ROOT, 'thumbnails', thumbnail_name)
        # thumbnail_path = generate_thumbnail(os.path.join(settings.MEDIA_ROOT, video_path), thumbnail_path)
        #
        # # Update the posture instance with the thumbnail path
        # posture.thumbnail = thumbnail_path
        # posture.save()

        return HttpResponse('''<script>alert('Added successfully');window.location='/trainer/trainer_homepage/'</script>''')
def trainer_viewposture(request):
    cat=Category.objects.all()
    res=Posture.objects.filter(trainer=request.session['user_id'][0])
    return render(request,'trainer/view posture.html',{"cat":cat,"data":res})

def trainer_viewposture_post(request):
    categoryname=request.POST['select']
    print(categoryname)
    cat = Category.objects.all()
    res = Posture.objects.filter(trainer=request.session['user_id'][0],category=categoryname)
    return render(request, 'trainer/view posture.html', {"cat": cat, "data": res})


def trainer_playvideo(request):
    return render(request,'trainer/play video.html')

def trainer_editposture(request,id):
    ob=Posture.objects.get(id=id)
    a=Category.objects.all()
    return render(request,'trainer/edit posture.html',{'data':ob,'data2':a})
def trainer_editposture_post(request):
    category_id = request.POST.get('select')
    title = request.POST.get('textfield')
    posture_id = request.POST.get('id')

    # Get the Posture object or return a 404 error if not found
    posture = get_object_or_404(Posture, id=posture_id)

    # Get the Category object or return a 404 error if not found
    category = get_object_or_404(Category, id=category_id)

    # Get the image file from request.FILES or None if not present
    image = request.FILES.get('fileField')

    # Get the video file from request.FILES or None if not present
    video = request.FILES.get('fileField2')

    # Update the posture object with the new data
    posture.category = category
    posture.title = title

    # Only update image if it's present in the request
    if image:
        posture.image = image

    # Only update video if it's present in the request
    if video:
        posture.video_file = video

    # Set the trainer based on the logged-in user
    posture.trainer = Userprofile.objects.get(id=request.session['user_id'][0])

    # Save the updated posture object
    posture.save()

    return HttpResponse(
        '<script>alert("Updated successfully");window.location="/trainer/trainer_viewposture/";</script>')

def trainer_deletetposture(request,id):
    data=Posture.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert('deleted successfully');window.location='/trainer/trainer_viewposture/'</script>''')




def trainer_viewuser(request):
    data=Userprofile.objects.filter(is_active=True,user_type='client').all()
    return render(request,'trainer/view user.html',{'dt':data})
def trainer_viewuser_post(request):
    search=request.POST['textfield']
    data=Userprofile.objects.filter(name__icontains=search)
    return render(request, 'trainer/view user.html', {'dt': data})


def trainer_viewusermoredetails(request,id):
    data=Userprofile.objects.get(id=id)
    return render(request,'trainer/view users more details.html',{'dt':data})

def trainer_adddietplan(request):
    return render(request,'trainer/add diet plan.html')
def trainer_adddietplan_post(request):
    title=request.POST['textfield']
    file=request.FILES['fileField']
    date = "p2" + datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
    fs = FileSystemStorage()
    fs.save(date, file)
    path = fs.url(date)
    var=Diet()
    var.title=title
    var.file=path
    var.trainer=Userprofile.objects.get(id=request.session['user_id'][id])
    var.save()
    return HttpResponse('''<script>alert('Added successfully');window.location='/myapp/trainer_homepage/'</script>''')


def trainer_viewdietplan(request):
    data = Diet.objects.filter(trainer=request.session['user_id'][0])
    return render(request,'trainer/view diet plan.html',{'dt':data})

def trainer_viewdietplan_post(request):
    search=request.POST['s']
    data=Diet.objects.filter(trainer=request.session['user_id'][0],title__icontains=search)
    return render(request,'trainer/view diet plan.html',{'dt':data})

def trainer_editdietplan(request,id):
    a=Diet.objects.get(id=id)
    return render(request,'trainer/edit diet plan.html',{'data':a})

def trainer_editdietplan_post(request):
    id=request.POST['id']
    title = request.POST['textfield']
    if 'fileField' in request.FILES:
        file = request.FILES['fileField']
        date = "p2" + datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs = FileSystemStorage()
        fs.save(date, file)
        path = fs.url(date)
        res=Diet.objects.filter(id=id).update(title=title,file=path)
    res = Diet.objects.filter(id=id).update(title=title)
    return HttpResponse('''<script>alert('Update successfully');window.location='/trainer/trainer_viewdietplan/'</script>''')


def trainer_deletetdiet(request,id):
    data=Diet.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert('deleted successfully');window.location='/trainer/trainer_viewdietplan/'</script>''')


def trainer_querychat(request):
    return render(request,'trainer/query chat(trainer and user).html')

def trainer_changepwd(request):
    return render(request,'trainer/changepwd.html')
def trainer_changepwd_post(request):
    oldpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    # Userprofile.objects.get(id=request.session['user_id'][0],password=oldpassword)
    if newpassword==confirmpassword:
        hash_pass=make_password(confirmpassword)
        Userprofile.objects.filter(id=request.session['user_id'][0]).update(password=hash_pass)
        return HttpResponse('''<script>alert('successfully updated');window.location='/'</script>''')
    else:
        return HttpResponse('''<script>alert('password change not success');window.location='/adminfitness/user_homepage/'</script>''')
def trainer_logout(request):
    return render(request,'newlogin.html')

def trainer_homepage(request):
    return render(request,'trainer/trainerhome_index.html')
def trainer_viewusermoredetails(request,id):
    data=User.objects.get(id=id)
    return render(request,'trainer/view users more details.html',{'dt':data})

def trainer_adddietplan(request):
    return render(request,'trainer/add diet plan.html')
def trainer_adddietplan_post(request):
    title=request.POST['textfield']
    file=request.FILES['fileField']
    var=Diet()
    var.title=title
    var.file=file
    var.trainer=Userprofile.objects.get(id=request.session['user_id'][0])
    var.save()
    return HttpResponse('''<script>alert('Added successfully');window.location='/trainer/trainer_viewdietplan/'</script>''')


def trainer_viewdietplan(request):
    data = Diet.objects.filter(trainer=request.session['user_id'][0])
    return render(request,'trainer/view diet plan.html',{'dt':data})

def trainer_viewdietplan_post(request):
    search=request.POST['s']
    print(search)
    data=Diet.objects.filter(trainer=request.session['user_id'][0],title=search).all()
    return render(request,'trainer/view diet plan.html',{'dt':data})

def trainer_editdietplan(request,id):
    a=Diet.objects.get(id=id)
    return render(request,'trainer/edit diet plan.html',{'data':a})

import datetime
def trainer_editdietplan_post(request):
    id=request.POST['id']
    title = request.POST['textfield']
    if 'fileField' in request.FILES:
        file = request.FILES['fileField']
        date = "p2" + datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs = FileSystemStorage()
        fs.save(date, file)
        path = fs.url(date)
        res=Diet.objects.filter(id=id).update(title=title,file=path)
    res = Diet.objects.filter(id=id).update(title=title)
    return HttpResponse('''<script>alert('Update successfully');window.location='/trainer/trainer_viewdietplan/'</script>''')


def trainer_deletetdiet(request,id):
    data=Diet.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert('deleted successfully');window.location='/trainer/trainer_viewdietplan/'</script>''')


def trainer_querychat(request):
    return render(request,'trainer/query chat(trainer and user).html')


class Viewdietapiview(APIView):
    def get(self,request,data=None):
        if data is not None:
            diet_instances=Diet.objects.filter(trainer=data,is_active=True).all()
            serializer=Dietserializer(diet_instances,many=True,context={'request':request})
            return Response(serializer.data)

        else:
            diet_instances=Diet.objects.filter(is_active=True).all()
            serializer=Dietserializer1(diet_instances,many=True)
            return Response(serializer.data)
    def post(self,request,data=None):
        diet=Dietserializer(data=request.data)
        print(request.data)
        if diet.is_valid():
            diet.save()
            return Response(diet.data, status=status.HTTP_201_CREATED)
    def patch(self,request,data):
        diet_instance=Diet.objects.filter(id=data,is_active=True).first()
        diet=Dietserializer1(data=request.data,instance=diet_instance)
        if diet.is_valid():
            diet.save()
            return Response(diet.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, data):
        diet_instance = Diet.objects.filter(id=data,is_active=True).first()
        if diet_instance:
            diet_instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Diet not found"}, status=status.HTTP_404_NOT_FOUND)
class Viewuserprofileapiview(APIView):
    def get(self, request):
        client_instances = Clientprofile.objects.filter(is_active=True).all()
        serializer = UserprofileSerializer1(client_instances, many=True,context={'request': request})
        return Response(serializer.data)
# class Viewtrainerprofileapiview(APIView):
#     def get(self, request):
#         trainer_instances = Trainer.objects.filter(is_active=True).all()
#         serializer = TrainerprofileSerializer(trainer_instances, many=True,context={'request': request})
#         return Response(serializer.data)
class Traineraddchallenges(View):
    def get(self,request):

        return render(request, 'trainer/addchallenges.html',)

    def post(self,request):
        id=request.session['user_id'][0]
        print(id)
        form = Challengesform(request.POST,request.FILES)
        if form.is_valid():

            Registration=form.save(commit=False)
            Registration.user__id=id

            # print(request.POST['user_type'])

            Registration.save()
            return HttpResponse('''<script>alert('added successfully');window.location='/trainer/trainer_viewchallenge/'</script>''')



class Trainerviewchallenges(View):

     def get(self,request):
         id=request.session['user_id'][0]
         data = Challenges.objects.filter(user=id,is_active=True).all()
         print(data)
         return render(request, 'trainer/viewchallenges.html', {'dt': data})


class Trainerviewchallengespost(View):

    def post(self, request):
        search=request.POST['s']
        print(search)
        id = request.session['user_id'][0]
        data = Challenges.objects.filter(user=id, is_active=True,title=search).all()
        print(data)
        return render(request, 'trainer/viewchallenges.html', {'dt': data})
class Trainerupdatechallenges(View):
    def get(self, request,data):
        print("sfdsdsdfsfd")
        registration=Challenges.objects.filter(id=data, is_active=True).first()
        print(registration)
        return render(request,'trainer/updatechallenges.html',{'data':registration})

    def post(self,request,data):
        print("dsfdsfds")
        listinstance = Challenges.objects.filter(id=data, is_active=True).first()
        form = Challengesform(request.POST,request.FILES, instance=listinstance)
        if form.is_valid():
            registration = form.save(commit=False)

            registration.save()

            return HttpResponse(
                '''<script>alert('updated successfully');window.location='/trainer/trainer_viewchallenge/'</script>''')

class Trainerdeletechallenges(View):
    def get(self,request,data):
        Registration_instance = Challenges.objects.filter(id=data, is_active=True).first()

        if Registration_instance:
            Registration_instance.is_active = False
            Registration_instance.save()

            return HttpResponse(
        '''<script>alert('deleted successfully');window.location='/trainer/trainer_viewchallenge/'</script>''')

class Traineraddtask(View):
    def get(self,request):

        return render(request, 'trainer/addtask.html',)

    def post(self,request):
        id=request.session['user_id'][0]
        print(id)
        form = Taskform(request.POST)
        if form.is_valid():

            Registration=form.save(commit=False)
            Registration.user_id=id

            # print(request.POST['user_type'])

            Registration.save()
            return HttpResponse('''<script>alert('added successfully');window.location='/trainer/trainer_viewtask/'</script>''')



class Trainerviewtask(View):

     def get(self,request):
         id=request.session['user_id'][0]
         data = Task.objects.filter(user=id,is_active=True).all()
         print(data)
         return render(request, 'trainer/viewtask.html', {'dt': data})


class Trainerviewtaskpost(View):

    def post(self, request):
        title=request.POST['s']
        id = request.session['user_id'][0]
        data = Task.objects.filter(user=id, is_active=True,title=title).all()
        print(data)
        return render(request, 'trainer/viewtask.html', {'dt': data})
class Trainerupdatetask(View):
    def get(self, request,data):
        print("sfdsdsdfsfd")
        registration=Task.objects.filter(id=data, is_active=True).first()
        print(registration)
        return render(request,'trainer/updatetask.html',{'data':registration})

    def post(self,request,data):
        print("dsfdsfds")
        listinstance = Task.objects.filter(id=data, is_active=True).first()
        form = Taskform(request.POST,request.FILES, instance=listinstance)
        if form.is_valid():
            registration = form.save(commit=False)

            registration.save()

            return HttpResponse(
                '''<script>alert('updated successfully');window.location='/trainer/trainer_viewtask/'</script>''')

class Trainerdeletetask(View):
    def get(self,request,data):
        Registration_instance = Task.objects.filter(id=data, is_active=True).first()

        if Registration_instance:
            Registration_instance.is_active = False
            Registration_instance.save()

            return HttpResponse(
        '''<script>alert('deleted successfully');window.location='/trainer/trainer_viewtask/'</script>''')

def trainer_viewuser(request):
    data=Clientprofile.objects.filter(is_active=True).all()
    return render(request,'trainer/view user.html',{'dt':data})
def trainer_viewuser_post(request):
    search=request.POST['textfield']
    data=Clientprofile.objects.filter(user__first_name__icontains=search)
    return render(request,'trainer/view user.html',{'dt':data})
def trainer_viewusermoredetails(request,id):
    data=Clientprofile.objects.get(id=id)
    return render(request,'trainer/view users more details.html',{'dt':data})
class UserprofileCreateAPIView(APIView):
    permission_classes = [AllowAny]


    def get(self, request,pk=None):
        if pk is not None:
            try:
                client_profile = Trainer.objects.get(user=pk)
                serializer = TrainerprofileSerializer(client_profile,context={'request': request})

                client_profile1 = Userprofile.objects.get(id=pk)
                ser = UserprofileSerializer(client_profile1,context={'request': request} )

                # Combine serializer data without keys
                response = {**serializer.data, **ser.data}

                return Response(response)
            except Clientprofile.DoesNotExist:
                return Response({"error":"Trainer profile does not exist"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error":"Trainer profile does not exist"},status=status.HTTP_404_NOT_FOUND)

class Viewposture(APIView):
    def get(self,request,id=None):
        if id is not None:
            posture_instances=Posture.objects.filter(is_active=True,trainer=id).all()
            print(posture_instances)
            serializers=Postureviewserializer(posture_instances,many=True,context={'request':request})
            return Response(serializers.data)
        else:
            posture_instances = Posture.objects.filter(is_active=True).all()

            serializers = Postureviewserializer(posture_instances,many=True,context={'request':request})
            data=serializers.data
            return Response(data)

    def post(self, request):
        serializer = Postureviewserializer1(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        posture_instance = Posture.objects.filter(is_active=True, id=id).first()
        if posture_instance:
            serializer = Postureviewserializer(posture_instance, data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Posture not found"}, status=status.HTTP_404_NOT_FOUND)
class Viewputposture(APIView):

    def patch(self, request, id):
        print(id)
        posture_instance = Posture.objects.filter(is_active=True, id=id).first()
        if posture_instance:
            print(request.data)
            serializer = Postureputserializer(posture_instance, data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Posture not found"}, status=status.HTTP_404_NOT_FOUND)
class Viewdeleteposture(APIView):

    def put(self, request, id):
        print(id)
        posture_instance = Posture.objects.filter(is_active=True, id=id).first()
        if posture_instance:
            print(request.data)
            serializer = Posturedeleteserializer(posture_instance, data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Posture not found"}, status=status.HTTP_404_NOT_FOUND)

class Viewtask(APIView):
    def get(self,request,id=None):
        if id is not None:
            task_instances=Task.objects.filter(is_active=True,user=id).all()
            serializers=Taskviewserializer(task_instances,many=True)
            return Response(serializers.data)
        else:
            task_instances = Posture.objects.filter(is_active=True, user=id).all()
            serializers = Taskviewserializer(task_instances,many=True)
            return Response(serializers.data)

    def post(self, request):
        serializer = Taskviewserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        task_instance = Task.objects.filter(is_active=True, id=id).first()
        if task_instance:
            serializer = Taskviewserializer1(task_instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        task_instance = Task.objects.filter(is_active=True, id=id).first()
        if task_instance:
            serializer = Taskviewserializer(task_instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        task_instance = Task.objects.filter(is_active=True, id=id).first()
        if task_instance:
            task_instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
class Viewchallenges(APIView):
    def get(self,request,id=None):
        if id is not None:
            challenge_instances=Challenges.objects.filter(is_active=True,user=id).all()
            serializers=Challengeviewserializer(challenge_instances,many=True,context={'request':request})
            return Response(serializers.data)
        else:
            challenge_instances = Challenges.objects.filter(is_active=True, user=id).all()
            serializers = Taskviewserializer(challenge_instances,many=True)
            return Response(serializers.data)

    def post(self, request):
        serializer = Challengeviewserializer1(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        challenge_instance = Challenges.objects.filter(is_active=True, id=id).first()
        print(challenge_instance)
        if challenge_instance:
            serializer = Challengeviewserializer3(challenge_instance, data=request.data, partial=True)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Challenge not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        challenge_instance = Challenges.objects.filter(is_active=True, id=id).first()
        if challenge_instance:
            challenge_instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Challenge not found"}, status=status.HTTP_404_NOT_FOUND)
class ChatAPIView(APIView):
    def get(self, request,fromid,toid):

        chats = Chat.objects.filter(Q(from_id=fromid, to_id=toid) | Q(from_id=toid, to_id=fromid)).order_by('created_at')
        chats = chats.order_by('created_at')  # Order by created_at
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)
class ChatAPIViewPOST(APIView):
    def post(self, request):
        serializer = ChatPostSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        chat_instance = self.get_object(pk)
        serializer = ChatSerializer(chat_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
class Viewdata(APIView):
    def post(self,request):
        print(request.data['key'])
        return HttpResponse("OK")

class viewcategorylist(APIView):
    def get(self,request):
        se=Category.objects.all()
        serializers=Categorylistserializer(se,many=True)
        return Response(serializers.data)