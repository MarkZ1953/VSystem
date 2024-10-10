"""
URL configuration for VSystem project.

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
from django.contrib import admin
from django.urls import path, include
from webApp.views import IndexView
from people.views import StudentsView, DetailStudentView, AddStudentView
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('students/', StudentsView.as_view(), name='students'),
    path('students/get-student/<int:pk>/', DetailStudentView.as_view(), name="detail-student"),
    path('students/add-student/', AddStudentView.as_view(), name="add-student"),
]
