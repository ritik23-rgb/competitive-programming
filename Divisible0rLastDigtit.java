import java.util.Scanner;

class DivisibleOrLastDigit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int lastDigit = n % 10;

        
        if (n % 3 == 0 || lastDigit == 4) {
            System.out.println(" The number is  divisible by 3 or last  4.");
        } else {
            System.out.println(" The number is NOT divisible by 3 and last digit 4");
        }

        sc.close();
    }
}