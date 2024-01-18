from django.db import models

class addMusicdb(models.Model):
    category=models.CharField(max_length=100,null=True,blank=True)
    mname=models.CharField(max_length=100,null=True,blank=True)
    cname=models.CharField(max_length=100,null=True,blank=True)
    music=models.FileField(upload_to="Music",null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to="Images",null=True,blank=True)

class addcatedb(models.Model):
    catname=models.CharField(max_length=100,null=True,blank=True)
    catimage=models.ImageField(upload_to="images",null=True,blank=True)

class replydb(models.Model):
    reply=models.CharField(max_length=500,null=True,blank=True)



class addeventdb(models.Model):
    evename=models.CharField(max_length=100,null=True,blank=True)
    eveplace=models.CharField(max_length=100,null=True,blank=True)
    evedate=models.DateField(max_length=100,null=True,blank=True)
    evedescription=models.CharField(max_length=100,null=True,blank=True)
    eveimage=models.ImageField(upload_to="Images",null=True,blank=True)
    eveorganiser=models.CharField(max_length=100,null=True,blank=True)
    evecontact=models.IntegerField(max_length=100,null=True,blank=True)
    eveguest=models.CharField(max_length=100,null=True,blank=True)




# Create your models here.
