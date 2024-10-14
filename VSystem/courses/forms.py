from django.forms import ModelForm, CharField, TextInput, ChoiceField, Select, DateField, DateInput
from people.models import Person
from .models import Course, Course_Student
from .choices import STATUS_CHOICES


class CourseAddForm(ModelForm):
    name = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "64",
            "name": "inputNameAdd",
            "id": "inputNameAdd"
        }
    ))

    teacher = ChoiceField(
        widget=Select(
            attrs={
                "class": "form-control",
                "id": "selectTeacherAdd"
            }
        )
    )
    
    maxCapacity = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "type": "number",
            "min": "0",
            "step": "1",
            "id": "inputMaxCapacityAdd"
        }
    ))

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailForm(ModelForm):
    name = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "64",
            "id": "inputNameDetail",
            "readonly": True,
            "disabled": True
        }
    ))

    teacher = CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "id": "inputTeacherDetail",
                "readonly": True,
                "disabled": True
            }
        )
    )
    
    maxCapacity = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "type": "number",
            "min": "0",
            "step": "1",
            "id": "inputMaxCapacityDetail",
            "readonly": True,
            "disabled": True
        }
    ))

    class Meta:
        model = Course
        fields = "__all__"


class CourseUpdateForm(ModelForm):
    name = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "64",
            "id": "inputNameUpdate"
        }
    ))

    teacher = ChoiceField(
        widget=Select(
            attrs={
                "class": "form-control",
                "id": "selectTeacherUpdate"
            }
        )
    )
    
    maxCapacity = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "type": "number",
            "min": "0",
            "step": "1",
            "id": "inputMaxCapacityUpdate"
        }
    ))

    class Meta:
        model = Course
        fields = "__all__"


class ClassAddForm(ModelForm):
    student = ChoiceField(
        widget=Select(        
            attrs={
                "class": "form-control",
                "id": "selectStudentAdd"
            }
        )
    )

    course = ChoiceField(
        widget=Select(
            attrs={
                "class": "form-control",
                "id": "selectCourseAdd"
            }
        )
    )
    
    startDate = DateField(
        widget=DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "id": "inputStartDateAdd"
            }
        )
    )

    endDate = DateField(
        widget=DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "id": "inputEndDateAdd"
            }
        )
    )

    state = ChoiceField(
        choices=STATUS_CHOICES,
        widget=Select(        
            attrs={
                "class": "form-control",
                "id": "selectStateAdd"
            }
        )
    )

    class Meta:
        model = Course_Student  
        fields = "__all__"


class ClassDetailForm(ModelForm):
    student = CharField(
        widget=TextInput(        
            attrs={
                "class": "form-control",
                "id": "inputStudentDetail",
                "readonly": True,
                "disabled": True
            }
        )
    )

    course = CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "id": "inputCourseDetail",
                "readonly": True,
                "disabled": True
            }
        )
    )
    
    startDate = DateField(
        widget=DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "id": "inputStartDateDetail",
                "readonly": True,
                "disabled": True
            }
        )
    )

    endDate = DateField(
        widget=DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "id": "inputEndDateDetail",
                "readonly": True,
                "disabled": True
            }
        )
    )

    state = DateField(
        widget=DateInput(        
            attrs={
                "class": "form-control",
                "id": "inputStateDetail",
                "readonly": True,
                "disabled": True
            }
        )
    )

    class Meta:
        model = Course_Student  
        fields = "__all__"


class ClassUpdateForm(ModelForm):
    student = ChoiceField(
        widget=Select(        
            attrs={
                "class": "form-control",
                "id": "selectStudentUpdate"
            }
        )
    )

    course = ChoiceField(
        widget=Select(
            attrs={
                "class": "form-control",
                "id": "selectCourseUpdate"
            }
        )
    )
    
    startDate = DateField(
        widget=DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "id": "inputStartDateUpdate"
            }
        )
    )

    endDate = DateField(
        widget=DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "id": "inputEndDateUpdate"
            }
        )
    )

    state = ChoiceField(
        choices=STATUS_CHOICES,
        widget=Select(        
            attrs={
                "class": "form-control",
                "id": "selectStateUpdate"
            }
        )
    )

    class Meta:
        model = Course_Student  
        fields = "__all__"
