from django.urls import path
from django.contrib.auth import views as aunt_views
from . import views

urlpatterns = [
    path('', aunt_views.LoginView.as_view(template_name='myweb/login.html'), name='login'),
    path('index', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('logout',views.logout, name='logout'),
    path('savoryfood',views.savoryfood, name='savoryfood'),

]