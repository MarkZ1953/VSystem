export function updateSelectOptions() {
    $.ajax({
        url: '/teachers/get-teachers/', // Ruta para obtener las opciones actualizadas
        method: 'GET',
        success: function(response) {
            const selectTeacherCourseAdd = document.getElementById('selectTeacherAdd');
            const selectTeacherCourseUpdate = document.getElementById('selectTeacherUpdate');
            
            // Limpia las opciones actuales
            selectTeacherCourseAdd.innerHTML = ''; 
            selectTeacherCourseUpdate.innerHTML = ''; 

            // Agrega cada nueva opción recibida a ambos selects
            response.teachers.forEach(teacher => {
                const optionElementAdd = document.createElement('option');
                optionElementAdd.value = teacher.pk;
                optionElementAdd.textContent = `${teacher.fields.firstName} ${teacher.fields.lastName}`;
                selectTeacherCourseAdd.appendChild(optionElementAdd);
                
                const optionElementUpdate = document.createElement('option');
                optionElementUpdate.value = teacher.pk;
                optionElementUpdate.textContent = `${teacher.fields.firstName} ${teacher.fields.lastName}`;
                selectTeacherCourseUpdate.appendChild(optionElementUpdate);
            });
        }
    });
}
