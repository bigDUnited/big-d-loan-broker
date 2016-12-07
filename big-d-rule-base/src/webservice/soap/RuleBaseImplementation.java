package webservice.soap;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import javax.jws.WebService;
import webservice.logic.Controller;
import webservice.logic.entity.Bank;

//Service Implementation
@WebService(endpointInterface = "webservice.soap.RuleBaseInterface")
public class RuleBaseImplementation implements RuleBaseInterface {

    @Override
    public String getHelloWorldAsString(String name) {
        return "Hello World JAX-WS " + name;
    }

    @Override
    public ArrayList<Bank> getBanksByCrediScore(int creditScore) {
        Controller control = new Controller();
        return control.getBanksByCrediScore(creditScore);
    }

    @Override
    public ArrayList<String> helloWorldList() {
        ArrayList<String> ar = new ArrayList();
        ar.add("1");
        ar.add("2");
        return ar;
    }

    @Override
    public ArrayList<Bank> getBanksByCrediScoreJson(int creditScore) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

}
