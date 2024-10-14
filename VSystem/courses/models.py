from django.db import models
from people.models import Person
from django.core.exceptions import ValidationError
from .choices import STATUS_CHOICES


class Course(models.Model):
    name = models.CharField(max_length=64, verbose_name="Name")
    maxCapacity = models.IntegerField(verbose_name="Max Capacity")
    teacher = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, db_column="teacherId")
    isActive = models.BooleanField(default=True, verbose_name="Is Active")

    def __str__(self) -> str:
        return self.name

    def clean(self) -> None:
        if self.teacher.rol != "Docente":
            raise ValidationError("Se debe elegir a una persona con el rol 'Docente' para poder guardar el curso.")

    class Meta:
        db_table = "courses"
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Course_Student(models.Model):
    student = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, db_column="studentId", verbose_name="Student")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, db_column="courseId", verbose_name="Course")
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    state = models.IntegerField(choices=STATUS_CHOICES, default=0)
    isActive = models.BooleanField(default=True, verbose_name="Is Active")

    def __str__(self) -> str:
        return f"{self.course} | {self.student}"

    class Meta:
        db_table = "courses_students"
        verbose_name = "Course Student"
        verbose_name_plural = "Courses Students"
