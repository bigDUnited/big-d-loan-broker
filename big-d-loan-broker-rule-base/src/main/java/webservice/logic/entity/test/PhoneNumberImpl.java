package webservice.logic.entity.test;

import javax.xml.bind.annotation.XmlValue;

public class PhoneNumberImpl implements PhoneNumber {

    private String value;

    @XmlValue
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

}
