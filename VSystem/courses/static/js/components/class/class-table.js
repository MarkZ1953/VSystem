export function updateClassTable() {
    let content = ``;
    let row = 1

    $.ajax({
        url: "get-classes/",
        type: "GET",   
        success: function(response) {
            response.coursesStudents.forEach(courseStudent =>  {
                content += `
                    <tr>
                        <td class="align-middle text-center">${row}</td>
                        <td class="align-middle text-center">${courseStudent.fields.course}</td>  
                        <td class="align-middle text-center">${courseStudent.fields.student}</td>
                        <td class="align-middle text-center">${courseStudent.fields.startDate}</td>
                        <td class="align-middle text-center">${courseStudent.fields.endDate}</td>
                        <td class="align-middle text-center">${courseStudent.fields.state}</td>
                        <td class="align-middle text-center">
                            <a class="btn btn-secondary py-1 mb-1 mt-1 btnDetail" data-bs-toggle="modal" data-bs-target="#detailForm" data-id="${courseStudent.pk}"><i class="bi bi-info-square" style="font-size: 18px;"></i></a>
                            <a class="btn btn-primary py-1 btnUpdate" data-bs-toggle="modal" data-bs-target="#updateForm" data-id="${courseStudent.pk}"><i class="bi bi-pencil-square" style="font-size: 18px;"></i></a>
                            <a class="btn btn-danger py-1 btnDelete" data-bs-toggle="modal" data-bs-target="#deleteForm" data-id="${courseStudent.pk}"><i class="bi bi-dash-square" style="font-size: 18px;"></i></a>
                        </td>
                    </tr>
                `
                row += 1
            })
            document.getElementById("classesTableBody").innerHTML = content
        }
    })
}
