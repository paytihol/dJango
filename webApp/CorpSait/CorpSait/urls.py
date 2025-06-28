"""
URL configuration for CorpSait project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import models
from django.contrib import admin
from django.urls import path#, handler403
from . import Views
handler403 = 'CorpSait.Views.permission_denied'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboba/', Views.aboba, name='aboba'),
    path('employee_info/', Views.employee_info, name='employee_info'),
    path('employee/<int:employee_id>', Views.employee_detail, name='employee'),
    path('employes/', Views.search_Employees, name = "search_Employees"),
    path('create_client/', Views.create_client, name = "create_client"),
    path('login/', Views.user_login, name = 'login'),
    path('logout/', Views.user_logout, name = 'logout'),
    
]

