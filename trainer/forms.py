from django import forms
from .models import Challenges,Task

class Challengesform(forms.ModelForm):
    class Meta:
        model=Challenges
        fields=['title','video_file']
class Taskform(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','discription']