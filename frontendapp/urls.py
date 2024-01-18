from django.urls import path
from frontendapp import views

urlpatterns=[
path('mainpage/',views.mainpage,name="mainpage"),
path('Albumspage1/',views.Albumspage1,name="Albumspage1"),
path('Contact/',views.Contact,name="Contact"),
path('contactdata/',views.contactdata,name="contactdata"),
path('Singlesong/<int:proid>/',views.Singlesong,name="Singlesong"),
path('categorysong/<cat_name>/', views.categorysong, name="categorysong"),


path('loginpage/', views.loginpage, name="loginpage"),
path('Registerpage/', views.Registerpage, name="Registerpage"),
path('signupdata/', views.signupdata, name="signupdata"),
path('UserLogin/', views.UserLogin, name="UserLogin"),
path('UserLogout/', views.UserLogout, name="UserLogout"),


path('HH/', views.HH, name="HH"),
path('Profilepage/', views.Profilepage, name="Profilepage"),
# path('useraddmusicsave/', views.useraddmusicsave, name="useraddmusicsave"),
path('Inbox/', views.Inbox, name="Inbox"),

path('likeddata/', views.likeddata, name="likeddata"),
path('likeitemdelete/<int:dataid>/', views.likeitemdelete, name="likeitemdelete"),

path('News/',views.News,name="News"),
path('Events/',views.Events,name="Events"),

]