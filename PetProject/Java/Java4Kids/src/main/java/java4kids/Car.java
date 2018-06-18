package main.java.java4kids;

/**
 * Created by Алена on 17.02.2017.
 */
public class Car {
    public void start(){
           System.out.println("I'm start!");
        }
    public void stop(){
        System.out.println("Stop! Stop!!!");
    }

    public int drive(int howlong){

        int distance =howlong * 60;
        System.out.println("I run " + distance + " meters!");
        return distance;
    }
}
