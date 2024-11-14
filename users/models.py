import random
import string

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your models here.
USER_TYPE_CHOICES={
    ("ADMIN","admin"),
    ("TRAINER","trainer"),
    ("CLIENT","client"),

}
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
SUBS_CHOICES={("STANDARD","standard"),
              ("PREMIUM","premium"),
              ("ORDINARY","ordinary")}
class Userprofile(AbstractUser):
    #firstname
    phoneno=models.CharField(max_length=20,null=True,blank=True)
    photo=models.ImageField(upload_to=generate_unique_filename,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    dob=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=20,null=True,blank=True)
    place=models.CharField(max_length=100,null=True,blank=True)
    subscriptionplan=models.CharField(max_length=100,null=True,blank=True,default='ORDINARY',choices=SUBS_CHOICES)
    otp=models.CharField(max_length=50,null=True,blank=True,default='')
    status = models.CharField(max_length=20,null=True,choices=STATUS_CHOICES,blank=True)
    is_active = models.BooleanField(default=True)
    user_type=models.CharField(max_length=30,null=True,choices=USER_TYPE_CHOICES,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return f"{self.pk}-{self.first_name}"
import random
import string
class Token(models.Model):
    key = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(
        Userprofile,
        related_name="auth_tokens",
        on_delete=models.CASCADE,
        verbose_name="user",
        unique=True,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    session_dict = models.TextField(null=False, default="{}")

    dict_ready = False
    data_dict = None

    def _init_(self, *args, **kwargs):
        self.dict_ready = False
        self.data_dict = None
        super(Token, self)._init_(*args,**kwargs)
    def generate_key(self):
        return "".join(
            random.choice(
                string.ascii_lowercase + string.digits + string.ascii_uppercase
            )
            for i in range(40)
        )
    def save(self, *args, **kwargs):
        if not self.key:
            new_key = self.generate_key()
            while type(self).objects.filter(key=new_key).exists():
                new_key = self.generate_key()
            self.key = new_key
        return super(Token, self).save(*args,**kwargs)

    def read_session(self):
        if self.session_dict == "null":
            self.data_dict = {}
        else:
            self.data_dict = json.loads(self.session_dict)
        self.dict_ready = True
    def update_session(self, tdict, save=True, clear=False):
        if not clear and not self.dict_ready:
            self.read_session()
        if clear:
            self.data_dict = tdict
            self.dict_ready = True
        else:
             for key, value in tdict.items():
                 self.data_dict[key] = value
             if save:
                 self.write_back()

    def set(self, key, value, save=True):
        if not self.dict_ready:
            self.read_session()
        self.data_dict[key] = value
        if save:
            self.write_back()

    def write_back(self):
        self.session_dict = json.dumps(self.data_dict)
        self.save()

    def get(self, key, default=None):
        if not self.dict_ready:
            self.read_session()
        return self.data_dict.get(key, default)

    def _str_(self):
        return str(self.user) if self.user else str(self.id)


