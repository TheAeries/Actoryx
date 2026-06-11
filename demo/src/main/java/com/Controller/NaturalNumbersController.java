package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class NaturalNumbersController {

    @GetMapping("/natural")
    public String printNaturalNumbers() {

        String result = "";

        for (int i = 1; i <= 10; i++) {
            result += i + " ";
        }

        return result;
    }
}