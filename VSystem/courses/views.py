from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View, DetailView 
from .models import Course, Course_Student
from people.models import Person
from django.http import JsonResponse
from .forms import CourseAddForm, CourseDetailForm, CourseUpdateForm, ClassAddForm, ClassUpdateForm, ClassDetailForm


############################################################ Courses ############################################################


class CoursesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'courses.html', {'courseDetailForm': CourseDetailForm,
                                                'courseAddForm': CourseAddForm,
                                                'courseUpdateForm': CourseUpdateForm}) 


class ListCoursesView(ListView):
    def get(self, resquest, *args, **kwargs):
        courses = Course.objects.filter(isActive=True, teacher__isActive=True)
        coursesData = []

        for course in courses:
            coursesData.append(
                {
                    "pk": course.id,
                    "fields": {
                        "name": course.name,
                        "maxCapacity": course.maxCapacity,
                        "teacher": course.teacher.__str__()
                    }
                }
            )

        return JsonResponse({"success": True, "courses": coursesData}, safe=False)


class AddCourseView(CreateView):
    form_class = CourseAddForm

    def post(self, request, *args, **kwargs):
        name = request.POST["name"].strip()
        maxCapacity = request.POST["maxCapacity"].strip()
        teacher = Person.objects.get(id=request.POST["teacher"].strip())

        course = Course(name=name, maxCapacity=maxCapacity, teacher=teacher)
        message = f"Se ha guardado correctamente el curso {name}"
        course.save()

        return JsonResponse({"success": True, "message": message})


class DeleteCourseView(DeleteView):
    model = Course

    def post(self, request, *args, **kwargs):
        course = self.get_object()

        if course:
            course.isActive = False
            course.save()
            
        return JsonResponse({"success": True, "message": f"Se ha eliminado correctamente a el curso de {course}"})


class DetailCourseView(DetailView):
    model = Course

    def get(self, request, *args, **kwargs):
        course = self.get_object()

        courseData = {
            "pk": course.pk,
            "fields": {
                "name": course.name,
                "maxCapacity": course.maxCapacity,
                "teacher": course.teacher.__str__(),
            }
        }

        return JsonResponse({"success": True, "course": courseData})


class UpdateCourseView(UpdateView):
    model = Course
    form_class = CourseUpdateForm

    def post(self, request, *args, **kwargs):
        success = False
        courseObj = self.get_object()
        
        name = request.POST["name"].strip()
        maxCapacity = request.POST["maxCapacity"].strip()
        teacher = Person.objects.get(id=request.POST["teacher"].strip())

        courseObj.name = name
        courseObj.teacher = teacher
        courseObj.maxCapacity = maxCapacity
        courseObj.save()

        message = f"Se ha guardado los cambios correctamente del {courseObj.name}."
        success = True

        return JsonResponse({"success": success, "message": message})

    def get(self, request, *args, **kwargs):
        course = self.get_object()

        courseData = {
            "pk": course.pk,
            "fields": {
                "name": course.name,
                "maxCapacity": course.maxCapacity,
                "teacher": course.teacher.id,
            }
        }

        return JsonResponse({"success": True, "course": courseData})


############################################################ Classes ############################################################


class ClassesView(View):    
    def get(self, request, *args, **kwargs):
        return render(request, 'classes.html', {'classDetailForm': ClassDetailForm,
                                                'classAddForm': ClassAddForm,
                                                'classUpdateForm': ClassUpdateForm}) 
    

class ListClassesView(ListView):
    def get(self, resquest, *args, **kwargs):
        coursesStudents = Course_Student.objects.filter(student__rol="Estudiante", student__isActive=True, course__isActive=True, isActive=True)
        coursesStudentsData = []

        for courseStudent in coursesStudents:
            coursesStudentsData.append(
                {
                    "pk": courseStudent.id,
                    "fields": {
                        "student": courseStudent.student.__str__(),
                        "course": courseStudent.course.__str__(),
                        "startDate": courseStudent.startDate,
                        "endDate": courseStudent.endDate,
                        "state": courseStudent.get_state_display()
                    }
                }
            )

        return JsonResponse({"success": True, "coursesStudents": coursesStudentsData}, safe=False)


class AddClassView(CreateView):
    form_class = CourseAddForm

    def post(self, request, *args, **kwargs):
        student = Person.objects.get(id=request.POST["student"].strip())
        course = Course.objects.get(id=request.POST["course"].strip())
        startDate = request.POST["startDate"].strip()
        endDate = request.POST["endDate"].strip()
        state = request.POST["state"].strip()

        courseStudent = Course_Student(student=student, course=course, startDate=startDate, endDate=endDate, state=state)
        message = f"Se ha agregado correctamente el/la {student} al curso de {course}"
        courseStudent.save()

        return JsonResponse({"success": True, "message": message})
    

class DetailClassView(DetailView):
    model = Course_Student

    def get(self, request, *args, **kwargs):
        courseStudent = self.get_object()

        courseStudentData = {
            "pk": courseStudent.pk,
            "fields": {
                "student": courseStudent.student.__str__(),
                "course": courseStudent.course.__str__(),
                "startDate": courseStudent.startDate,
                "endDate": courseStudent.endDate,
                "state": courseStudent.get_state_display(),
            }
        }

        return JsonResponse({"success": True, "class": courseStudentData})
    

class DeleteClassView(DeleteView):
    model = Course_Student

    def post(self, request, *args, **kwargs):
        courseStudent = self.get_object()

        if courseStudent:
            courseStudent.isActive = False
            courseStudent.save()
            
        return JsonResponse({"success": True, "message": f"Se ha eliminado correctamente a el/la {courseStudent.student} del curso de {courseStudent.course}"})


class UpdateClassView(UpdateView):
    model = Course_Student
    form_class = ClassUpdateForm

    def post(self, request, *args, **kwargs):
        success = False
        classObj = self.get_object()
        
        student = Person.objects.get(id=request.POST["student"].strip())
        course = Course.objects.get(id=request.POST["course"].strip())
        startDate = request.POST["startDate"].strip()
        endDate = request.POST["endDate"].strip()
        state = request.POST["state"].strip()

        classObj.student = student
        classObj.course = course
        classObj.startDate = startDate
        classObj.endDate = endDate
        classObj.state = state  
        classObj.save()

        message = f"Se ha guardado los cambios correctamente en la relacion de el/la estudiante {student} y el curso de {course}."
        success = True

        return JsonResponse({"success": success, "message": message})

    def get(self, request, *args, **kwargs):
        courseStudent = self.get_object()

        courseStudentData = {
            "pk": courseStudent.pk,
            "fields": {
                "student": courseStudent.student.id,
                "course": courseStudent.course.id,
                "startDate": courseStudent.startDate,
                "endDate": courseStudent.endDate,
                "state": courseStudent.state,
            }
        }

        return JsonResponse({"success": True, "class": courseStudentData})