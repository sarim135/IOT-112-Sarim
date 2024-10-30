import java.util.Scanner;
public class printing_out_string_Day03_part {
    public static void main(String[] args) {
        System.out.println("Printing out the string by scanner module>>");
        Scanner sc = new Scanner(System.in);
        // String str = sc.next();
        // System.out.println(str);
        String str1 = sc.nextLine();
        System.out.println(str1);
        sc.close();
    }
}
