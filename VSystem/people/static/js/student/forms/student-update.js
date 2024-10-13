import { showToast } from "../../toast.js"
import { alertController } from "../../alert.js"
import { updateStudentTable } from "../components/student-table.js"


const studentUpdateForm = document.getElementById("studentUpdateForm")
let studentId;

document.getElementById("students-table").addEventListener("click", function(event) {
    const btnUpdate = event.target.closest(".btnUpdate");

    if (btnUpdate) {
        event.preventDefault();
        studentId = btnUpdate.getAttribute("data-id");

        $.ajax({
            url: `detail-student/${studentId}/`,
            method: "GET",
            success: function(response) {
                document.getElementById("inputFirstNameUpdate").value = response.student.fields.firstName;    
                document.getElementById("inputLastNameUpdate").value = response.student.fields.lastName;
                document.getElementById("inputDocumentUpdate").value = response.student.fields.document;
                document.getElementById("inputPhoneNumberUpdate").value = response.student.fields.phoneNumber;
                document.getElementById("inputBirthDateUpdate").value = response.student.fields.birthDate;
                document.getElementById("inputEmailUpdate").value = response.student.fields.email;
            }
        });
    }
});

studentUpdateForm.addEventListener("submit", function(event) {
    event.preventDefault()
    const formData = new FormData(studentUpdateForm)

    $.ajax({
        url: `update-student/${studentId}/`,
        method: "POST",
        data: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        processData: false,
        contentType: false,
        success: function(response) {
            if (response.success) {
                var myModalElement = document.getElementById('updateForm')
                var modal = bootstrap.Modal.getInstance(myModalElement)
                modal.hide()
                updateStudentTable()    
                showToast("studentsToast", response.message)
            } else {
                alertController({
                    idAlert: "updateFormAlert",
                    message: response.message
                })
            }
        }, error: function(event) {
            alertController({
                idAlert: "updateFormAlert",
                message: "internalError"
            })
        }
    })
})

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Comprueba si este es el cookie que estamos buscando
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
