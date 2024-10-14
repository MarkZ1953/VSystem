import { updateClassTable } from "./components/class/class-table.js";
import { updateSelectCourseOptions } from "./components/class/select-course-update.js";
import { updateSelectStudentOptions } from "./components/class/select-student-update.js";


document.addEventListener("DOMContentLoaded", function() {
    updateClassTable()
    updateSelectCourseOptions()
    updateSelectStudentOptions()
})