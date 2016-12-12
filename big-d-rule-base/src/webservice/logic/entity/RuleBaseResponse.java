package webservice.logic.entity;

import java.util.ArrayList;

public class RuleBaseResponse {
    private ArrayList<Bank> bankElem;

    public RuleBaseResponse( ArrayList<Bank> bankElem ) {
        this.bankElem = bankElem;
    }

    public ArrayList<Bank> getBankElem() {
        return bankElem;
    }

    public void setBankElem(ArrayList<Bank> bankElem) {
        this.bankElem = bankElem;
    }
}