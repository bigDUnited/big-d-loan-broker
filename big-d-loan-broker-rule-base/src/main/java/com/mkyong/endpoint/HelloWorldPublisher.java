package com.mkyong.endpoint;

import javax.xml.ws.Endpoint;
import com.mkyong.ws.HelloWorldImpl;

//Endpoint publisher
public class HelloWorldPublisher {

    /*
     * Can be accessed via "http://localhost:9999/ws/hello?wsdl"
     */
    public static void main(String[] args) {
        Endpoint.publish("http://localhost:9999/ws/hello", new HelloWorldImpl());
    }

}
