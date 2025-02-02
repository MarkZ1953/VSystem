# Generated by Django 4.2.16 on 2024-10-14 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
        migrations.AlterField(
            model_name='course_student',
            name='state',
            field=models.IntegerField(choices=[(0, 'Inscrito'), (1, 'Completado'), (2, 'Cancelado')], default=0),
        ),
    ]
