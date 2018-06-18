package calc;

public class CalculatorWithAnonymousClasses {
    // The first anonymous class for addition
    static ArithmeticOperation addition = new ArithmeticOperation() {
        public double performOperation(double first, double second) {
            double result = first + second;
            System.out.println("" + first + " * " +
                    second + " = " + result );
            return result;
        }
    };

    // The second anonymous class for subtraction
    static ArithmeticOperation subtraction = new ArithmeticOperation() {
        public double performOperation(double first, double second) {
            double result = first - second;
            System.out.println("" + first + " - " +
                    second + " = " + result );
            return result;
        }
    };


    public static double calculate(ArithmeticOperation whatToDo, double a, double b ){

        return whatToDo.performOperation(a,b);
    }

    public static void main(String[] args) {

        calculate(addition, 3.55, 50.00);
        calculate(subtraction, 3.55, 50.00);
    }
}
