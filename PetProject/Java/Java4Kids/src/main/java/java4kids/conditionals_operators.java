package main.java.java4kids;

public class conditionals_operators {

    int price = 60;
    double discount = 5;

    public double disc(int price) {
        if (price > 50) {
            discount = discount * 0.5;
        } else {
            discount = 5;
        }
        return discount;

// the same as
//        discount = price > 50 ? 10 : 5;
    }
    public static void main(String[] args) {
        conditionals_operators My = new conditionals_operators();
        double a = My.disc(51);
        System.out.println(a);
    }

}



