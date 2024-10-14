import { showToast } from "../../toast.js"
import { alertController } from "../../alert.js"
import { updateClassTable } from "../../components/class/class-table.js"
import { getCookie } from "../../cookie.js"


document.addEventListener("DOMContentLoaded", function() {
    const courseAddForm = document.getElementById("classAddForm")

    courseAddForm.addEventListener("submit", function(event) {
        event.preventDefault()
        const formData = new FormData(courseAddForm)

        $.ajax({
            url: `add-class/`,
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
                    updateClassTable()
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
