//package webservice.client;
//
//import webservice.soap.RuleBaseInterface;
//import webservice.soap.RuleBaseImplementationService;
//
//public class RuleBaseClient2 {
//
//    public static void main(String[] args) {
//
//        RuleBaseImplementationService helloService = new RuleBaseImplementationService();
//        RuleBaseInterface rbi = (RuleBaseInterface) helloService.getRuleBaseImplementationPort();
//
//        System.out.println("Remote Request 1: " + rbi.getBanksByCreditScoreJson(690));
//        System.out.println("Remote Request 2: " + rbi.getBanksByCreditScoreJson(550));
//    }
//
//}
