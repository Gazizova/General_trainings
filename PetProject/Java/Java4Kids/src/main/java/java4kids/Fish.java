package main.java.java4kids;

/**
 * Created by Алена on 17.02.2017.
 */
public class Fish extends Pet implements Swimmable{
    int currentDepth=0;
    public int dive(int howDeep) {

        currentDepth = currentDepth + howDeep;
        if ((currentDepth > 100) | (currentDepth == 100)){
            System.out.println("I am a little fish and  " + " can't dive below 100 feet");
            currentDepth = currentDepth - howDeep;
        } else {
            System.out.println("Diving for " + howDeep + " feet");
            System.out.println("I am at " + howDeep + " feet below sea level");
        }
        return currentDepth;
    }
    public String talk(String smth){
        String petResponse = smth + " But... Don't you know that fish do not talk?";
        return petResponse;
    }
    public void swim(int howFar){
        System.out.println("OK, will swim " + howFar + " feet");
    }
    public void dive1(int howDeep){
        System.out.println("OK, will dive " + howDeep + " feet");
    }
}

