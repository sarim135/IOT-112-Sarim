import java.util.Scanner;

public class Day03_input {
   public static void main(String[] args) {
      // Getting input from the user by using the normal functions of the scanner module.
        System.out.println("Taking input from the user:");
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number 1");
        int a = sc.nextInt();
        System.out.println("Enter number 2");
        int b = sc.nextInt();
        int sum = a + b;
        System.out.println("The sum of the two input numbers is:" + sum);
      // knowing if the number is integer or not by the boolean method.(By scanner module)
        Boolean b1 = sc.hasNextInt();
        System.out.println(b1);
        sc.close();
   }
}
