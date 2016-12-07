package com.mkyong.client;

import testingwsimport.webservice.soap.RuleBaseImplementationService;
import testingwsimport.webservice.soap.RuleBaseInterface;

public class HelloWorldClient2 {

    public static void main(String[] args) {

        RuleBaseImplementationService helloService = new RuleBaseImplementationService();
        RuleBaseInterface rbi = helloService.getRuleBaseImplementationPort();

        System.out.println(rbi.getHelloWorldAsString("Secondary Client"));
    }

}
