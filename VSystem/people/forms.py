from django.forms import CharField, TextInput, Form, EmailField, EmailInput, DateField, DateInput


class StudentDetailForm(Form):
    firstName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "name": "inputFirstName",
            "id": "inputFirstName",
            "readonly": True,
            "disabled": True
        }
    ))

    lastName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "name": "inputLastName",
            "id": "inputLastName",
            "readonly": "True",
            "disabled": "True"
        }
    ))

    document = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "name": "inputDocument",
            "id": "inputDocument",
            "readonly": "True",
            "disabled": "True"
        }
    ))
    
    phoneNumber = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "name": "inputPhoneNumber",
            "id": "inputPhoneNumber",
            "readonly": "True",
            "disabled": "True"
        }
    ))

    email = EmailField(widget=EmailInput(
        attrs={
            "class": "form-control",
            "maxlength": "128",
            "name": "inputEmail",
            "id": "inputEmail",
            "readonly": "True",
            "disabled": "True"
        }
    ))

    birthDate = DateField(widget=DateInput(
        attrs={
            "class": "form-control",
            "type": "date",
            "name": "inputBirthDate",
            "id": "inputBirthDate",
            "readonly": "True",
            "disabled": "True"
        }
    ))


class StudentAddForm(Form):
    firstName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "name": "inputFirstName",
            "id": "inputFirstName"
        }
    ))

    lastName = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "32",
            "name": "inputLastName",
            "id": "inputLastName"
        }
    ))

    document = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "name": "inputDocument",
            "id": "inputDocument"
        }
    ))
    
    phoneNumber = CharField(widget=TextInput(        
        attrs={
            "class": "form-control",
            "maxlength": "16",
            "name": "inputPhoneNumber",
            "id": "inputPhoneNumber"
        }
    ))

    email = EmailField(widget=EmailInput(
        attrs={
            "class": "form-control",
            "maxlength": "128",
            "name": "inputEmail",
            "id": "inputEmail"
        }
    ))

    birthDate = DateField(widget=DateInput(
        attrs={
            "class": "form-control",
            "type": "date",
            "name": "inputBirthDate",
            "id": "inputBirthDate"
        }
    ))


class FormTeacher(Form):
    pass