package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GradeController {

    @GetMapping("/grade")
    public String calculateGrade(
            @RequestParam String name,
            @RequestParam int maths,
            @RequestParam int physics,
            @RequestParam int chemistry) {

        int total = maths + physics + chemistry;
        String grade;

        if (total >= 270) {
            grade = "A";
        } else if (total >= 240) {
            grade = "B";
        } else if (total >= 180) {
            grade = "C";
        } else {
            grade = "D";
        }

        return "Student Name: " + name +
               ", Total Marks: " + total +
               ", Grade: " + grade;
    }
}