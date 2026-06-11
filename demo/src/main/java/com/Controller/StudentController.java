package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class StudentController {

    @GetMapping("/students")
    public String displayStudents() {

        return """
                Student Information

                Roll No: 101, Name: Anil, Age: 20, Marks: 85
                Roll No: 102, Name: Priya, Age: 19, Marks: 90
                Roll No: 103, Name: Rahul, Age: 21, Marks: 78
                Roll No: 104, Name: Sneha, Age: 20, Marks: 88
                Roll No: 105, Name: Kiran, Age: 19, Marks: 92
                Roll No: 106, Name: Divya, Age: 20, Marks: 81
                Roll No: 107, Name: Arun, Age: 21, Marks: 75
                Roll No: 108, Name: Pooja, Age: 19, Marks: 89
                Roll No: 109, Name: Ravi, Age: 20, Marks: 84
                Roll No: 110, Name: Neha, Age: 21, Marks: 91
                """;
    }
}