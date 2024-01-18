from django.shortcuts import render,redirect
from Adminapp.models import addMusicdb,addcatedb,replydb,addeventdb
from frontendapp.models import signupdb, contactdb, likedb
from django.contrib import messages

def mainpage(req):
    mus=addMusicdb.objects.all()
    cat=addcatedb.objects.all()
    return render(req,'mainpage.html',{'mus':mus,'cat':cat})

# def Albumspage(req):
#     mus=addMusicdb.objects.all()
#     cat=addcatedb.objects.all()
#     return render(req,'albums.html',{'mus':mus,'cat':cat})


def Albumspage1(req):
    mus=addMusicdb.objects.all()
    cat=addcatedb.objects.all()
    return render(req,'album1.html',{'mus':mus,'cat':cat})

def Singlesong(req,proid):
    data = addMusicdb.objects.get(id=proid)
    cat=addcatedb.objects.all()
    return render(req,"singlesong.html",{'data':data,'cat':cat})

def categorysong(req,cat_name):
    data= addMusicdb.objects.filter(category=cat_name)
    cat=addcatedb.objects.all()


    return render(req,'CategorySong.html',{'data':data,'cat':cat})


def HH(req):
    mus=addMusicdb.objects.all()
    cat=addcatedb.objects.all()
    return render(req,'hhh.html',{'mus':mus,'cat':cat})

def loginpage(req):
    return render(req,"Login.html")


def Registerpage(req):
    return render(req,"Register.html")

def signupdata(req):
  if req.method=="POST":
        sna=req.POST.get('susername')
        sem=req.POST.get('semail')
        snum= req.POST.get('snumber')
        spw= req.POST.get('spassword')
        obj=signupdb(susername=sna,semail=sem,snumber=snum,spassword=spw)
        obj.save()
        return redirect(Registerpage)

def UserLogin(request):
    if request.method=="POST":
        un=request.POST.get('lname')
        pw=request.POST.get('lpassword')
        if signupdb.objects.filter(susername=un,spassword=pw).exists():
            request.session['susername']=un
            request.session['spassword']=pw
            messages.success(request, "Welcome")

            return redirect(mainpage)
        else:
            messages.error(request, "Invalid UserName or Password")


            return redirect(loginpage)
    return redirect(loginpage)


def UserLogout(request):
    del request.session['susername']
    del request.session['spassword']
    return redirect(loginpage)

def Contact(req):
    cat=addcatedb.objects.all()
    return render(req,'contact.html',{'cat':cat})


def contactdata(req):
  if req.method=="POST":
        na=req.POST.get('name')
        sub= req.POST.get('subject')
        msg= req.POST.get('message')
        obj=contactdb(name=na,subject=sub,message=msg)
        obj.save()
        messages.success(req, "Message Sent")
        return redirect(Contact)

def Profilepage(request):
    mus = addMusicdb.objects.all()
    cat = addcatedb.objects.all()
    selcat=addcatedb.objects.all()
    data1 = likedb.objects.filter(likusername=request.session['susername'])

    return render(request,'profilepage.html',{'cat':cat,'mus':mus,'data1':data1,'selcat':selcat})



def Inbox(req):
    data=replydb.objects.all()

    cat=addcatedb.objects.all()

    return render(req,'inbox.html',{'data':data,'cat':cat})



def likeddata(req):
  if req.method=="POST":
        ln= req.POST.get('likmname')
        ldes= req.POST.get('likdescription')
        lcn=req.POST.get('likcname')
        lm=req.POST.get('likmusic')
        li= req.POST.get('likimage')
        lu= req.POST.get('likusername')
        obj=likedb(likmname=ln,likdescription=ldes,likcname=lcn,likmusic=lm,likimage=li,likusername=lu)
        obj.save()
        return redirect(Profilepage)
        # messages.success(req, "Added to cart")

def likeitemdelete(request,dataid):
    data=likedb.objects.filter(id=dataid)
    data.delete()
    # messages.success(request, "Deleted successfully")

    return redirect(Profilepage)


def News(req):
    cat = addcatedb.objects.all()
    return render(req,'news.html',{'cat':cat})


def Events(req):
    cat = addcatedb.objects.all()
    data=addeventdb.objects.all()
    return render(req,'events.html',{'cat':cat,'data':data})

# Create your views here.
