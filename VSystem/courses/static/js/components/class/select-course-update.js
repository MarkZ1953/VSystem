export function updateSelectCourseOptions() {
    $.ajax({
        url: '/courses/get-courses/',
        method: 'GET',
        success: function(response) {
            const selectCourseClassAdd = document.getElementById('selectCourseAdd');
            const selectCourseClassUpdate = document.getElementById('selectCourseUpdate');
            
            // Limpia las opciones actuales de ambos selects
            selectCourseClassAdd.innerHTML = ''; 
            selectCourseClassUpdate.innerHTML = ''; 

            // Agrega cada nueva opción recibida a ambos selects
            response.courses.forEach(course => {
                const optionElementAdd = document.createElement('option');
                optionElementAdd.value = course.pk;
                optionElementAdd.textContent = `${course.fields.name}`;
                selectCourseClassAdd.appendChild(optionElementAdd);

                const optionElementUpdate = document.createElement('option');
                optionElementUpdate.value = course.pk;
                optionElementUpdate.textContent = `${course.fields.name}`;
                selectCourseClassUpdate.appendChild(optionElementUpdate);
            });
        }
    });
}
