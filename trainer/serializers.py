
from rest_framework import serializers
from .models import *
from users.models import Userprofile
from client.models import Clientprofile,Chat
from adminfitness.models import Category
from rest_framework.views import APIView


class Dietserializer(serializers.ModelSerializer):
    file=serializers.SerializerMethodField()
    def get_file(self, obj):
        if obj.file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.file.url)
        return None
    class Meta:
        model = Diet
        fields = ['id','trainer','title','file']
class Dietserializer1(serializers.ModelSerializer):

    class Meta:
        model = Diet
        fields = ['title','file']
# class Viewusersserializer(serializers.ModelSerializer):
#     phoneno=models.CharField(max_length=20,null=True,blank=True)
#     photo=models.ImageField(upload_to=generate_unique_filename,null=True,blank=True)
#     email=models.CharField(max_length=100,null=True,blank=True)
#     dob=models.CharField(max_length=100,null=True,blank=True)
#     gender=models.CharField(max_length=20,null=True,blank=True)
#     place=models.CharField(max_length=100,null=True,blank=True)
#     class Meta:
#         model = Userprofile
#         fields = ['first_name','phoneno','email','gender','place','dob','photo']
# class Viewuseradditionaldetails(serializers.ModelSerializer):
#     class Meta:
#         model=Clientprofile
#         fields=['height','weight']
# class ClientprofileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Clientprofile
#         fields=['height','weight']

class TrainerprofileSerializer(serializers.ModelSerializer):
    certificate_url = serializers.SerializerMethodField()
    def get_certificate_url(self, obj):
        if obj.certificate:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.certificate.url)
        return None

    class Meta:
        model = Trainer
        fields = ['certificate_url']




class UserprofileSerializer(serializers.ModelSerializer):
    # trainer_id = serializers.CharField(source='user.pk', read_only=True)
    # username = serializers.CharField(source='user.first_name', read_only=True)
    # photo = serializers.SerializerMethodField()
    # phoneno = serializers.CharField(source='user.phoneno', read_only=True)

    def get_photo(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
        return None
    class Meta:
        model = Userprofile

        fields = ['id','first_name', 'email','phoneno','photo','email','dob','gender','place','password']
class UserprofileSerializer1(serializers.ModelSerializer):
    client_id = serializers.CharField(source='user.pk', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    photo = serializers.SerializerMethodField()
    phoneno = serializers.CharField(source='user.phoneno', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    dob =  serializers.CharField(source='user.dob', read_only=True)
    gender = serializers.CharField(source='user.gender', read_only=True)
    place = serializers.CharField(source='user.place', read_only=True)
    subscriptionplan = serializers.CharField(source='user.subscriptionplan', read_only=True)
    def get_photo(self, obj):
        if obj.user.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.user.photo.url)
        return None
    class Meta:
        model = Clientprofile

        fields = ['client_id','first_name', 'email','phoneno','photo','dob','gender','place','height','weight','subscriptionplan']

class Postureviewserializer(serializers.ModelSerializer):
    video_file=serializers.SerializerMethodField()
    image=serializers.SerializerMethodField()
    # category_name = serializers.CharField(source='category.title', read_only=True)
    category_name = serializers.CharField(source='category.categoryname', read_only=True)
    class Meta:
        model = Posture
        fields = ['id','category','category_name','trainer','title','video_file','image','is_active']
    def get_video_file(self, obj):
        if obj.video_file:
            # Construct the absolute URL using the host address and the video file path
            return self.context['request'].build_absolute_uri(obj.video_file.url)
        return None

    def get_image(self, obj):
        if obj.image:
            # Construct the absolute URL using the host address and the image file path
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None
class Postureviewserializer1(serializers.ModelSerializer):
     class Meta:
        model = Posture
        fields = ['id','category','trainer','title','video_file','image']



class Postureputserializer(serializers.ModelSerializer):

    class Meta:
        model = Posture
        fields = [ 'category', 'trainer', 'title', 'video_file', 'image']
class Posturedeleteserializer(serializers.ModelSerializer):

    class Meta:
        model = Posture
        fields = ['is_active']


class Taskviewserializer(serializers.ModelSerializer):
    trainername=serializers.CharField(source='user.first_name')
    class Meta:
        model = Task
        fields = ['id','user','trainername','title','discription']
class Taskviewserializer1(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','discription']
class Challengeviewserializer(serializers.ModelSerializer):
    video_file=serializers.SerializerMethodField()
    def get_video_file(self, obj):
        if obj.video_file:
            # Construct the absolute URL using the host address and the video file path
            return self.context['request'].build_absolute_uri(obj.video_file.url)
        return None
    class Meta:
        model = Challenges
        fields = ['id','user','title','video_file']
class Challengeviewserializer1(serializers.ModelSerializer):
    class Meta:
        model = Challenges
        fields = ['user','title','video_file']
class Challengeviewserializer3(serializers.ModelSerializer):
    class Meta:
        model = Challenges
        fields = ['title','video_file']
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['message','from_id','to_id','created_at']
class ChatPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['message','from_id','to_id']
class Categorylistserializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields=['id','categoryname']