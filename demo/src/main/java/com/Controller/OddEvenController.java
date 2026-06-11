package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class OddEvenController {

    @GetMapping("/oddeven")
    public String checkOddEven(@RequestParam int number) {
        return (number % 2 == 0)
                ? number + " is Even"
                : number + " is Odd";
    }
}