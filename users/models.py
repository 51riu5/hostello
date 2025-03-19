from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
    fullname=models.CharField(max_length=50)
    rollno = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    contactno = models.CharField(max_length=11)
    yearofstudy = models.CharField(max_length=50)
    dob = models.DateField()
    bloodgroup=models.CharField(max_length=20)
    nationality=models.CharField(max_length=50)
    mothertongue=models.CharField(max_length=50)
    aadhaar=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    iscompleted=models.BooleanField(default=False)

    def __str__(self):
        return self.username