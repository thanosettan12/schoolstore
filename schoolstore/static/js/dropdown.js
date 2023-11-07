// Sample data for sub-courses by department
        const subCourses = {
            computer_science: ["Algorithms", "Software Engineering", "Artificial Intelligence", "Database Management", "Web Development"],
            history: ["American History", "World History", "Ancient History", "European History", "History of Science"],
            economics: ["Microeconomics", "Macroeconomics", "International Economics", "Economic Development", "Game Theory"],
            art: ["Painting", "Sculpture", "Art History", "Graphic Design", "Photography"],
            mathematics: ["Calculus", "Linear Algebra", "Probability and Statistics", "Number Theory", "Differential Equations"],
            // Add data for other departments here
        };

        const departmentDropdown = document.getElementById('department');
        const subCourseDropdown = document.getElementById('subcourse');

        departmentDropdown.addEventListener('change', function() {
            const selectedDepartment = departmentDropdown.value;
            subCourseDropdown.innerHTML = ''; // Clear the sub-course dropdown

            if (selectedDepartment) {
                subCourses[selectedDepartment].forEach(subCourse => {
                    const option = document.createElement('option');
                    option.value = subCourse;
                    option.text = subCourse;
                    subCourseDropdown.appendChild(option);
                });
                subCourseDropdown.disabled = false; // Enable the sub-course dropdown
            } else {
                subCourseDropdown.disabled = true; // Disable the sub-course dropdown if no department is selected
            }
        });


