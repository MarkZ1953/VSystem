import { showToast } from "../toast.js"
import { updateEnrollmentTable } from "../components/enrollment-table.js"
import { getCookie } from "../cookie.js"


document.addEventListener("DOMContentLoaded", function() {
    let enrollmentId;
    const btnDeleteAccept = document.getElementById("btnDeleteAccept")

    document.getElementById("enrollmentsTable").addEventListener("click", function(event) {
        const btnDelete = event.target.closest(".btnDelete");

        if (btnDelete) {
            event.preventDefault();
            enrollmentId = btnDelete.getAttribute("data-id");
            const enrollmentText = document.getElementById("enrollmentText")
            
            $.ajax({
                url: `detail-enrollment/${enrollmentId}/`,
                method: "GET",
                success: function(response) {
                    enrollmentText.innerText = `Esta seguro/a que desea eliminar la matricula de ${response.enrollment.fields.studentCourse}?`
                }
            })
        }
    })

    btnDeleteAccept.addEventListener("click", function(event) {
        $.ajax({
            url: `delete-enrollment/${enrollmentId}/`,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },  
            method: "POST",
            success: function(response) {
                if (response.success) {
                    var myModalElement = document.getElementById('deleteForm')
                    var modal = bootstrap.Modal.getInstance(myModalElement)
                    modal.hide()
                    updateEnrollmentTable()
                    showToast("enrollmentsToast", response.message, "danger")
                }
            }
        })
    })
})
