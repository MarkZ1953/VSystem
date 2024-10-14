import { showToast } from "../../toast.js"
import { updateClassTable } from "../../components/class/class-table.js"
import { getCookie } from "../../cookie.js"


document.addEventListener("DOMContentLoaded", function() {
    let classId;
    const btnDeleteAccept = document.getElementById("btnDeleteAccept")

    document.getElementById("classesTable").addEventListener("click", function(event) {
        const btnDelete = event.target.closest(".btnDelete");

        if (btnDelete) {
            event.preventDefault();
            classId = btnDelete.getAttribute("data-id");
            const classText = document.getElementById("classText")
            
            $.ajax({
                url: `detail-class/${classId}/`,
                method: "GET",
                success: function(response) {
                    classText.innerText = `Esta seguro/a que desea eliminar la relacion del estudiante ${response.class.fields.student} con el curso ${response.class.fields.course}?`
                }
            })
        }
    })

    btnDeleteAccept.addEventListener("click", function(event) {
        $.ajax({
            url: `delete-class/${classId}/`,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },  
            method: "POST",
            success: function(response) {
                if (response.success) {
                    var myModalElement = document.getElementById('deleteForm')
                    var modal = bootstrap.Modal.getInstance(myModalElement)
                    modal.hide()
                    updateClassTable()
                    showToast("classesToast", response.message, "danger")
                }
            }
        })
    })
})
