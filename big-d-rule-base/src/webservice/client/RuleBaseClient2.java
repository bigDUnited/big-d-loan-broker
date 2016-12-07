package webservice.client;

import wsimport.webservice.soap.RuleBaseImplementationService;
import wsimport.webservice.soap.RuleBaseInterface;

public class RuleBaseClient2 {

    public static void main(String[] args) {

        RuleBaseImplementationService helloService = new RuleBaseImplementationService();
        RuleBaseInterface rbi = helloService.getRuleBaseImplementationPort();

        System.out.println(rbi.getHelloWorldAsString("Secondary Client"));
    }

}
