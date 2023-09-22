"""
URL configuration for SumagoEnquiryManagementSystem project.

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
from django.urls import path,include
from django.views.generic import RedirectView
from SumagoEnquiryManagementSystem.views import department_index



urlpatterns = [
    path('admin/', admin.site.urls),
    path('enquiry_department/',include('enquiry_department.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('department_index/',department_index,name="department_index"),
    path('',RedirectView.as_view(url='/accounts/login'))
]
