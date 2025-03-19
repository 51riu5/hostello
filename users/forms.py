from django.db import models
from django.forms import ModelForm
from .models import profile

class completeprofile(ModelForm):
    class Meta:
        model = profile
        fields = '__all__'
        exclude = ['username','iscompleted']


