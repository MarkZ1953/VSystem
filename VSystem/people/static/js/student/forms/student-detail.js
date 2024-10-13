document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("students-table").addEventListener("click", function(event) {
        
        // Busca el botón de detalle más cercano
        const detailButton = event.target.closest(".btnDetail");
        
        // Verifica si se encontró un botón de detalle
        if (detailButton) {
            event.preventDefault();
            const studentId = detailButton.getAttribute("data-id");
    
            $.ajax({
                url: `detail-student/${studentId}/`,
                method: "GET",
                success: function(response) {
                    if (response.success) {
                        // Rellena los campos del formulario con la información del estudiante
                        document.getElementById("inputFirstNameDetail").value = response.student.fields.firstName;
                        document.getElementById("inputLastNameDetail").value = response.student.fields.lastName;
                        document.getElementById("inputDocumentDetail").value = response.student.fields.document;
                        document.getElementById("inputPhoneNumberDetail").value = response.student.fields.phoneNumber;
                        document.getElementById("inputBirthDateDetail").value = response.student.fields.birthDate;
                        document.getElementById("inputEmailDetail").value = response.student.fields.email;
                    }
                }
            });
        }
    });
})