package main.java.java4kids;

/**
 * Created by Алена on 17.02.2017.
 */
public class JamesBondCar extends Car{
    public int drive(int howlong){

        int distance =howlong * 180;
        System.out.println("I'm Bond, I run " + distance);
        return distance;
    }
}
