package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ListSumController {

    @GetMapping("/listsum")
    public String calculateSum(@RequestParam String numbers) {

        String[] numArray = numbers.split(",");
        int sum = 0;

        for (String num : numArray) {
            sum += Integer.parseInt(num.trim());
        }

        return "Sum of elements = " + sum;
    }
}