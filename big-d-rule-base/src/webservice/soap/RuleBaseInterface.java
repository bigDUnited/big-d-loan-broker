package webservice.soap;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;
import javax.xml.bind.annotation.XmlSeeAlso;
import webservice.logic.entity.Bank;

//Service Endpoint Interface
//Remote procedure call -its calling a method from another system
//You have to tell the system what method to run and what to set as params
@WebService
@SOAPBinding(style = Style.RPC)
public interface RuleBaseInterface {

    @WebMethod
    ArrayList<Bank> getBanksByCrediScore(int creditScore);

    @WebMethod
    String getBanksByCrediScoreJson(int creditScore);

}
