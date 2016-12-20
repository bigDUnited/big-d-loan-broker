package webservice.soap;

import java.io.StringWriter;
import java.util.ArrayList;
import javax.jws.WebService;
import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBElement;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Marshaller;
import javax.xml.namespace.QName;
import webservice.logic.Controller;
import webservice.logic.entity.Bank;
import webservice.logic.entity.RuleBaseResponse;

//Service Implementation
@WebService(endpointInterface = "webservice.soap.RuleBaseInterface")
public class RuleBaseImplementation implements RuleBaseInterface {

    @Override
    public ArrayList<Bank> getBanksByCreditScore(int creditScore) {
        Controller control = new Controller();
        return control.getBanksByCrediScore(creditScore);
    }

    @Override
    public String getBanksByCreditScoreJson(int creditScore) {
        String xmlString = null;

        Controller control = new Controller();
        ArrayList<Bank> banks = control.getBanksByCrediScore(creditScore);

        RuleBaseResponse rbr = new RuleBaseResponse(banks);

        try {
            JAXBContext jaxbContext = JAXBContext.newInstance(RuleBaseResponse.class);
            Marshaller jaxbMarshaller = jaxbContext.createMarshaller();

            // output pretty printed
            jaxbMarshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

            //Create array of objects based on RuleBase structure
            JAXBElement<RuleBaseResponse> je2 = new JAXBElement(
                    new QName("RuleBaseList"), RuleBaseResponse.class, rbr);

            //jaxbMarshaller.marshal(customer, file);
            StringWriter sw = new StringWriter();
            jaxbMarshaller.marshal(je2, sw);
            xmlString = sw.toString();

        } catch (JAXBException e) {
            return "Internal server error : " + e;
        }

        return xmlString;
    }
}
