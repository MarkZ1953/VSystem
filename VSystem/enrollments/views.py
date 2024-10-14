from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View, DetailView 
from enrollments.models import Enrollment
from .forms import EnrollmentAddForm, EnrollmentUpdateForm, EnrollmentDetailForm
from courses.models import Course_Student


class EnrollmentsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'enrollments.html', {"enrollmentAddForm": EnrollmentAddForm,
                                                    "enrollmentUpdateForm": EnrollmentUpdateForm,
                                                    "enrollmentDetailForm": EnrollmentDetailForm}) 
    

class ListEnrollmentsView(ListView):
    def get(self, resquest, *args, **kwargs):
        enrollments = Enrollment.objects.filter(isActive=True, studentCourse__student__isActive=True, studentCourse__course__isActive=True)
        enrollmentsData = []

        for enrollment in enrollments:
            enrollmentsData.append(
                {
                    "pk": enrollment.id,
                    "fields": {
                        "studentCourse": enrollment.studentCourse.__str__(),
                        "startDate": enrollment.startDate,
                        "cost": enrollment.cost,
                        "state": enrollment.get_state_display()
                    }
                }
            )

        return JsonResponse({"success": True, "enrollments": enrollmentsData}, safe=False)


class AddEnrollmentView(CreateView):
    form_class = EnrollmentAddForm

    def post(self, request, *args, **kwargs):
        state = request.POST["state"].strip()
        startDate = request.POST["startDate"].strip()
        cost = request.POST["cost"].strip()
        studentCourse = Course_Student.objects.get(id=request.POST["studentCourse"].strip())

        enrollment = Enrollment(studentCourse=studentCourse, cost=cost, startDate=startDate, state=state)
        message = f"Se ha guardado correctamente la matricula de la clase {studentCourse}"
        enrollment.save()

        return JsonResponse({"success": True, "message": message})
    

class DetailEnrollmentView(DetailView):
    model = Enrollment

    def get(self, request, *args, **kwargs):
        enrollment = self.get_object()

        courseStudentData = {
            "pk": enrollment.id,
            "fields": {
                "studentCourse": enrollment.studentCourse.__str__(),
                "startDate": enrollment.startDate,
                "cost": enrollment.cost,
                "state": enrollment.get_state_display()
            }
        }

        return JsonResponse({"success": True, "enrollment": courseStudentData})


class DeleteEnrollmentView(DeleteView):
    model = Enrollment

    def post(self, request, *args, **kwargs):
        enrollment = self.get_object()

        if enrollment:
            enrollment.isActive = False
            enrollment.save()
            
        return JsonResponse({"success": True, "message": f"Se ha eliminado correctamente a la matricula de {enrollment.studentCourse}."})
    

class UpdateEnrollmentView(UpdateView):
    model = Enrollment
    form_class = EnrollmentUpdateForm

    def post(self, request, *args, **kwargs):
        success = False
        enrollmentObj = self.get_object()
        
        state = request.POST["state"].strip()
        startDate = request.POST["startDate"].strip()
        cost = request.POST["cost"].strip()
        studentCourse = Course_Student.objects.get(id=request.POST["studentCourse"].strip())

        enrollmentObj.studentCourse = studentCourse
        enrollmentObj.cost = cost
        enrollmentObj.startDate = startDate
        enrollmentObj.state = state  
        enrollmentObj.save()

        message = f"Se ha guardado los cambios correctamente de la matricula de la clase {enrollmentObj.studentCourse}."
        success = True

        return JsonResponse({"success": success, "message": message})

    def get(self, request, *args, **kwargs):
        enrollment = self.get_object()

        courseStudentData = {
            "pk": enrollment.id,
            "fields": {
                "studentCourse": enrollment.studentCourse.id,
                "startDate": enrollment.startDate,
                "cost": enrollment.cost,
                "state": enrollment.state
            }
        }

        return JsonResponse({"success": True, "enrollment": courseStudentData})
    