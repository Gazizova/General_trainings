package main.java.java4kids;

/**
 * Created by Алена on 17.02.2017.
 */
public class Pet {
    int age;
    float weight;
    float height;
    String color;
    public void sleep(){
        System.out.println(
                "Good night, see you tomorrow!");
    }

    public void eat(){
        System.out.println(
                "I’m so hungry, let me have a snack like nachos!");
    }

    public String talk(String aWord){
        String petResponse = "OK!! OK!! " +aWord;
        return petResponse;
    }

    public String speakup(Talkative1 talkRules, String name){
        return talkRules.talk1(name);
    }
}
