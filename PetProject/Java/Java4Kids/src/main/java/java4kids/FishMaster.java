package main.java.java4kids;

/**
 * Created by Алена on 17.02.2017.
 */
public class FishMaster {
    public static void main(String[] args) {
        Fish myFish = new Fish();

        myFish.eat();
        myFish.dive(5);
        myFish.dive(95);



        String fishReaction;
        fishReaction = myFish.talk("Hey!");
        System.out.println(fishReaction);

    }
}
