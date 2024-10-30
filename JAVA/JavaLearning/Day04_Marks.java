import java.util.Scanner;

public class Day04_Marks {
    public static void main(String[] args) {
        System.out.println("This is the program for checking the percentage of the marks of the students.");
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your marks...");
        int marks = sc.nextInt();
        int totalMarks = 1100;
        double percentage = (double)marks / totalMarks * 100.0;
        System.out.println(percentage);
        if (percentage > 80){
            System.out.println("YOU'VE GOT GRADE A");
        }
        else if (percentage < 80){
            System.out.println("YOU'VE GOT GRADE B");
        }
        else {
            System.out.println("The program has ended.");
        }
        sc.close();
        }
}