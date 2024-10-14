import { showToast } from "../toast.js"
import { alertController } from "../alert.js"
import { updateEnrollmentTable } from "../components/enrollment-table.js"
import { getCookie } from "../cookie.js"


document.addEventListener("DOMContentLoaded", function() {
    const enrollmentUpdateForm = document.getElementById("enrollmentUpdateForm")
    let enrollmentId;
    
    document.getElementById("enrollmentsTable").addEventListener("click", function(event) {
        const btnUpdate = event.target.closest(".btnUpdate");
    
        if (btnUpdate) {
            event.preventDefault();
            enrollmentId = btnUpdate.getAttribute("data-id");
    
            $.ajax({
                url: `update-enrollment/${enrollmentId}/`,
                method: "GET",
                success: function(response) {
                    document.getElementById("selectClassUpdate").value = response.enrollment.fields.studentCourse;
                    document.getElementById("inputCostUpdate").value = response.enrollment.fields.cost;
                    document.getElementById("inputStartDateUpdate").value = response.enrollment.fields.startDate;
                    document.getElementById("selectStateUpdate").value = response.enrollment.fields.state;
                }
            });
        }
    });
    
    enrollmentUpdateForm.addEventListener("submit", function(event) {
        event.preventDefault()
        const formData = new FormData(enrollmentUpdateForm)
    
        $.ajax({
            url: `update-enrollment/${enrollmentId}/`,
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
                    updateEnrollmentTable()
                    showToast("enrollmentsToast", response.message)
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
