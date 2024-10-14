document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("coursesTable").addEventListener("click", function(event) {
        
        const detailButton = event.target.closest(".btnDetail");
        
        if (detailButton) {
            event.preventDefault();
            const courseId = detailButton.getAttribute("data-id");
    
            $.ajax({
                url: `detail-course/${courseId}/`,
                method: "GET",
                success: function(response) {
                    if (response.success) {
                        document.getElementById("inputNameDetail").value = response.course.fields.name;
                        document.getElementById("inputTeacherDetail").value = response.course.fields.teacher;
                        document.getElementById("inputMaxCapacityDetail").value = response.course.fields.maxCapacity;
                    }
                }
            });
        }
    });
})