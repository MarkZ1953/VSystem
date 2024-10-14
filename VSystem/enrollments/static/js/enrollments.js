import { updateEnrollmentTable } from "./components/enrollment-table.js";
import { updateSelectStudentCourseOptions } from "./components/select-student-course-update.js";
// import { updateSelectStudentOptions } from "./components/class/select-student-update.js";


document.addEventListener("DOMContentLoaded", function() {
    updateEnrollmentTable()
    updateSelectStudentCourseOptions()
})