from django.urls import path,include
from django.contrib.auth import views as aunt_views
from . import views
from . import *
urlpatterns = [
    path('', aunt_views.LoginView.as_view(template_name='myweb/login.html'), name='login'),
    path('index', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('logout',views.logout, name='logout'),
    path('savoryfood',views.savoryfood, name='savoryfood'),
    path('singledish',views.singledish, name='singledish'),
    path('snackfood',views.snackfood, name='snackfood'),
    path('sweettreat',views.sweettreat, name='sweettreat'),
    path('showFood', views.showFood,name="showFood"),
    path('addfood', views.addfood,name="addfood")

]