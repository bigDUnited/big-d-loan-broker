package webservice.endpoint;

import javax.xml.ws.Endpoint;
import webservice.soap.RuleBaseImplementation;

//Endpoint publisher
public class RuleBasePublisher {

    /*
     * Can be accessed via "http://localhost:9999/ws/hello?wsdl"
     */
    public static void main(String[] args) {
        Endpoint.publish("http://localhost:9999/ws/hello", new RuleBaseImplementation());
    }

}
