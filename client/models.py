from django.db import models
from users.models import Userprofile
from trainer.models import Posture
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from django.db.models.signals import post_save, post_delete
# Create your models here.
STATUS_CHOICES={
    ("ACTIVE","Active"),
    ("DEACTIVE","Deactive"),
}
class Clientprofile(models.Model):
    user=models.OneToOneField(Userprofile,on_delete=models.CASCADE)
    height = models.CharField(max_length=100,null=True,blank=True)
    weight = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)




class Chat(models.Model):
    message = models.CharField(max_length=100)
    from_id = models.ForeignKey(Userprofile,on_delete=models.CASCADE,default=1,related_name="fuser")
    to_id = models.ForeignKey(Userprofile,on_delete=models.CASCADE,default=1,related_name="tuser")
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class Payment(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    validity_date = models.DateField(default='2023-11-18',null=True,blank=True)
    amount = models.FloatField(null=True,blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def save(self, *args, **kwargs):
        if self.pk is None:
            # Only reduce balance when the payment is being created, not updated
            bank = Bank.objects.get(user=self.user)
            bank.balance -= self.amount
            bank.save()
        super().save(*args, **kwargs)


class Bank(models.Model):
    user = models.OneToOneField(Userprofile,on_delete=models.CASCADE,null=True,blank=True)
    card_number = models.CharField(max_length=100,null=True,blank=True)
    cvv = models.CharField(max_length=100,null=True,blank=True)
    expiry_date = models.CharField(max_length=100,null=True,blank=True)
    balance=models.FloatField(null=True,blank=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class Rating(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE, null=True, blank=True)
    posture = models.ForeignKey(Posture, on_delete=models.CASCADE, null=True, blank=True)
    review=models.CharField(max_length=700,null=True,blank=True)
    rating=models.FloatField(null=True,blank=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, blank=True)
    is_active = models.BooleanField(default=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
class Videorating(models.Model):
    user=models.ForeignKey(Userprofile,on_delete=models.CASCADE,null=True,blank=True)
    video_id=video_id=models.ForeignKey(Posture,on_delete=models.CASCADE,null=True,blank=True)
    userrating=models.CharField(max_length=20,null=True,blank=True,default=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


@receiver(post_save, sender=Videorating)
def update_posture_rating(sender, instance, **kwargs):
    video_id = instance.video_id
    avg_rating = Videorating.objects.filter(video_id=video_id).aggregate(Avg('userrating'))['userrating__avg']

    if avg_rating is not None:
        # Scale the average rating to be out of 5
        scaled_rating = (avg_rating / 100) * 5

        # Update posture's overallrating field
        posture = Posture.objects.get(pk=video_id.pk)
        posture.overallrating = scaled_rating
        posture.save()
class Videolike(models.Model):
    user=models.ForeignKey(Userprofile,on_delete=models.CASCADE,null=True,blank=True)
    video_id=models.ForeignKey(Posture,on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
@receiver(post_save, sender=Videolike)
def update_posture_likes_on_like(sender, instance, created, **kwargs):
    if created and instance.video_id:
        instance.video_id.likes += 1
        instance.video_id.save()

@receiver(post_delete, sender=Videolike)
def update_posture_likes_on_unlike(sender, instance, **kwargs):
    if instance.video_id:
        instance.video_id.likes -= 1
        instance.video_id.save()

class Videocomment(models.Model):
    user=models.ForeignKey(Userprofile,on_delete=models.CASCADE,null=True,blank=True)
    video_id=models.ForeignKey(Posture,on_delete=models.CASCADE,null=True,blank=True)
    comment=models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
class Feedback(models.Model):
    user=models.ForeignKey(Userprofile,on_delete=models.CASCADE,null=True,blank=True)
    discription= models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
class Complaint(models.Model):
    user=models.ForeignKey(Userprofile,on_delete=models.CASCADE,null=True,blank=True)
    complaints= models.CharField(max_length=100,null=True,blank=True)
    reply= models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=20, null=True, default='pending', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
