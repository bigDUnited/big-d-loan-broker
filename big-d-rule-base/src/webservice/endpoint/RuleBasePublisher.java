package webservice.endpoint;

import javax.xml.ws.Endpoint;
import webservice.soap.RuleBaseImplementation;

//Endpoint publisher
public class RuleBasePublisher {

    /*
     * Can be accessed via "http://localhost:9999/ws/hello?wsdl"
     * Tutorial : http://www.mkyong.com/webservices/jax-ws/jax-ws-hello-world-example/
     * Export command : wsimport -keep http://localhost:9999/ws/rule-base?wsdl
     */
    public static void main(String[] args) {
        Endpoint.publish("http://localhost:9999/ws/rule-base?wsdl", new RuleBaseImplementation());
    }

}
