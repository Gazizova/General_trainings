package main.java.java4kids;

/**
 * Created by Алена on 19.02.2017.
 */
public class ReportCard {
    String studentName;

    public char convertGrade(int testResult) {
        char grade;

        if (testResult >= 90) {
            grade = 'A';
        } else if (testResult >= 80 && testResult < 90) {
            grade = 'B';
        } else if (testResult >= 70 && testResult < 80) {
            grade = 'C';
        } else {
            grade = 'D';
        }
        return grade;
    }

//    public static void main(String[] args) {
//        ReportCard rd = new ReportCard();
//        rd.studentName = "Nik";
//
//        char yourGrade = new rd.convertGrade(8);
//        System.out.println("Your grade is " + yourGrade);
//
//    }
        public static void main(String[] args) {
            ReportCard rc = new ReportCard();
//            rc.studentName = "Jerry";

            char yourGrade = rc.convertGrade(90);

            switch (yourGrade){
                case 'A':
                    System.out.println("Excellent!");
                    break;
                case  'B':
                    System.out.println("Good!");
                    break;
            }
    }
}
