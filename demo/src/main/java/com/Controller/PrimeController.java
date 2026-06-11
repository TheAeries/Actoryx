package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PrimeController {

    @GetMapping("/prime")
    public String checkPrime(@RequestParam int number) {

        if (number <= 1) {
            return number + " is not a Prime Number";
        }

        boolean isPrime = true;

        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            return number + " is a Prime Number";
        } else {
            return number + " is not a Prime Number";
        }
    }
}