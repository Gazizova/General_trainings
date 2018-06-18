package main.java.java4kids;

public class Fish_swimmable implements Swimmable {
    public void swim(int howFar){
        System.out.println("OK, will swim " + howFar + " feet");
    }
    public void dive(int howDeep){
        System.out.println("OK, will dive " + howDeep + " feet");
    }
}
