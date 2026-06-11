package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PositiveNegativeController {

    @GetMapping("/checknumber")
    public String checkNumber(@RequestParam double number) {

        if (number > 0) {
            return number + " is a Positive Number";
        } else if (number < 0) {
            return number + " is a Negative Number";
        } else {
            return "The number is Zero";
        }
    }
}