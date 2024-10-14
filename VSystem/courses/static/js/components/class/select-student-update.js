export function updateSelectStudentOptions() {
    $.ajax({
        url: '/students/get-students/',
        method: 'GET',
        success: function(response) {
            const selectStudentClassAdd = document.getElementById('selectStudentAdd');
            const selectStudentClassUpdate = document.getElementById('selectStudentUpdate');
            
            // Limpia las opciones actuales de ambos selects
            selectStudentClassAdd.innerHTML = ''; 
            selectStudentClassUpdate.innerHTML = ''; 

            // Agrega cada nueva opción recibida a ambos selects
            response.students.forEach(student => {
                const optionElementAdd = document.createElement('option');
                optionElementAdd.value = student.pk;
                optionElementAdd.textContent = `${student.fields.firstName} ${student.fields.lastName}`;
                selectStudentClassAdd.appendChild(optionElementAdd);

                const optionElementUpdate = document.createElement('option');
                optionElementUpdate.value = student.pk;
                optionElementUpdate.textContent = `${student.fields.firstName} ${student.fields.lastName}`;
                selectStudentClassUpdate.appendChild(optionElementUpdate);
            });
        }
    });
}
