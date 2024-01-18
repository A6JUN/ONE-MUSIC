from django.urls import path
from Adminapp import views


urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('AddMusic/',views.AddMusic,name="AddMusic"),
    path('addcate/',views.addcate,name="addcate"),
    path('catedatasave/',views.catedatasave,name="catedatasave"),
    path('categorydisplay/',views.categorydisplay,name="categorydisplay"),
    path('Categorydelete/<int:dataid>',views.Categorydelete,name="Categorydelete"),
    path('categoryupdate/<int:dataid>',views.categoryupdate,name="categoryupdate"),
    path('categoryedit/<int:dataid>',views.categoryedit,name="categoryedit"),
    path('addmusicsave/',views.addmusicsave,name="addmusicsave"),
    path('DisplayMusic/',views.DisplayMusic,name="DisplayMusic"),
    path('musicdelete/<int:dataid>/',views.musicdelete,name="musicdelete"),
    path('catedit/<int:dataid>/',views.catedit,name="catedit"),
    path('catupdate/<int:dataid>/',views.catupdate,name="catupdate"),

    path('admin_login/', views.admin_login, name="admin_login"),
    path('Adminlogin/', views.Adminlogin, name="Adminlogin"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),

    path('Usermessage/', views.Usermessage, name="Usermessage"),
    path('msgdelete/<int:dataid>', views.msgdelete, name="msgdelete"),

    path('Reply/', views.Reply, name="Reply"),
    path('replysave/', views.replysave, name="replysave"),



    path('AddEvents/', views.AddEvents, name="AddEvents"),
    path('addeventsave/', views.addeventsave, name="addeventsave"),
    path('Displayevents/', views.Displayevents, name="Displayevents"),
    path('eventdelete/<int:dataid>', views.eventdelete, name="eventdelete"),
    path('eventupdate/<int:dataid>', views.eventupdate, name="eventupdate"),
    path('eventedit/<int:dataid>', views.eventedit, name="eventedit"),

]