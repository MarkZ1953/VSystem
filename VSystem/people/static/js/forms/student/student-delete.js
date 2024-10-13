import { showToast } from "../../toast.js"
import { updateStudentTable } from "../../components/student/student-table.js"


document.addEventListener("DOMContentLoaded", function() {
    let studentId;
    const btnDeleteAccept = document.getElementById("btnDeleteAccept")

    document.getElementById("studentsTable").addEventListener("click", function(event) {
        const btnDelete = event.target.closest(".btnDelete");

        if (btnDelete) {
            event.preventDefault();
            studentId = btnDelete.getAttribute("data-id");
            const studentText = document.getElementById("student-text")
            
            $.ajax({
                url: `detail-student/${studentId}/`,
                method: "GET",
                success: function(response) {
                    studentText.innerText = `Esta seguro/a que desea eliminar a el/la estudiante ${response.student.fields.firstName} ${response.student.fields.lastName}`
                }
            })
        }
    })

    btnDeleteAccept.addEventListener("click", function(event) {
        $.ajax({
            url: `delete-student/${studentId}/`,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },  
            method: "POST",
            success: function(response) {
                if (response.success) {
                    var myModalElement = document.getElementById('deleteForm')
                    var modal = bootstrap.Modal.getInstance(myModalElement)
                    modal.hide()
                    updateStudentTable()
                    showToast("studentsToast", response.message, "danger")
                }
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
})
