import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int month = sc.nextInt();
        int day = sc.nextInt();

        int[] Month = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String[] Day = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};

        int result = day;
        for (int i = 0; i < month - 1; i++) {
            result += Month[i];
        }
        System.out.print(Day[result % 7]);
    }
}