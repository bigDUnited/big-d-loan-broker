package webservice.logic;

import java.util.ArrayList;
import webservice.logic.entity.Bank;
import webservice.logic.entity.Rank;
import webservice.logic.utils.RanksLevels;

public class Controller {

    private ArrayList<Bank> banksList;
    private ArrayList<Bank> shareableList;
    private ArrayList<Rank> ranksList;

    public Controller() {
        banksList = new ArrayList();
        ranksList = new ArrayList();
        loadBanks();
        loadRanks();
    }

    private void loadBanks() {
        banksList.add(new Bank("danskebank_translator_queue", new int[]{RanksLevels.EXCELLENT_CS,
            RanksLevels.GOOD_CS}));
        banksList.add(new Bank("nordea_translator_queue", new int[]{RanksLevels.GOOD_CS, RanksLevels.AVERAGE_CS,
            RanksLevels.POOR_CS}));
        banksList.add(new Bank("nytkredit_translator_queue", new int[]{RanksLevels.AVERAGE_CS,
            RanksLevels.POOR_CS, RanksLevels.BAD_CS}));
        banksList.add(new Bank("bdo_translator_queue", new int[]{RanksLevels.POOR_CS,
            RanksLevels.BAD_CS, RanksLevels.MISERABLE_CS}));

    }

    private void loadRanks() {
        ranksList.add(new Rank(RanksLevels.EXCELLENT_CS, 720, 800));
        ranksList.add(new Rank(RanksLevels.GOOD_CS, 680, 719));
        ranksList.add(new Rank(RanksLevels.AVERAGE_CS, 620, 679));
        ranksList.add(new Rank(RanksLevels.POOR_CS, 580, 619));
        ranksList.add(new Rank(RanksLevels.BAD_CS, 500, 579));
        ranksList.add(new Rank(RanksLevels.MISERABLE_CS, 0, 500));
    }

    public ArrayList<Bank> getBanksByCrediScore(int creditScore) {
        shareableList = new ArrayList();
        int chosenRank = 0;

        for (int i = 0; i < ranksList.size(); i++) {
            if (ranksList.get(i).getLowerLimit() < creditScore && ranksList.get(i).getUpperLimit() > creditScore) {
                chosenRank = ranksList.get(i).getRankLevel();
                break;
            }
        }

        if (chosenRank > 0) {
            for (int x = 0; x < banksList.size(); x++) {
                int[] currRanksList = banksList.get(x).getRankElem();
                for (int y = 0; y < currRanksList.length; y++) {
                    if (currRanksList[y] == chosenRank) {
                        shareableList.add(banksList.get(x));
                    }
                }
            }
        }
        return shareableList;
    }
}
