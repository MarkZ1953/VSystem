import { showToast } from "../toast.js"
import { alertController } from "../alert.js"
import { updateEnrollmentTable } from "../components/enrollment-table.js"
import { getCookie } from "../cookie.js"


document.addEventListener("DOMContentLoaded", function() {
    const enrollmentAddForm = document.getElementById("enrollmentAddForm")

    enrollmentAddForm.addEventListener("submit", function(event) {
        event.preventDefault()
        const formData = new FormData(enrollmentAddForm)

        $.ajax({
            url: `add-enrollment/`,
            method: "POST",
            data: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            processData: false,
            contentType: false,
            success: function(response) {
                if (response.success) {
                    var myModalElement = document.getElementById('addForm')
                    var modal = bootstrap.Modal.getInstance(myModalElement)
                    modal.hide()
                    updateEnrollmentTable()
                    showToast("enrollmentsToast", response.message)
                } else {
                    alertController({
                        idAlert: "addFormAlert",
                        message: response.message
                    })
                }
            }, error: function(event) {
                alertController({
                    idAlert: "addFormAlert",
                    message: "internalError"
                })
            }
        })
    })
})
