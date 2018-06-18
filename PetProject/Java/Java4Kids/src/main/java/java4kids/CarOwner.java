package main.java.java4kids;

/**
 * Created by Алена on 17.02.2017.
 */
public class CarOwner {
    public static void main(String[] args) {
        Car myCar = new Car();

        myCar.start();
        myCar.drive(6);
        myCar.stop();

        JamesBondCar Bond = new JamesBondCar();
        Bond.drive(5);

    }
}
