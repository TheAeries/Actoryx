package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SumOfDigitsController {

    @GetMapping("/sumdigits")
    public String sumOfDigits(@RequestParam int number) {

        int sum = 0;
        int temp = Math.abs(number);

        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }

        return "Sum of digits of " + number + " = " + sum;
    }
}