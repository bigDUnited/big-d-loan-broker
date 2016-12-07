package webservice.logic.entity;

public class Rank {

    private final int rankLevel;
    private final int lowerLimit;
    private final int upperLimit;

    public Rank(int rankLevel, int lowerLimit, int upperLimit) {
        this.rankLevel = rankLevel;
        this.lowerLimit = lowerLimit;
        this.upperLimit = upperLimit;
    }

    public int getLowerLimit() {
        return lowerLimit;
    }

    public int getRankLevel() {
        return rankLevel;
    }

    public int getUpperLimit() {
        return upperLimit;
    }

}
