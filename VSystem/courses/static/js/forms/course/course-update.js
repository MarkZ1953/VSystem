import { showToast } from "../../toast.js"
import { alertController } from "../../alert.js"
import { updateCourseTable } from "../../components/course/course-table.js"
import { getCookie } from "../../cookie.js"


document.addEventListener("DOMContentLoaded", function() {
    const courseUpdateForm = document.getElementById("courseUpdateForm")
    let courseId;
    
    document.getElementById("coursesTable").addEventListener("click", function(event) {
        const btnUpdate = event.target.closest(".btnUpdate");
    
        if (btnUpdate) {
            event.preventDefault();
            courseId = btnUpdate.getAttribute("data-id");
    
            $.ajax({
                url: `update-course/${courseId}/`,
                method: "GET",
                success: function(response) {
                    document.getElementById("inputNameUpdate").value = response.course.fields.name;    
                    document.getElementById("inputMaxCapacityUpdate").value = response.course.fields.maxCapacity;
                    document.getElementById("selectTeacherUpdate").value = response.course.fields.teacher;
                }
            });
        }
    });
    
    courseUpdateForm.addEventListener("submit", function(event) {
        event.preventDefault()
        const formData = new FormData(courseUpdateForm)
    
        $.ajax({
            url: `update-course/${courseId}/`,
            method: "POST",
            data: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            processData: false,
            contentType: false,
            success: function(response) {
                console.log("Hola mundo")
                if (response.success) {
                    var myModalElement = document.getElementById('updateForm')
                    var modal = bootstrap.Modal.getInstance(myModalElement)
                    modal.hide()
                    updateCourseTable()
                    showToast("coursesToast", response.message)
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
