from django.forms import ModelForm, CharField, TextInput, ChoiceField, Select, DateField, DateInput
from .models import Enrollment
from .choices import STATUS_CHOICES


class EnrollmentAddForm(ModelForm):
    studentCourse = ChoiceField(
        widget=Select(        
            attrs={
                "class": "form-control",
                "id": "selectClassAdd"
            }
        )
    )

    cost = CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "type": "number",
                "id": "inputCostAdd",
                "min": "0",
                "step": "1"
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
        model = Enrollment
        fields = "__all__"


class EnrollmentUpdateForm(ModelForm):
    studentCourse = ChoiceField(
        widget=Select(        
            attrs={
                "class": "form-control",
                "id": "selectClassUpdate"
            }
        )
    )

    cost = CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "type": "number",
                "id": "inputCostUpdate",
                "min": "0",
                "step": "1"
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
        model = Enrollment
        fields = "__all__"


class EnrollmentDetailForm(ModelForm):
    studentCourse = CharField(
        widget=TextInput(        
            attrs={
                "class": "form-control",
                "id": "inputClassDetail",
                "readonly": True,
                "disabled": True
            }
        )
    )

    cost = CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "type": "number",
                "id": "inputCostDetail",
                "min": "0",
                "step": "1",
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

    state = CharField(
        widget=TextInput(        
            attrs={
                "class": "form-control",
                "id": "inputStatetDetail",
                "readonly": True,
                "disabled": True
            }
        )
    )

    class Meta:
        model = Enrollment
        fields = "__all__"
