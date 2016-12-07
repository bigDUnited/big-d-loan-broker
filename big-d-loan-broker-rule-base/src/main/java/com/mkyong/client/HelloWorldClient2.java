package com.mkyong.client;

import testingwsimport.com.mkyong.ws.HelloWorldImplService;
import testingwsimport.com.mkyong.ws.HelloWorld;

public class HelloWorldClient2 {

    public static void main(String[] args) {

        HelloWorldImplService helloService = new HelloWorldImplService();
        HelloWorld hello = helloService.getHelloWorldImplPort();

        System.out.println(hello.getHelloWorldAsString("Secondary Client"));

    }

}
