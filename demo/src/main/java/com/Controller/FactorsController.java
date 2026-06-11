package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class FactorsController {

    @GetMapping("/factors")
    public String findFactors(@RequestParam int number) {

        StringBuilder factors = new StringBuilder();

        for (int i = 1; i <= number; i++) {
            if (number % i == 0) {
                factors.append(i).append(" ");
            }
        }

        return "Factors of " + number + " are: " + factors;
    }
}
