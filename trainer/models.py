from django.db import models
from users.models import Userprofile
from adminfitness.models import Category
from django.db.models.signals import post_save, post_delete
STATUS_CHOICES={
    ("ACTIVE","Active"),
    ("DEACTIVE","Deactive"),
}
from django.core.files.storage import FileSystemStorage
from django.utils import timezone


def generate_unique_filename(instance, filename):
    """
    Function to generate a unique filename based on the current timestamp.
    """
    # Get the file extension
    extension = filename.split('.')[-1]

    # Generate a unique filename
    unique_filename = f"p1_{timezone.now().strftime('%Y%m%d-%H%M%S')}.{extension}"

    return unique_filename
# Create your models here.
class Trainer(models.Model):
    user=models.OneToOneField(Userprofile,on_delete=models.CASCADE,null=True,blank=True)
    tid=models.CharField(max_length=50,null=True,blank=True)
    certificate = models.FileField(upload_to=generate_unique_filename,null=True,blank=True)
    trainerrating=models.CharField(max_length=50,null=True,blank=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
class Posture(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    trainer = models.ForeignKey(Userprofile,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    video_file = models.FileField(upload_to='trainerposture/',null=True,blank=True)
    # thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    overallrating=models.FloatField(default=0,null=True,blank=True)
    likes=models.IntegerField(default=0,null=True,blank=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
class Diet(models.Model):
    trainer=models.ForeignKey(Userprofile,on_delete=models.CASCADE,null=True,blank=True)
    title= models.CharField(max_length=100,null=True,blank=True)
    file= models.FileField(upload_to='diet_files/',max_length=500,null=True,blank=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class Challenges(models.Model):
    user=models.ForeignKey(Userprofile,on_delete=models.CASCADE,null=True,blank=True)
    title= models.CharField(max_length=100)
    video_file = models.FileField(upload_to='challengefiles/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
class Task(models.Model):
    user=models.ForeignKey(Userprofile,on_delete=models.CASCADE,null=True,blank=True)
    title= models.CharField(max_length=100)
    discription= models.CharField(max_length=100)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
