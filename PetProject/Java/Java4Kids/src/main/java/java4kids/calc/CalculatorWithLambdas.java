package calc;

public class CalculatorWithLambdas {

    // Implementing addition as a lambda expression
    static ArithmeticOperation addition=(first, second) -> {
        double result = first + second;
        System.out.println("" + first + " + " +
                second + " = " + result );
        return result;
    };

    // Implementing addition as a lambda expression
    static ArithmeticOperation subtraction = (first, second) -> {
        double result = first - second;
        System.out.println("" + first + " - " +
                second + " = " + result );
        return result;
    };

    public static double calculate(ArithmeticOperation whatToDo, double a, double b ){

        return whatToDo.performOperation(a,b);
    }

    public static void main(String[] args) {

        calculate(addition, 3.55, 50.00);
        calculate(subtraction, 3.55, 50.00);
    }
}
