package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class NNaturalNumbersController {

    @GetMapping("/naturaln")
    public String printNaturalNumbers(@RequestParam int n) {

        StringBuilder result = new StringBuilder();

        int i = 1;

        while (i <= n) {
            result.append(i).append(" ");
            i++;
        }

        return result.toString();
    }
}