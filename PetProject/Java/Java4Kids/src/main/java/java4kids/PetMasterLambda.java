package main.java.java4kids;

public class PetMasterLambda{
    public static void main(String[] args) {

        // dogs
        Pet myDog = new Pet();

        Talkative1 dogTalkRules = (name) -> {
            return  "I'm a dog. My name is " + name;
        };

        System.out.println(myDog.speakup(dogTalkRules, "Sammy"));

        // parrots


//        Pet myParrot = new Pet();
//        Talkative1 parrotTalkRules = (name) -> {
//            return  "I'm a parrot. Don't call me " + name;
//        };

//        System.out.println(myDog.speakup(parrotTalkRules, "Charlie"));
    }
}
