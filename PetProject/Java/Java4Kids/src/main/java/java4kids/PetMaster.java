package main.java.java4kids;

/**
 * Created by Алена on 17.02.2017.
 */
public class PetMaster {
    public static void main(String[] args) {
        String petReaction;

        Pet myPet = new Pet();

        myPet.eat();
        petReaction = myPet.talk("Tweet!!");
        System.out.println(petReaction);
        myPet.sleep();


        Dog myDog = new Dog();
        myDog.talk();
        myDog.swim(7);
        myDog.dive1(2);  // will use default method
//
//        Fish_swimmable myFish = new Fish_swimmable();
//        myFish.swim(50);
//        myFish.dive1(20);

    }
}
