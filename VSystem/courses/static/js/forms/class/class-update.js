import { showToast } from "../../toast.js"
import { alertController } from "../../alert.js"
import { updateClassTable } from "../../components/class/class-table.js"
import { getCookie } from "../../cookie.js"


document.addEventListener("DOMContentLoaded", function() {
    const classUpdateForm = document.getElementById("classUpdateForm")
    let classId;
    
    document.getElementById("classesTable").addEventListener("click", function(event) {
        const btnUpdate = event.target.closest(".btnUpdate");
    
        if (btnUpdate) {
            event.preventDefault();
            classId = btnUpdate.getAttribute("data-id");
    
            $.ajax({
                url: `update-class/${classId}/`,
                method: "GET",
                success: function(response) {
                    document.getElementById("selectStudentUpdate").value = response.class.fields.student;
                    document.getElementById("selectCourseUpdate").value = response.class.fields.course;
                    document.getElementById("inputStartDateUpdate").value = response.class.fields.startDate;
                    document.getElementById("inputEndDateUpdate").value = response.class.fields.endDate;
                    document.getElementById("selectStateUpdate").value = response.class.fields.state;
                }
            });
        }
    });
    
    classUpdateForm.addEventListener("submit", function(event) {
        event.preventDefault()
        const formData = new FormData(classUpdateForm)
    
        $.ajax({
            url: `update-class/${classId}/`,
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
                    updateClassTable()
                    showToast("classesToast", response.message)
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
