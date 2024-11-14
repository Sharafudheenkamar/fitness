from django.db import models

STATUS_CHOICES={
    ("ACTIVE","Active"),
    ("DEACTIVE","Deactive"),
}
# Create your models here.
class Category(models.Model):
    categoryname = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
class Subscriptions(models.Model):
    subscriptionname = models.CharField(max_length=100,null=True,blank=True)
    monthlyprice = models.CharField(max_length=100,null=True,blank=True)
    workoutvideoes = models.BooleanField(default=True)
    dietplans = models.BooleanField(default=True)
    workoutchallenges = models.BooleanField(default=True)
    chatsupport=models.BooleanField(default=True)
    physiotherapy=models.BooleanField(default=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

