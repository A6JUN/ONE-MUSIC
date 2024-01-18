from django.shortcuts import render,redirect
from Adminapp.models import addMusicdb,addcatedb,replydb,addeventdb
from frontendapp.models import contactdb,signupdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def indexpage(req):
    return render(req,"index.html")

def addcate(req):
    return render(req,'Addcategory.html')


def catedatasave(req):
    if req.method=="POST":
        catna=req.POST.get('catname')
        cimg=req.FILES['catimage']
        obj=addcatedb(catname=catna,catimage=cimg)
        obj.save()
        messages.success(req,"Category added Successfully")

        return redirect(addcate)

def categorydisplay(req):
    data=addcatedb.objects.all()
    return render(req,'displaycategory.html',{'data':data})

def Categorydelete(req,dataid):
    data=addcatedb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Deleted Successfully")

    return redirect(categorydisplay)

def categoryupdate(req,dataid):
  if req.method=="POST":
      catna = req.POST.get('catname')
      try:
          cimg = req.FILES['catimage']
          fs = FileSystemStorage()
          file = fs.save(cimg.name, cimg)
      except MultiValueDictKeyError:
          file = addcatedb.objects.get(id=dataid).catimage
      addcatedb.objects.filter(id=dataid).update(catname=catna,catimage=file)
      messages.success(req, "Category Edited Successfully")

      return redirect(categorydisplay)



def categoryedit(req,dataid):
    data=addcatedb.objects.get(id=dataid)
    return render(req,"CAtegoryedit.html",{'data':data})


def AddMusic(req):
    selcat=addcatedb.objects.all()
    return render(req,"addmusic.html",{'selcat':selcat})

def addmusicsave(req):
    if req.method=="POST":
        cat=req.POST.get('category')
        mna=req.POST.get('mname')
        cna=req.POST.get('cname')
        mus=req.FILES['music']
        des=req.POST.get('description')
        img=req.FILES['image']
        obj=addMusicdb(category=cat,mname=mna,cname=cna,music=mus,description=des,image=img)
        obj.save()
        messages.success(req,"Music added Successfully")

        return redirect(AddMusic)

def DisplayMusic(req):
    data=addMusicdb.objects.all()
    return render(req,"displaymusic.html",{'data':data})


def musicdelete(req,dataid):
    data=addMusicdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Deleted Successfully")

    return redirect(DisplayMusic)

def catupdate(req,dataid):
  if req.method=="POST":
      cat = req.POST.get('category')
      mna = req.POST.get('mname')
      cna = req.POST.get('cname')
      des = req.POST.get('description')

      try:
         mus = req.FILES['music']
         img = req.FILES['image']
         fs=FileSystemStorage()
         file=fs.save(mus.name,mus)
         file1=fs.save(img.name,img)
      except MultiValueDictKeyError:
         file=addMusicdb.objects.get(id=dataid).music
         file1=addMusicdb.objects.get(id=dataid).image
      addMusicdb.objects.filter(id=dataid).update(category=cat,mname=mna,cname=cna,music=file,description=des,image=file1)
      messages.success(req, "Edited Successfully")

      return redirect(DisplayMusic)



def catedit(req,dataid):
    data2 = addcatedb.objects.all()
    data=addMusicdb.objects.get(id=dataid)

    return render(req,"musicedit.html",{'data':data,'data2':data2})

def admin_login(request):
    return render(request,"adminlogin.html")

def Adminlogin(request):
    if request.method=='POST':
        un=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(indexpage)
            else:
                return redirect(admin_login)

        else:
            return redirect(admin_login)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)


def Usermessage(req):
    data=contactdb.objects.all()
    return render(req,'usermessages.html',{'data':data})

def msgdelete(req,dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(Usermessage)


def Reply(req):
    return render(req,'reply.html')

def replysave(req):
    if req.method=="POST":
        rp=req.POST.get('reply')
        obj=replydb(reply=rp)
        obj.save()
        messages.success(req, "Message Sent")

        return redirect(Usermessage)


def AddEvents(req):
    return render(req,'addevents.html')

def addeventsave(req):
    if req.method=="POST":
        en=req.POST.get('evename')
        ep=req.POST.get('eveplace')
        ed=req.POST.get('evedate')
        edes=req.POST.get('evedescription')
        eimg=req.FILES['eveimage']
        eog=req.POST.get('eveorganiser')
        ec=req.POST.get('evecontact')
        eg=req.POST.get('eveguest')

        obj=addeventdb(evename=en,eveplace=ep,evedate=ed,evedescription=edes,eveimage=eimg,eveorganiser=eog,evecontact=ec,eveguest=eg)
        obj.save()
        messages.success(req,"Event added Successfully")

        return redirect(AddEvents)


def Displayevents(req):
    data=addeventdb.objects.all()
    return render(req,"displayevents.html",{'data':data})

def eventedit(req,dataid):
    data=addeventdb.objects.get(id=dataid)
    return render(req,"editevents.html",{'data':data})


def eventdelete(req,dataid):
    data=addeventdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Deleted Successfully")

    return redirect(Displayevents)


def eventupdate(req,dataid):
  if req.method=="POST":
      en = req.POST.get('evename')
      ep = req.POST.get('eveplace')
      ed = req.POST.get('evedate')
      edes = req.POST.get('evedescription')
      eog = req.POST.get('eveorganiser')
      ec = req.POST.get('evecontact')
      eg = req.POST.get('eveguest')
      try:
          eimg = req.FILES['eveimage']
          fs = FileSystemStorage()
          file = fs.save(eimg.name, eimg)
      except MultiValueDictKeyError:
          file = addcatedb.objects.get(id=dataid).eveimage
      addeventdb.objects.filter(id=dataid).update(evename=en,eveplace=ep,evedate=ed,evedescription=edes,eveimage=file,eveorganiser=eog,evecontact=ec,eveguest=eg)
      messages.success(req, "Category Edited Successfully")

      return redirect(Displayevents)





# Create your views here.
