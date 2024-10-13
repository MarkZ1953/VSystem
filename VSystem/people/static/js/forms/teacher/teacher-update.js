import { showToast } from "../../toast.js"
import { alertController } from "../../alert.js"
import { updateTeacherTable } from "../../components/teacher/teacher-table.js"
import { getCookie } from "../../cookie.js"


document.addEventListener("DOMContentLoaded", function() {
    const teacherUpdateForm = document.getElementById("teacherUpdateForm")
    let teacherId;
    
    document.getElementById("teachersTable").addEventListener("click", function(event) {
        const btnUpdate = event.target.closest(".btnUpdate");
    
        if (btnUpdate) {
            event.preventDefault();
            teacherId = btnUpdate.getAttribute("data-id");
    
            $.ajax({
                url: `detail-teacher/${teacherId}/`,
                method: "GET",
                success: function(response) {
                    document.getElementById("inputFirstNameUpdate").value = response.teacher.fields.firstName;    
                    document.getElementById("inputLastNameUpdate").value = response.teacher.fields.lastName;
                    document.getElementById("inputDocumentUpdate").value = response.teacher.fields.document;
                    document.getElementById("inputPhoneNumberUpdate").value = response.teacher.fields.phoneNumber;
                    document.getElementById("inputBirthDateUpdate").value = response.teacher.fields.birthDate;
                    document.getElementById("inputEmailUpdate").value = response.teacher.fields.email;
                }
            });
        }
    });
    
    teacherUpdateForm.addEventListener("submit", function(event) {
        event.preventDefault()
        const formData = new FormData(teacherUpdateForm)
    
        $.ajax({
            url: `update-teacher/${teacherId}/`,
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
                    updateTeacherTable()    
                    showToast("teachersToast", response.message)
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
})
