package main.java.java4kids;

public class Array {

    String[] players = {"David","Daniel","Anna","Gregory"};

    int totalPlayers = players.length;
    int counter=0;

    public void list(){

//        int totalPlayers = players.length;
//        int counter=0;

        for (counter = 0; counter < totalPlayers; counter++) {
            String thePlayer = players[counter];
            System.out.println("Congratulations," +
                    thePlayer + "!");
        }

    }
    public void condition1(){
        while (counter< totalPlayers){

            if (counter == 2){
                break; // Jump out of the loop
            }
            String thePlayer = players[counter];
            System.out.println("Congratulations, "+thePlayer+ "!");
            counter++;
        }
    }
    public void condition_2(){
        do {
            System.out.println("Congratulations, "+
                            players[counter] + "!");
                    counter++;

        } while (counter< totalPlayers);
    }

    public static void main(String[] args){
     Array myArray = new Array();
     myArray.condition_2();
    }

}
