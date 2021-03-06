package main.java.java4kids;

import java.time.LocalDate;
import java.time.Month;

public interface Swimmable {

    public void swim(int howFar);

    public default void dive1(int howDeep){

        if (isSummer()){
            System.out.println("OK, will dive. The water should be warm.");
        } else {
            System.out.println("Can't dive, sorry. The water's cold for diving.");
        }
    };

    // Check if it's summer now
    static boolean isSummer(){
        Month month = LocalDate.now().getMonth();
        if (month == Month.JUNE || month == Month.JULY || month == Month.AUGUST){
            return true;
        } else{
            return false;
        }
    }
}