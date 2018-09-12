#from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path ('hello/',   views.hello,    name="helloview"),
    path ('liveops/',  views.liveops, name="liveopsview"),
    path('posts_table/',views.posts_table,name='posts_table'),
    path('boards_table/',views.boards_table,name='boards_table'),
    path('topics_table/',views.topics_table,name='topics_table'),
    path('fetchdata_form/',views.fetchdataform_table,name='fetchdata_form'),
    path('login_form/',views.login_form_table,name='login_form'),
    path('SignupForm_Example/',views.SignupForm_Example_f,name='SignupForm_Example'),



]