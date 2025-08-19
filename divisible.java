import java.util.Scanner;

class divisible {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number:");
        int n = sc.nextInt();
        
        if (n % 7 == 0) {
            System.out.println("The number is divisible by 7.");
        } else {
            System.out.println("The number is not divisible by 7.");
        }
        
        sc.close();
    }
}