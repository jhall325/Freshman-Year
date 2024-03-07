import java.math.BigDecimal;
import java.util.Scanner;

public class Lab3B {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);



        System.out.println("Course 1 hours: ");
        float course1 = scanner.nextFloat();
        System.out.println("Grade for course: ");
        float grade1 = scanner.nextFloat();
        System.out.println("Course 2 hours: ");
        float course2 = scanner.nextFloat();
        System.out.println("Grade for course: ");
        float grade2 = scanner.nextFloat();
        System.out.println("Course 3 hours: ");
        float course3 = scanner.nextFloat();
        System.out.println("Grade for course:");
        float grade3 = scanner.nextFloat();
        System.out.println("Course 4 hours: ");
        float course4 = scanner.nextFloat();
        System.out.println("Grade for course: ");
        float grade4 = scanner.nextFloat();



        float quality_points =  (course1 * grade1) + (course2 * grade2) + (course3 * grade3) + (course4 * grade4);
        float total_hours = course1 + course2 + course3 + course4;
        float GPA = quality_points / total_hours;


        System.out.println("Total hours is: " + total_hours);
        System.out.println("Total quality points is : "+ quality_points);
        System.out.println("Your GPA for this semester is " + GPA);


    }

}
