import { showToast } from "../../toast.js"
import { alertController } from "../../alert.js"
import { updateCourseTable } from "../../components/course/course-table.js"
import { getCookie } from "../../cookie.js"


document.addEventListener("DOMContentLoaded", function() {
    const courseAddForm = document.getElementById("courseAddForm")

    courseAddForm.addEventListener("submit", function(event) {
        event.preventDefault()
        const formData = new FormData(courseAddForm)

        $.ajax({
            url: `add-course/`,
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
                    updateCourseTable()
                    showToast("classesToast", response.message)
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
