document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".btnDetail").forEach(button => {
        button.addEventListener("click", function(event) {
            event.preventDefault();
            const studentId = event.target.getAttribute("data-id"); // Obtener el ID directamente del evento
            console.log(studentId);

            $.ajax({
                url: `get-student/${studentId}/`,
                method: "GET",
                success: function(response) {
                    document.getElementById("inputFirstName").value = response.student.fields.firstName
                    document.getElementById("inputLastName").value = response.student.fields.lastName
                    document.getElementById("inputDocument").value = response.student.fields.document
                    document.getElementById("inputPhoneNumber").value = response.student.fields.phoneNumber
                    document.getElementById("inputBirthDate").value = response.student.fields.birthDate
                    document.getElementById("inputEmail").value = response.student.fields.email 
                }
            })
        })
    })
})
