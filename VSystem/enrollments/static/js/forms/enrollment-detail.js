document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("enrollmentsTable").addEventListener("click", function(event) {
        
        const detailButton = event.target.closest(".btnDetail");
        
        if (detailButton) {
            event.preventDefault();
            const classId = detailButton.getAttribute("data-id");
    
            $.ajax({
                url: `detail-enrollment/${classId}/`,
                method: "GET",
                success: function(response) {
                    if (response.success) {
                        document.getElementById("inputClassDetail").value = response.enrollment.fields.studentCourse;
                        document.getElementById("inputCostDetail").value = response.enrollment.fields.cost;
                        document.getElementById("inputStartDateDetail").value = response.enrollment.fields.startDate;
                        document.getElementById("inputStatetDetail").value = response.enrollment.fields.state;
                    }
                }
            });
        }
    });
})