export function updateTeacherTable() {
    let content = ``;
    let row = 1

    $.ajax({
        url: "get-teachers/",
        type: "GET",   
        success: function(response) {
            response.teachers.forEach(teacher =>  {
                if (teacher.fields.isActive) {
                    content += `
                        <tr>
                            <td class="align-middle text-center">${row}</td>
                            <td class="align-middle text-center">${teacher.fields.document}</td>
                            <td class="align-middle text-center">${teacher.fields.firstName}</td>
                            <td class="align-middle text-center">${teacher.fields.lastName}</td>
                            <td class="align-middle text-center">${teacher.fields.phoneNumber}</td>
                            <td class="align-middle text-center">${teacher.fields.email}</td> 
                            <td class="align-middle text-center">${teacher.fields.birthDate}</td>
                            <td class="align-middle text-center">
                                <a class="btn btn-secondary py-1 mb-1 mt-1 btnDetail" data-bs-toggle="modal" data-bs-target="#detailForm" data-id="${teacher.pk}"><i class="bi bi-info-square" style="font-size: 18px;"></i></a>
                                <a class="btn btn-primary py-1 btnUpdate" data-bs-toggle="modal" data-bs-target="#updateForm" data-id="${teacher.pk}"><i class="bi bi-pencil-square" style="font-size: 18px;"></i></a>
                                <a class="btn btn-danger py-1 btnDelete" data-bs-toggle="modal" data-bs-target="#deleteForm" data-id="${teacher.pk}"><i class="bi bi-dash-square" style="font-size: 18px;"></i></a>
                            </td>
                        </tr>
                    `
                    row += 1
                }
            })
            document.getElementById("teachersTableBody").innerHTML = content
        }
    })
}
