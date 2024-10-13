document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("teachersTable").addEventListener("click", function(event) {
        
        // Busca el botón de detalle más cercano
        const detailButton = event.target.closest(".btnDetail");
        
        // Verifica si se encontró un botón de detalle
        if (detailButton) {
            event.preventDefault();
            const teacherId = detailButton.getAttribute("data-id");
    
            $.ajax({
                url: `detail-teacher/${teacherId}/`,
                method: "GET",
                success: function(response) {
                    if (response.success) {
                        // Rellena los campos del formulario con la información del estudiante
                        document.getElementById("inputFirstNameDetail").value = response.teacher.fields.firstName;
                        document.getElementById("inputLastNameDetail").value = response.teacher.fields.lastName;
                        document.getElementById("inputDocumentDetail").value = response.teacher.fields.document;
                        document.getElementById("inputPhoneNumberDetail").value = response.teacher.fields.phoneNumber;
                        document.getElementById("inputBirthDateDetail").value = response.teacher.fields.birthDate;
                        document.getElementById("inputEmailDetail").value = response.teacher.fields.email;
                    }
                }
            });
        }
    });
})