package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class FactorialController {

    @GetMapping("/factorial")
    public String factorial(@RequestParam int number) {

        long fact = 1;

        for (int i = 1; i <= number; i++) {
            fact = fact * i;
        }

        return "Factorial of " + number + " = " + fact;
    }
}