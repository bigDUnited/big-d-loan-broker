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
//Remote procedure call -its calling am ethod from another system
// you ahve to tell the systme what method to run and params
@WebService
@SOAPBinding(style = Style.RPC)
public interface RuleBaseInterface {
    
    @WebMethod
    String getHelloWorldAsString(String name);

    @WebMethod
    ArrayList<Bank> getBanksByCrediScore(int creditScore);
    
    @WebMethod
    ArrayList<String> helloWorldList();

}
