package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ArithmeticController {

    @GetMapping("/calculate")
    public String calculate(
            @RequestParam double num1,
            @RequestParam double num2) {

        double addition = num1 + num2;
        double subtraction = num1 - num2;
        double multiplication = num1 * num2;

        String result = "Addition = " + addition +
                        ", Subtraction = " + subtraction +
                        ", Multiplication = " + multiplication;

        if (num2 != 0) {
            double division = num1 / num2;
            result += ", Division = " + division;
        } else {
            result += ", Division not possible (cannot divide by zero)";
        }

        return result;
    }
}