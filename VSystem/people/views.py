from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View, DetailView 
from .models import Person
from .forms import StudentAddForm, StudentDetailForm, StudentUpdateForm, TeacherDetailForm, TeacherAddForm, TeacherUpdateForm
from django.http import JsonResponse
from django.contrib import messages
from datetime import date, datetime


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

############################################################ Students ############################################################

class StudentsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'students.html', {'studentDetailForm': StudentDetailForm,
                                                'studentAddForm': StudentAddForm,
                                                'studentUpdateForm': StudentUpdateForm})


class ListStudentsView(ListView):
    def get(self, resquest, *args, **kwargs):
        students = Person.objects.filter(rol="Estudiante", isActive=True)
        studentsData = []

        for student in students:
            studentsData.append(
                {
                    "pk": student.id,
                    "fields": {
                        "firstName": student.firstName,
                        "lastName": student.lastName,
                        "document": student.document,
                        "email": student.email,
                        "phoneNumber": student.phoneNumber,
                        "birthDate": calculateAge(student.birthDate),
                        "isActive": student.isActive
                    }
                }
            )

        return JsonResponse({"success": True, "students": studentsData}, safe=False)


class AddStudentView(CreateView):
    form_class = StudentAddForm

    def post(self, request, *args, **kwargs):
        success = False

        firstName = request.POST["firstName"].strip()
        document = request.POST["document"].strip()
        lastName = request.POST["lastName"].strip()
        phoneNumber = request.POST["phoneNumber"].strip()
        email = request.POST["email"].strip()
        birthDate = request.POST["birthDate"].strip()

        age = calculateAge(datetime.strptime(birthDate, "%Y-%m-%d"))

        if Person.objects.filter(document=document, rol="Estudiante").exists():
            student = Person.objects.filter(document=document).first()
            message = f"El/La estudiante {student.firstName} {student.lastName} ya se encuentra registrado/a."
        elif int(age) < 3:
            message = "La edad mínima de el/la estudiante debe ser mayor a 3 años."
        else:
            student = Person(firstName=firstName, lastName=lastName, document=document, phoneNumber=phoneNumber, email=email, birthDate=birthDate, rol="Estudiante")
            message = f"Se ha guardado correctamente el/la estudiante {firstName} {lastName}"
            success = True
            student.save()

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
            student.isActive = False
            student.save()
            
        return JsonResponse({"success": True, "message": f"Se ha eliminado correctamente a el/la estudiante {student.firstName} {student.lastName}"})
    

class UpdateStudentView(UpdateView):
    model = Person
    form_class = StudentUpdateForm

    def post(self, request, *args, **kwargs):
        success = False
        studentObj = self.get_object()
        
        firstName = request.POST["firstName"].strip()
        document = request.POST["document"].strip()
        lastName = request.POST["lastName"].strip()
        phoneNumber = request.POST["phoneNumber"].strip()
        email = request.POST["email"].strip()
        birthDate = request.POST["birthDate"].strip()

        if document != studentObj.document and Person.objects.filter(document=document, rol="Estudiante"):
            student = Person.objects.filter(document=document, rol="Estudiante").first()
            message = f"El documento con número {student.document} de el/la estudiante {student.firstName} {student.lastName} ya se encuentra en uso. Por favor, compruebe los datos y vuelva a intentar."
            success = False
        else:
            studentObj.firstName = firstName
            studentObj.lastName = lastName
            studentObj.document = document
            studentObj.phoneNumber = phoneNumber
            studentObj.email = email
            studentObj.birthDate = birthDate
            studentObj.save()
            message = f"Se ha guardado los cambios correctamente de el/la estudiante {studentObj.firstName} {studentObj.lastName}."
            success = True

        return JsonResponse({"success": success, "message": message})


############################################################ Teachers ############################################################


class TeachersView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'teachers.html', {'teacherDetailForm': TeacherDetailForm,
                                                'teacherAddForm': TeacherAddForm,
                                                'teacherUpdateForm': TeacherUpdateForm})
    

