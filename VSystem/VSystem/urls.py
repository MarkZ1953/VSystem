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
from people.views import StudentsView, DetailStudentView, AddStudentView, DeleteStudentView, ListStudentsView, UpdateStudentView, TeachersView, ListTeachersView, DetailTeacherView, AddTeacherView, UpdateTeacherView, DeleteTeacherView
from courses.views import ListCoursesView, AddCourseView, DeleteCourseView, UpdateCourseView, DetailCourseView, CoursesView, ClassesView, ListClassesView, AddClassView, DetailClassView, UpdateClassView, DeleteClassView
from enrollments.views import EnrollmentsView, AddEnrollmentView, ListEnrollmentsView, DetailEnrollmentView, UpdateEnrollmentView, DeleteEnrollmentView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('students/', StudentsView.as_view(), name='students'),
    path('students/get-students/', ListStudentsView.as_view(), name='get-students'),
    path('students/add-student/', AddStudentView.as_view(), name="add-student"),
    path('students/detail-student/<int:pk>/', DetailStudentView.as_view(), name="detail-student"),
    path('students/update-student/<int:pk>/', UpdateStudentView.as_view(), name="update-student"),
    path('students/delete-student/<int:pk>/', DeleteStudentView.as_view(), name="delete-student"),
    path('teachers/', TeachersView.as_view(), name='teachers'),
    path('teachers/get-teachers/', ListTeachersView.as_view(), name='get-teachers'),
    path('teachers/add-teacher/', AddTeacherView.as_view(), name="add-teacher"),
    path('teachers/detail-teacher/<int:pk>/', DetailTeacherView.as_view(), name="detail-teacher"),
    path('teachers/update-teacher/<int:pk>/', UpdateTeacherView.as_view(), name="update-teacher"),  
    path('teachers/delete-teacher/<int:pk>/', DeleteTeacherView.as_view(), name="delete-teacher"),
    path('courses/', CoursesView.as_view(), name='courses'),
    path('courses/get-courses/', ListCoursesView.as_view(), name='get-course'),
    path('courses/add-course/', AddCourseView.as_view(), name="add-course"),
    path('courses/detail-course/<int:pk>/', DetailCourseView.as_view(), name="detail-course"),
    path('courses/update-course/<int:pk>/', UpdateCourseView.as_view(), name="update-course"),  
    path('courses/delete-course/<int:pk>/', DeleteCourseView.as_view(), name="delete-course"),
    path('classes/', ClassesView.as_view(), name='classes'),
    path('classes/get-classes/', ListClassesView.as_view(), name='get-class'),
    path('classes/add-class/', AddClassView.as_view(), name="add-class"),
    path('classes/detail-class/<int:pk>/', DetailClassView.as_view(), name="detail-class"),
    path('classes/update-class/<int:pk>/', UpdateClassView.as_view(), name="update-class"),  
    path('classes/delete-class/<int:pk>/', DeleteClassView.as_view(), name="delete-class"),
    path('enrollments/', EnrollmentsView.as_view(), name='enrollments'),
    path('enrollments/get-enrollments/', ListEnrollmentsView.as_view(), name='get-enrollments'),
    path('enrollments/add-enrollment/', AddEnrollmentView.as_view(), name="add-enrollment"),
    path('enrollments/detail-enrollment/<int:pk>/', DetailEnrollmentView.as_view(), name="detail-enrollment"),
    path('enrollments/update-enrollment/<int:pk>/', UpdateEnrollmentView.as_view(), name="update-class"),  
    path('enrollments/delete-enrollment/<int:pk>/', DeleteEnrollmentView.as_view(), name="delete-class"),
]
