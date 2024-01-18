from django.db import models

class signupdb(models.Model):
    susername=models.CharField(max_length=100,null=True,blank=True)
    semail=models.CharField(max_length=100,null=True,blank=True)
    snumber=models.IntegerField(null=True,blank=True)
    spassword=models.CharField(max_length=100,null=True,blank=True)

class contactdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    subject=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=100,null=True,blank=True)

class likedb(models.Model):
    likmname=models.CharField(max_length=100,null=True,blank=True)
    likcname = models.CharField(max_length=100, null=True, blank=True)
    likmusic = models.FileField(upload_to="Music", null=True, blank=True)
    likdescription = models.CharField(max_length=100, null=True, blank=True)
    likimage = models.ImageField(upload_to="Images", null=True, blank=True)
    likusername=models.CharField(max_length=100,null=True,blank=True)





# Create your models here.
