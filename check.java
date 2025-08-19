import java.util.Scanner;

public class check {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number:");
        int n = sc.nextInt();
        int lastdigit = n % 10;
        if (lastdigit == 4) {
            System.out.println("last digit is four");
        } else {
            System.out.println("Tlast digit is not four.");
        }
        sc.close();
    }
}