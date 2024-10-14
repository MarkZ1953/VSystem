export function updateCourseTable() {
    let content = ``;
    let row = 1

    $.ajax({
        url: "get-courses/",
        type: "GET",   
        success: function(response) {
            response.courses.forEach(course =>  {
                content += `
                    <tr>
                        <td class="align-middle text-center">${row}</td>
                        <td class="align-middle text-center">${course.fields.name}</td>
                        <td class="align-middle text-center">${course.fields.maxCapacity}</td>  
                        <td class="align-middle text-center">${course.fields.teacher}</td>
                        <td class="align-middle text-center">
                            <a class="btn btn-secondary py-1 mb-1 mt-1 btnDetail" data-bs-toggle="modal" data-bs-target="#detailForm" data-id="${course.pk}"><i class="bi bi-info-square" style="font-size: 18px;"></i></a>
                            <a class="btn btn-primary py-1 btnUpdate" data-bs-toggle="modal" data-bs-target="#updateForm" data-id="${course.pk}"><i class="bi bi-pencil-square" style="font-size: 18px;"></i></a>
                            <a class="btn btn-danger py-1 btnDelete" data-bs-toggle="modal" data-bs-target="#deleteForm" data-id="${course.pk}"><i class="bi bi-dash-square" style="font-size: 18px;"></i></a>
                        </td>
                    </tr>
                `
                row += 1
            })
            document.getElementById("coursesTableBody").innerHTML = content
        }
    })
}
