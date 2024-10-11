from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View, DetailView 
from .models import Person
from .forms import StudentAddForm, StudentDetailForm
from django.http import JsonResponse
from django.contrib import messages


class StudentsView(View):
    def get(self, request, *args, **kwargs):
        students = Person.objects.filter(rol="Estudiante")
        return render(request, 'students.html', {'studentDetailForm': StudentDetailForm,
                                                'studentAddForm': StudentAddForm,
                                                'students': students})


class AddStudentView(CreateView):
    form_class = StudentAddForm

    def post(self, request, *args, **kwargs):
        success = False

        firstName = request.POST["firstName"].strip()
        lastName = request.POST["lastName"].strip()
        phoneNumber = request.POST["phoneNumber"].strip()
        email = request.POST["email"].strip()
        birthDate = request.POST["birthDate"].strip()

        if not firstName and lastName and phoneNumber and email and birthDate:
            success = False
            messages = "Por favor complete todos los campos necesarios."
        else:
            message = f"Se ha guardado correctamente el/la estudiante {firstName} {lastName}"
            success = True  

        return JsonResponse({"success": success, "message": message})
    

class DetailStudentView(DetailView):
    model = Person

    def get(self, request, *args, **kwargs):
        student = self.get_object()

        studentData = {
            "pk": student.pk,
            "fields": {
                "firstName": student.firstName,
                "lastName": student.lastName,
                "document": student.document,
                "email": student.email,
                "phoneNumber": student.phoneNumber,
                "birthDate": student.birthDate
            }
        }

        return JsonResponse({"success": True, "student": studentData})


class DeleteStudentView(DeleteView):
    model = Person

    def post(self, request, *args, **kwargs):
        student = self.get_object()
        if student:
            student.delete()
            
        return JsonResponse({"success": True, "message": f"Se ha eliminado correctamente a el/la estudiante {student.firstName} {student.lastName}"})
    