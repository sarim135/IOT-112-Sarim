import java.util.Scanner;
public class sum {
    public static void main(String[] args) {
        System.out.println("Making the program for adding three numbers.");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int sum = a + b + c;
        System.out.println("The sum is...");
        System.out.println(sum);
        sc.close();
    }
    
}
