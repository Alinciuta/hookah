"""proiect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('location/', include('aplicatie1.urls')),
    path('companies/', include('aplicatie2.urls')),
    path('jobs/', include('aplicatie3.urls')),
    path('', include('django.contrib.auth.urls'), {'next_page': '/'}, name='login'),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
]
