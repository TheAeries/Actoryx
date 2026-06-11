package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ComparisonController {

    @GetMapping("/compare")
    public String compareNumbers(
            @RequestParam double num1,
            @RequestParam double num2) {

        if (num1 > num2) {
            return "First number (" + num1 + ") is greater";
        } else if (num2 > num1) {
            return "Second number (" + num2 + ") is greater";
        } else {
            return "Both numbers are equal";
        }
    }
}