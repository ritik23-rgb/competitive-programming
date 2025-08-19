import java.util.Scanner;

class check1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number:");
        int n = sc.nextInt();
        int lastDigit = n % 10;

     
        if (n % 3 == 0 || lastDigit  == 4) {
            System.out.println("The number is divisible by 3 andlast digit is 4 .");
        } else {
            System.out.println("The number is not divisible by 3.");
        }

        
       

        sc.close();
    }
}