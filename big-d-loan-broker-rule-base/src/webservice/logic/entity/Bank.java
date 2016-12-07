package webservice.logic.entity;

import java.util.Arrays;

public class Bank {

    private final String name;
    private final int[] ranks;

    public Bank(String name, int[] ranks) {
        this.name = name;
        this.ranks = ranks;
    }

    public String getName() {
        return name;
    }

    public int[] getRanks() {
        return ranks;
    }

    @Override
    public String toString() {
        return "Bank{" + "name=" + name + ", ranks=" + Arrays.toString(ranks) + '}';
    }

}
