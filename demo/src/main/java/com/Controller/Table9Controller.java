package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Table9Controller {

    @GetMapping("/table9")
    public String printTable9() {

        StringBuilder result = new StringBuilder();

        for (int i = 1; i <= 10; i++) {
            result.append("9 x ")
                  .append(i)
                  .append(" = ")
                  .append(9 * i)
                  .append("<br>");
        }

        return result.toString();
    }
}