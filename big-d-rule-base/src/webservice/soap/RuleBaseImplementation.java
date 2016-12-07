package webservice.soap;

import com.google.gson.Gson;
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
    public ArrayList<Bank> getBanksByCrediScore(int creditScore) {
        Controller control = new Controller();
        return control.getBanksByCrediScore(creditScore);
    }

    @Override
    public String getBanksByCrediScoreJson(int creditScore) {
        Controller control = new Controller();
        return new Gson().toJson(control.getBanksByCrediScore(creditScore));
    }

}
