from django import forms
from .models import *
from trainer.models import Trainer
class Registrationprofileform(forms.ModelForm):
    class Meta :

        model = Trainer
        fields = ['tid','certificate','status']
class Categoryform(forms.ModelForm):
    class Meta :
        model = Category
        fields=['categoryname']
class Subscriptionsform(forms.ModelForm):
    class Meta:
        model = Subscriptions
        fields =['subscriptionname','monthlyprice','workoutvideoes','dietplans','workoutchallenges','chatsupport','physiotherapy']