class ListTeachersView(ListView):
    def get(self, resquest, *args, **kwargs):
        teachers = Person.objects.filter(rol="Docente", isActive=True)
        teachersData = []

        for teacher in teachers:
            teachersData.append(
                {
                    "pk": teacher.id,
                    "fields": {
                        "firstName": teacher.firstName,
                        "lastName": teacher.lastName,
                        "document": teacher.document,
                        "email": teacher.email,
                        "phoneNumber": teacher.phoneNumber,
                        "birthDate": calculateAge(teacher.birthDate),
                    }
                }
            )

        return JsonResponse({"success": True, "teachers": teachersData}, safe=False)


class AddTeacherView(CreateView):
    form_class = TeacherAddForm

    def post(self, request, *args, **kwargs):
        success = False

        firstName = request.POST["firstName"].strip()
        document = request.POST["document"].strip()
        lastName = request.POST["lastName"].strip()
        phoneNumber = request.POST["phoneNumber"].strip()
        email = request.POST["email"].strip()
        birthDate = request.POST["birthDate"].strip()

        age = calculateAge(datetime.strptime(birthDate, "%Y-%m-%d"))

        if Person.objects.filter(document=document, rol="Docente").exists():
            teacher = Person.objects.filter(document=document).first()
            message = f"El/La docente {teacher.firstName} {teacher.lastName} ya se encuentra registrado/a."
        elif int(age) < 18:
            message = "La edad mínima de el/la docente debe ser mayor a 18 años."    
        else:
            teacher = Person(firstName=firstName, lastName=lastName, document=document, phoneNumber=phoneNumber, email=email, birthDate=birthDate, rol="Docente", isActive=True)
            message = f"Se ha guardado correctamente el/la docente {firstName} {lastName}"
            success = True
            teacher.save()

        return JsonResponse({"success": success, "message": message})


class DetailTeacherView(DetailView):
    model = Person

    def get(self, request, *args, **kwargs):
        teacher = self.get_object()

        teacherData = {
            "pk": teacher.pk,
            "fields": {
                "firstName": teacher.firstName,
                "lastName": teacher.lastName,
                "document": teacher.document,
                "email": teacher.email,
                "phoneNumber": teacher.phoneNumber,
                "birthDate": teacher.birthDate
            }
        }

        return JsonResponse({"success": True, "teacher": teacherData})


class UpdateTeacherView(UpdateView):
    model = Person
    form_class = TeacherUpdateForm

    def post(self, request, *args, **kwargs):
        success = False
        teacherObj = self.get_object()
        
        firstName = request.POST["firstName"].strip()
        document = request.POST["document"].strip()
        lastName = request.POST["lastName"].strip()
        phoneNumber = request.POST["phoneNumber"].strip()
        email = request.POST["email"].strip()
        birthDate = request.POST["birthDate"].strip()

        if document != teacherObj.document and Person.objects.filter(document=document, rol="Docente"):
            teacher = Person.objects.filter(document=document, rol="Docente").first()
            message = f"El documento con número {teacher.document} de el/la docente {teacher.firstName} {teacher.lastName} ya se encuentra en uso. Por favor, compruebe los datos y vuelva a intentar."
            success = False
        else:
            teacherObj.firstName = firstName
            teacherObj.lastName = lastName
            teacherObj.document = document
            teacherObj.phoneNumber = phoneNumber
            teacherObj.email = email
            teacherObj.birthDate = birthDate
            teacherObj.save()
            message = f"Se ha guardado los cambios correctamente de el/la docente {teacherObj.firstName} {teacherObj.lastName}."
            success = True

        return JsonResponse({"success": success, "message": message})


class DeleteTeacherView(DeleteView):
    model = Person

    def post(self, request, *args, **kwargs):
        teacher = self.get_object()

        if teacher:
            teacher.isActive = False
            teacher.save()
            
        return JsonResponse({"success": True, "message": f"Se ha eliminado correctamente a el/la docente {teacher.firstName} {teacher.lastName}"})
    