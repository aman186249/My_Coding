package Java;

import java.util.Scanner;

public class prime_checker {

    //function to check if a number is prime
    public static boolean isPrime(int num) {
        if (num <=1) {
            return false;
        }

        if (num <=3) {
            return true
        }

        if (num % 2 == 0 || num % 3 == 0) {
            return false
        }

        int i = 5;
        while (i * i <= num) {
            if (num % i == 0 || num % (i + 2) ==0) {
                return false;
            }
            i += 6;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = scanner.nextInt();

        if (isPrime(num)) {
            System.out.printIn(num + " is a prime number.");
        }
        else {
            System.out.println(num + " is not a prime number.");
        }
        scanner.close();
    }
}
