const API_BASE = "http://127.0.0.1:8000";

window.onload = () => {
    loadColleges();
};


/* ---------------------------
   Load Colleges
--------------------------- */

async function loadColleges() {

    try {

        const response =
            await fetch(
                `${API_BASE}/colleges`
            );

        const colleges =
            await response.json();

        const select =
            document.getElementById(
                "collegeSelect"
            );

        colleges.forEach(college => {

            const option =
                document.createElement(
                    "option"
                );

            option.value =
                college.name;

            option.textContent =
                college.name;

            select.appendChild(option);

        });

    }
    catch (error) {

        console.error(error);

        alert(
            "Unable to load colleges"
        );

    }

}


/* ---------------------------
   Load Departments
--------------------------- */

async function loadDepartments() {

    const collegeName =
        document.getElementById(
            "collegeSelect"
        ).value;

    if (!collegeName) {

        alert(
            "Please select a college"
        );

        return;
    }

    try {

        const response =
            await fetch(
                `${API_BASE}/college/${encodeURIComponent(collegeName)}`
            );

        const data =
            await response.json();

        const deptDiv =
            document.getElementById(
                "departments"
            );

        deptDiv.innerHTML = "";

        document.getElementById(
            "students"
        ).innerHTML = "";

        data.departments.forEach(
            dept => {

                const btn =
                    document.createElement(
                        "button"
                    );

                btn.className =
                    "department-btn";

                btn.innerHTML =
                    `
                    <strong>${dept.department_name}</strong><br>
                    HOD: ${dept.hod}<br>
                    Intake: ${dept.intake}
                    `;

                btn.onclick = () =>
                    loadCollegeDepartmentStudents(
                        collegeName,
                        dept.department_name
                    );

                deptDiv.appendChild(
                    btn
                );

            }
        );

    }
    catch (error) {

        console.error(error);

        alert(
            "Unable to load departments"
        );

    }

}


/* ---------------------------
   Load Students
   Selected College +
   Selected Department
--------------------------- */

async function loadCollegeDepartmentStudents(
    collegeName,
    departmentName
) {

    try {

        const response =
            await fetch(
                `${API_BASE}/college/${encodeURIComponent(collegeName)}/${encodeURIComponent(departmentName)}`
            );

        const data =
            await response.json();

        const studentDiv =
            document.getElementById(
                "students"
            );

        studentDiv.innerHTML = "";

        const title =
            document.createElement(
                "h3"
            );

        title.innerText =
            `${collegeName} - ${departmentName}`;

        studentDiv.appendChild(
            title
        );

        data.department.students.forEach(
            student => {

                const card =
                    document.createElement(
                        "div"
                    );

                card.className =
                    "student-card";

                card.innerHTML =
                    `
                    <strong>${student.name}</strong><br>
                    Roll No: ${student.roll_no}<br>
                    Year: ${student.year}<br>
                    CGPA: ${student.cgpa}
                    `;

                studentDiv.appendChild(
                    card
                );

            }
        );

    }
    catch (error) {

        console.error(error);

        alert(
            "Unable to load students"
        );

    }

}