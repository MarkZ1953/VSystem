import { updateCourseTable } from "./components/course/course-table.js";
import { updateSelectOptions } from "./components/course/select-teacher-update.js"


document.addEventListener("DOMContentLoaded", function() {
    updateCourseTable()
    updateSelectOptions()
})