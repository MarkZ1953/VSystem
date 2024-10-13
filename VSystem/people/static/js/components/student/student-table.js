export function updateStudentTable() {
    let content = ``;
    let row = 1

    $.ajax({
        url: "get-students/",
        type: "GET",   
        success: function(response) {
            response.students.forEach(student =>  {
                if (student.fields.isActive) {
                    content += `
                        <tr>
                            <td class="align-middle text-center">${row}</td>
                            <td class="align-middle text-center">${student.fields.document}</td>
                            <td class="align-middle text-center">${student.fields.firstName}</td>
                            <td class="align-middle text-center">${student.fields.lastName}</td>
                            <td class="align-middle text-center">${student.fields.phoneNumber}</td>
                            <td class="align-middle text-center">${student.fields.email}</td> 
                            <td class="align-middle text-center">${student.fields.birthDate}</td>
                            <td class="align-middle text-center">
                                <a class="btn btn-secondary py-1 mb-1 mt-1 btnDetail" data-bs-toggle="modal" data-bs-target="#detailForm" data-id="${student.pk}"><i class="bi bi-info-square" style="font-size: 18px;"></i></a>
                                <a class="btn btn-primary py-1 btnUpdate" data-bs-toggle="modal" data-bs-target="#updateForm" data-id="${student.pk}"><i class="bi bi-pencil-square" style="font-size: 18px;"></i></a>
                                <a class="btn btn-danger py-1 btnDelete" data-bs-toggle="modal" data-bs-target="#deleteForm" data-id="${student.pk}"><i class="bi bi-dash-square" style="font-size: 18px;"></i></a>
                            </td>
                        </tr>
                    `
                    row += 1
                }
            })
            document.getElementById("studentsTableBody").innerHTML = content
        }
    })
}
