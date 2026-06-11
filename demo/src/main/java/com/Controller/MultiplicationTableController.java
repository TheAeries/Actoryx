package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MultiplicationTableController {

    @GetMapping("/table")
    public String multiplicationTable(@RequestParam int number) {

        StringBuilder table = new StringBuilder();

        for (int i = 1; i <= 10; i++) {
            table.append(number)
                 .append(" x ")
                 .append(i)
                 .append(" = ")
                 .append(number * i)
                 .append("<br>");
        }

        return table.toString();
    }
}