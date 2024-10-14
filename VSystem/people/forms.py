from django.forms import CharField, TextInput, Form, EmailField, EmailInput, DateField, DateInput, ModelForm
from .models import Person


class StudentDetailForm(Form):
    firstName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "name": "inputFirstNameDetail",
            "id": "inputFirstNameDetail",
            "readonly": True,
            "disabled": True
        }
    ))

    lastName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "name": "inputLastNameDetail",
            "id": "inputLastNameDetail",
            "readonly": "True",
            "disabled": "True"
        }
    ))

    document = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "name": "inputDocumentDetail",
            "id": "inputDocumentDetail",
            "readonly": "True",
            "disabled": "True"
        }
    ))
    
    phoneNumber = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "name": "inputPhoneNumberDetail",
            "id": "inputPhoneNumberDetail",
            "readonly": "True",
            "disabled": "True"
        }
    ))

    email = EmailField(widget=EmailInput(
        attrs={
            "class": "form-control",
            "maxlength": "128",
            "name": "inputEmailDetail",
            "id": "inputEmailDetail",
            "readonly": "True",
            "disabled": "True"
        }
    ))

    birthDate = DateField(widget=DateInput(
        attrs={
            "class": "form-control",
            "type": "date",
            "name": "inputBirthDateDetail",
            "id": "inputBirthDateDetail",
            "readonly": "True",
            "disabled": "True"
        }
    ))


class StudentAddForm(Form):
    firstName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "id": "inputFirstNameAdd"
        }
    ))

    lastName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "id": "inputLastNameAdd"
        }
    ))

    document = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "id": "inputDocumentAdd"
        }
    ))
    
    phoneNumber = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "id": "inputPhoneNumberAdd"
        }
    ))

    email = EmailField(widget=EmailInput(
        attrs={
            "class": "form-control",
            "maxlength": "128",
            "id": "inputEmailAdd"
        }
    ))

    birthDate = DateField(widget=DateInput(
        attrs={
            "class": "form-control",
            "type": "date",
            "id": "inputBirthDateAdd"
        }
    ))
    

class StudentUpdateForm(ModelForm):
    firstName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "id": "inputFirstNameUpdate"
        }
    ))

    lastName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "id": "inputLastNameUpdate"
        }
    ))

    document = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "id": "inputDocumentUpdate"
        }
    ))
    
    phoneNumber = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "name": "inputPhoneNumber",
            "id": "inputPhoneNumberUpdate"
        }
    ))

    email = EmailField(widget=EmailInput(
        attrs={
            "class": "form-control",
            "maxlength": "128",
            "id": "inputEmailUpdate"
        }
    ))

    birthDate = DateField(widget=DateInput(
        attrs={
            "class": "form-control",
            "type": "date",
            "id": "inputBirthDateUpdate"
        }
    ))

    class Meta:
        model = Person
        fields = "__all__"


class TeacherDetailForm(Form):
    firstName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "id": "inputFirstNameDetail",
            "readonly": True,
            "disabled": True
        }
    ))

    lastName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "name": "inputLastNameDetail",
            "id": "inputLastNameDetail",
            "readonly": "True",
            "disabled": "True"
        }
    ))

    document = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "name": "inputDocumentDetail",
            "id": "inputDocumentDetail",
            "readonly": "True",
            "disabled": "True"
        }
    ))
    
    phoneNumber = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "name": "inputPhoneNumberDetail",
            "id": "inputPhoneNumberDetail",
            "readonly": "True",
            "disabled": "True"
        }
    ))

    email = EmailField(widget=EmailInput(
        attrs={
            "class": "form-control",
            "maxlength": "128",
            "name": "inputEmailDetail",
            "id": "inputEmailDetail",
            "readonly": "True",
            "disabled": "True"
        }
    ))

    birthDate = DateField(widget=DateInput(
        attrs={
            "class": "form-control",
            "type": "date",
            "name": "inputBirthDateDetail",
            "id": "inputBirthDateDetail",
            "readonly": "True",
            "disabled": "True"
        }
    ))


class TeacherAddForm(Form):
    firstName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "name": "inputFirstNameAdd",
            "id": "inputFirstNameAdd"
        }
    ))

    lastName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "name": "inputLastNameAdd",
            "id": "inputLastNameAdd"
        }
    ))

    document = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "name": "inputDocumentAdd",
            "id": "inputDocumentAdd"
        }
    ))
    
    phoneNumber = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "name": "inputPhoneNumberAdd",
            "id": "inputPhoneNumberAdd"
        }
    ))

    email = EmailField(widget=EmailInput(
        attrs={
            "class": "form-control",
            "maxlength": "128",
            "name": "inputEmailAdd",
            "id": "inputEmailAdd"
        }
    ))

    birthDate = DateField(widget=DateInput(
        attrs={
            "class": "form-control",
            "type": "date",
            "name": "inputBirthDateAdd",
            "id": "inputBirthDateAdd"
        }
    ))
    

class TeacherUpdateForm(ModelForm):
    firstName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "id": "inputFirstNameUpdate"
        }
    ))

    lastName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "id": "inputLastNameUpdate"
        }
    ))

    document = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "id": "inputDocumentUpdate"
        }
    ))
    
    phoneNumber = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "name": "inputPhoneNumber",
            "id": "inputPhoneNumberUpdate"
        }
    ))

    email = EmailField(widget=EmailInput(
        attrs={
            "class": "form-control",
            "maxlength": "128",
            "id": "inputEmailUpdate"
        }
    ))

    birthDate = DateField(widget=DateInput(
        attrs={
            "class": "form-control",
            "type": "date",
            "id": "inputBirthDateUpdate"
        }
    ))

    class Meta:
        model = Person
        fields = "__all__"