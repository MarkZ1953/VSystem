import { showToast } from "../toast.js"


document.addEventListener("DOMContentLoaded", function() {
    const studentAddForm = document.getElementById("studentAddForm")
    studentAddForm.addEventListener("submit", function(event) {
        event.preventDefault()
        const formData = new FormData(studentAddForm)

        $.ajax({
            url: `add-student/`,
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
                    showToast("studentsToast", response.message)
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
