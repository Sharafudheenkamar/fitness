from .models import Clientprofile
from users.models import Userprofile
from rest_framework import serializers
from trainer.models import *
from .models import *
class ClientprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientprofile
        # fields = '_all_'

        fields = ['height','weight']

class UserprofileSerializer(serializers.ModelSerializer):

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
        return None
    class Meta:
        model = Userprofile

        fields = ['first_name','phoneno','photo','email','dob','gender','place','password']


class Trainerlistserializer(serializers.ModelSerializer):
    trainer_id = serializers.CharField(source='user.pk', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    photo = serializers.SerializerMethodField()
    phoneno = serializers.CharField(source='user.phoneno', read_only=True)

    def get_photo(self, obj):
        if obj.user.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.user.photo.url)
        return None

    class Meta:
        model = Trainer
        fields = ['trainer_id','certificate','trainerrating','first_name','photo','phoneno']
class Videolistserializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='trainer.first_name', read_only=True)
    video_file = serializers.SerializerMethodField()
    image=serializers.SerializerMethodField()
    categoryname=serializers.CharField(source='category.categoryname', read_only=True)



    class Meta:
        model=Posture
        fields=['id','categoryname','first_name','title','video_file','image','likes']

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


class Videobyidserializer(serializers.ModelSerializer):
    class Meta:
        model=Posture
        fields=['video_file','image']
class VideolikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Videolike
        fields=['user','video_id','likestatus']
class VideolikeSerializerbyvideoid(serializers.ModelSerializer):
    class Meta:
        model=Videolike
        fields=['user','likestatus']
class VideocommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Videocomment
        fields=['user','video_id','comment']
class VideocommentSerializerbyvideoid(serializers.ModelSerializer):
    class Meta:
        model=Videocomment
        fields=['user','comment']
class Dietlistserializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    trainer_name = serializers.CharField(source='trainer.first_name', read_only=True)
    trainer_id = serializers.CharField(source='trainer.pk', read_only=True)

    def get_file(self, obj):
        if obj.file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.file.url)
        return None
    class Meta:
        model=Diet
        fields=['trainer_id','trainer_name','title','file']

class Challengeserializer(serializers.ModelSerializer):
    video_file= serializers.SerializerMethodField()
    trainer_name = serializers.CharField(source='user.first_name', read_only=True)
    trainer_id=serializers.CharField(source='user.pk',read_only=True)
    def get_video_file(self, obj):
        if obj.video_file:  # Assuming 'video_file' is the field storing the video file
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.video_file.url)
        return None
    class Meta:
        model = Challenges
        fields = ['trainer_id','trainer_name','title', 'video_file', 'thumbnail']
class Taskserializer(serializers.ModelSerializer):
    trainer_name = serializers.CharField(source='user.first_name', read_only=True)
    trainer_id=serializers.CharField(source='user.pk',read_only=True)
    class Meta:
        model=Task
        fields=['trainer_id','trainer_name','title','discription']
class Feedbackserializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields=['user','discription']
class Complaintserializer(serializers.ModelSerializer):
    class Meta:
        model=Complaint
        fields=['user','complaints','reply']

class Videocommentse(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.first_name', read_only=True)
    class Meta:
        model = Videocomment
        fields = ['user_name','comment','created_at']
class VideoLikeSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Videolike
        fields = ['user','video_id']
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['message','from_id','to_id','created_at']
class ChatPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['message','from_id','to_id']