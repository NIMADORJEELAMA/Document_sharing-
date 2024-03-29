"""
URL configuration for filesharing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project import views
# from .views import UploadView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.projectview),
    path('signin/',views.signview,name='signin'),
    path('login/',views.user_login,name='login'),
    path('contact/',views.contactpage,name='contact'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('dashboard/', views.dashboard_view,name='dashboard'),
    path('upload.html/', views.uploadpage,name='upload'),
    path('admin_main/', views.adminpage,name='admin'),


]
