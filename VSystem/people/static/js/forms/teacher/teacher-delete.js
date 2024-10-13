import { showToast } from "../../toast.js"
import { updateTeacherTable } from "../../components/teacher/teacher-table.js"
import { getCookie } from "../../cookie.js"


document.addEventListener("DOMContentLoaded", function() {
    let teacherId;
    const btnDeleteAccept = document.getElementById("btnDeleteAccept")

    document.getElementById("teachersTable").addEventListener("click", function(event) {
        const btnDelete = event.target.closest(".btnDelete");

        if (btnDelete) {
            event.preventDefault();
            teacherId = btnDelete.getAttribute("data-id");
            const teacherText = document.getElementById("teacherText")
            
            $.ajax({
                url: `detail-teacher/${teacherId}/`,
                method: "GET",
                success: function(response) {
                    teacherText.innerText = `Esta seguro/a que desea eliminar a el/la docente ${response.teacher.fields.firstName} ${response.teacher.fields.lastName}`
                }
            })
        }
    })

    btnDeleteAccept.addEventListener("click", function(event) {
        $.ajax({
            url: `delete-teacher/${teacherId}/`,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },  
            method: "POST",
            success: function(response) {
                if (response.success) {
                    var myModalElement = document.getElementById('deleteForm')
                    var modal = bootstrap.Modal.getInstance(myModalElement)
                    modal.hide()
                    updateTeacherTable()
                    showToast("teachersToast", response.message, "danger")
                }
            }
        })
    })
})
