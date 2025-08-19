import java.util.Scanner;

public class avg{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter five numbers:");
         System.out.print("Enter a: ");
        double a = scanner.nextDouble();
        System.out.print("Enter b: ");
        double b = scanner.nextDouble();
        System.out.print("Enter c: ");
        double c = scanner.nextDouble();
        System.out.print("Enter d: ");
        double d = scanner.nextDouble();
        System.out.print("Enter e: ");
        double e = scanner.nextDouble();
        double average = (a + b + c + d + e) / 5;
        System.out.println("The average of the five numbers is: " + average);
        scanner.close();
    }
}
