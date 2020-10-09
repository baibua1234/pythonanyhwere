from django.contrib import admin
from django.urls import path, include
from myweb import views
from django.contrib.auth import views as aunt_views

urlpatterns = [
    path('index', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('', aunt_views.LoginView.as_view(template_name='myweb/login.html'), name='login'),
    path('logout/',views.logout, name='logout'),
    path('savoryfood/',views.savoryfood, name='savoryfood'),
    path('singledish/',views.singledish, name='singledish'),
    path('snackfood/',views.snackfood, name='snackfood'),
    path('sweettreat/',views.sweettreat, name='sweettreat'),
    path('myweb/', include('myweb.urls')),

]
