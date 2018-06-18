///**
// * Created by Алена on 19.02.2017.
// */
//public class ReportCard2 {
//
//    String studentName;
//
//    /**
//     The method convertGrades has one integer argument - the result of the school test.  The method returns one letter A, B, C or D depending on the argument's value.
//     */
//    public char convertGrades( int testResult){
//
//        char grade;
//
//        if (testResult >= 90){
//            grade = 'A';
//        } else if (testResult >= 80 && testResult < 90){
//            grade = 'B';
//        }else if (testResult >= 70 && testResult < 80){
//            grade = 'C';
//        }else {
//            grade = 'D';
//        }
//
//        return grade;
//    }
//
//    public static void main(String[] args){
//
//        ReportCard rc = new ReportCard();
//
//        char yourGrade = rc.convertGrades(88);
//        System.out.println("Your first grade is " +
//                yourGrade);
//
//        yourGrade = rc.convertGrades(79);
//        System.out.println("Your second grade is " +
//                yourGrade);
//    }
//}