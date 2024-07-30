import java.util.Scanner;

public class PalindromeChecker {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter a string to check if it is a palindrome:");
        String input = scanner.nextLine();
        
        if (isPalindrome(input)) {
            System.out.println("The string is a palindrome.");
        } else {
            System.out.println("The string is not a palindrome.");
        }
        
        scanner.close();
    }

    public static boolean isPalindrome(String str) {
        int left = 0;
        int right = str.length() - 1;
        
        while (left < right) {
            // Compare characters at left and right indices
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            // Move towards the center
            left++;
            right--;
        }
        
        return true;
    }
}
