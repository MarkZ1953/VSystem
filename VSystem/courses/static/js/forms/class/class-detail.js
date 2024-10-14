document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("classesTable").addEventListener("click", function(event) {
        
        const detailButton = event.target.closest(".btnDetail");
        
        if (detailButton) {
            event.preventDefault();
            const classId = detailButton.getAttribute("data-id");
    
            $.ajax({
                url: `detail-class/${classId}/`,
                method: "GET",
                success: function(response) {
                    if (response.success) {
                        document.getElementById("inputStudentDetail").value = response.class.fields.student;
                        document.getElementById("inputCourseDetail").value = response.class.fields.course;
                        document.getElementById("inputStartDateDetail").value = response.class.fields.startDate;
                        document.getElementById("inputEndDateDetail").value = response.class.fields.endDate;
                        document.getElementById("inputStateDetail").value = response.class.fields.state;
                    }
                }
            });
        }
    });
})