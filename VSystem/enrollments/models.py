from django.db import models
from people.models import Person
from courses.models import Course_Student
from .choices import STATUS_CHOICES


class Enrollment(models.Model):
    state = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name="State")
    startDate = models.DateField(verbose_name="Start Date")
    cost = models.FloatField(verbose_name="Cost")
    studentCourse = models.ForeignKey(Course_Student, on_delete=models.SET_NULL, null=True, db_column="studentId", verbose_name="Student")
    isActive = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.get_state_display()} | {self.studentCourse}"

    class Meta:
        db_table = "enrollements"
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"
