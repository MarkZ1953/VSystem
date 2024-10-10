from django.db import models


class Person(models.Model):
    firstName = models.CharField(max_length=64, verbose_name="First Name")
    lastName = models.CharField(max_length=64, verbose_name="Last Name")
    document = models.CharField(max_length=16, verbose_name="Document")
    phoneNumber = models.CharField(max_length=16, verbose_name="Phone Number")
    email = models.CharField(max_length=128, verbose_name="Email")
    birthDate = models.DateField(verbose_name="Birth Date")
    rol = models.CharField(max_length=32, verbose_name="Rol")

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}"

    class Meta:
        db_table = "people"
        verbose_name = "Person"
        verbose_name_plural = "People"
