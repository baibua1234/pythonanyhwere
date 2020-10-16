from django.contrib import admin
from django.urls import path, include
#from myweb import views
#from django.contrib.auth import views as aunt_views

urlpatterns = [
    path('', include('myweb.urls')),
    path('admin/', admin.site.urls),

]
