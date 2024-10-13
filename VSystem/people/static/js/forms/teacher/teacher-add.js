import { showToast } from "../../toast.js"
import { alertController } from "../../alert.js"
import { updateTeacherTable } from "../../components/teacher/teacher-table.js"
import { getCookie } from "../../cookie.js"


document.addEventListener("DOMContentLoaded", function() {
    const teacherAddForm = document.getElementById("teacherAddForm")

    teacherAddForm.addEventListener("submit", function(event) {
        event.preventDefault()
        const formData = new FormData(teacherAddForm)

        $.ajax({
            url: `add-teacher/`,
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
                    updateTeacherTable()    
                    showToast("teachersToast", response.message)
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
