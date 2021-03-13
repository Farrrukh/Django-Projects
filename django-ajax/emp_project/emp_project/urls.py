"""emp_project URL Configuration

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
from django.urls import path
from emp_project.emp_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('office',OfficeCrud,name="OfficeCrud"),
    path('employee',EmployeeCrud,name="EmployeeCrud"),
    path('offices',getAllOffices,name="getAllOffices"),
    path('employees',getAllEmployee,name="getAllEmployee"),
    path("pages/employee" , showEmployeePage),
    path("pages/office" , showOfficePage)



]
