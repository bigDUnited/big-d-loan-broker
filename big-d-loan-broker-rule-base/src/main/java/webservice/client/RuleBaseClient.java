package webservice.client;

import java.net.URL;
import java.util.ArrayList;
import javax.xml.namespace.QName;
import javax.xml.ws.Service;
import webservice.logic.entity.Bank;
import webservice.soap.RuleBaseImplementation;
import webservice.soap.RuleBaseInterface;

public class RuleBaseClient {

    public static void main(String[] args) throws Exception {

        URL url = new URL("http://localhost:9999/ws/hello?wsdl");

        /* @args: 
         *  1st argument service URI - http:// + the package path to the implementation
         *      but switched eg: 1/2 -> 2/1 OR 1/2/3 -> 3/1/2.
         *  2nd argument is service name - the name of the webservice which implements
         *      the interface + "Service" at the end of the name.
         */
        QName qname = new QName("http://soap.webservice/", "RuleBaseImplementationService");

        Service service = Service.create(url, qname);

        RuleBaseInterface hello = service.getPort(RuleBaseInterface.class);

        RuleBaseImplementation rbi = new RuleBaseImplementation();

        int clientScore = 690;
        System.out.println("Request 1");
        ArrayList<Bank> liststring = rbi.getBanksByCrediScore(clientScore);
        for (Bank s : liststring) {
            System.out.println(s);
        }
        System.out.println("-----");
        clientScore = 550;
        System.out.println("Request 2");
        liststring = rbi.getBanksByCrediScore(clientScore);
        for (Bank s : liststring) {
            System.out.println(s);
        }

    }

}
