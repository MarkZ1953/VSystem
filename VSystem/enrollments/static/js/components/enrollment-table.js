export function updateEnrollmentTable() {
    let content = ``;
    let row = 1

    $.ajax({
        url: "get-enrollments/",
        type: "GET",   
        success: function(response) {
            response.enrollments.forEach(enrollment =>  {
                content += `
                    <tr>
                        <td class="align-middle text-center">${row}</td>
                        <td class="align-middle text-center">${enrollment.fields.studentCourse}</td>  
                        <td class="align-middle text-center">${enrollment.fields.startDate}</td>
                        <td class="align-middle text-center">${enrollment.fields.cost}</td>
                        <td class="align-middle text-center">${enrollment.fields.state}</td>
                        <td class="align-middle text-center">
                            <a class="btn btn-secondary py-1 mb-1 mt-1 btnDetail" data-bs-toggle="modal" data-bs-target="#detailForm" data-id="${enrollment.pk}"><i class="bi bi-info-square" style="font-size: 18px;"></i></a>
                            <a class="btn btn-primary py-1 btnUpdate" data-bs-toggle="modal" data-bs-target="#updateForm" data-id="${enrollment.pk}"><i class="bi bi-pencil-square" style="font-size: 18px;"></i></a>
                            <a class="btn btn-danger py-1 btnDelete" data-bs-toggle="modal" data-bs-target="#deleteForm" data-id="${enrollment.pk}"><i class="bi bi-dash-square" style="font-size: 18px;"></i></a>
                        </td>
                    </tr>
                `
                row += 1
            })
            document.getElementById("enrollmentsTableBody").innerHTML = content
        }
    })
}
