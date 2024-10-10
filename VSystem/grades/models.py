from django.db import models
from people.models import Person
from courses.models import Course
from django.core.validators import MaxValueValidator, MinValueValidator


class Grade(models.Model):
    grade = models.DecimalField(max_digits=3, decimal_places=2,  null=False, validators=[MaxValueValidator(5.00), MinValueValidator(0.00)], verbose_name="Grade")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, verbose_name="Course")
    student = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, verbose_name="Student")

    def __str__(self) -> str:
        return f"{self.grade}"

    class Meta:
        db_table = "grades"
        verbose_name = "Grade"
        verbose_name_plural = "Grades"
