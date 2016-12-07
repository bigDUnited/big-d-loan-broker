package webservice.logic.entity.test;
 
import java.util.List;
 
public interface Customer {
 
    Address getAddress();
 
    void setAddress(Address address);
 
    List<PhoneNumber> getPhoneNumbers();
 
    void setPhoneNumbers(List<PhoneNumber> phoneNumbers);
 
}