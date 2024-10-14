import { showToast } from "../../toast.js"
import { updateCourseTable } from "../../components/course/course-table.js"
import { getCookie } from "../../cookie.js"
import { updateSelectOptions } from "../../components/course/select-teacher-update.js"


document.addEventListener("DOMContentLoaded", function() {
    let courseId;
    const btnDeleteAccept = document.getElementById("btnDeleteAccept")

    document.getElementById("coursesTable").addEventListener("click", function(event) {
        const btnDelete = event.target.closest(".btnDelete");

        if (btnDelete) {
            event.preventDefault();
            courseId = btnDelete.getAttribute("data-id");
            const courseText = document.getElementById("courseText")
            
            $.ajax({
                url: `detail-course/${courseId}/`,
                method: "GET",
                success: function(response) {
                    courseText.innerText = `Esta seguro/a que desea eliminar a el curso de ${response.course.fields.name}`
                }
            })
        }
    })

    btnDeleteAccept.addEventListener("click", function(event) {
        $.ajax({
            url: `delete-course/${courseId}/`,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },  
            method: "POST",
            success: function(response) {
                if (response.success) {
                    var myModalElement = document.getElementById('deleteForm')
                    var modal = bootstrap.Modal.getInstance(myModalElement)
                    modal.hide()
                    updateCourseTable()
                    updateSelectOptions()
                    showToast("coursesToast", response.message, "danger")
                }
            }
        })
    })
})
