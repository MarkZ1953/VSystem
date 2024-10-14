export function updateSelectStudentCourseOptions() {
    $.ajax({
        url: '/classes/get-classes/',
        method: 'GET',
        success: function(response) {
            const selectClassClassAdd = document.getElementById('selectClassAdd');
            const selectClassUpdate = document.getElementById('selectClassUpdate');
            
            // Limpia las opciones actuales de ambos selects
            selectClassClassAdd.innerHTML = ''; 
            selectClassUpdate.innerHTML = ''; 

            // Agrega cada nueva opción recibida a ambos selects
            response.coursesStudents.forEach(courseStudent => {
                const optionElementAdd = document.createElement('option');
                optionElementAdd.value = courseStudent.pk;
                optionElementAdd.textContent = `${courseStudent.fields.course} | ${courseStudent.fields.student}`;
                selectClassClassAdd.appendChild(optionElementAdd);

                const optionElementUpdate = document.createElement('option');
                optionElementUpdate.value = courseStudent.pk;
                optionElementUpdate.textContent = `${courseStudent.fields.course} | ${courseStudent.fields.student}`;
                selectClassUpdate.appendChild(optionElementUpdate);
            });
        }
    });
}
