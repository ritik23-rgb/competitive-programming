import java.util.Scanner;

public class riangle {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        
        System.out.print("Enter first angle: ");
        int num1 = scanner.nextInt();

        System.out.print("Enter second angle: ");
        int num2 = scanner.nextInt();

        System.out.print("Enter third angle: ");
        int num3 = scanner.nextInt();


        if (num1 + num2+ num3 == 180) {
            System.out.println("this is a valid triangle");
        } else {
            System.out.println("this is not a valid triangle");
        }
        scanner.close();    
    }
}