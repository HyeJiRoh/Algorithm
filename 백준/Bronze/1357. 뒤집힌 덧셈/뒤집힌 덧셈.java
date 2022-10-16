import java.util.Scanner;

public class Main {
	
	private static int Rev(int num) {
       int result = 0;
            while (num > 0) {
            result = result * 10 + num % 10;
            num /= 10;
        }

       return result; 
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
	
        int result = Rev(Rev(a) + Rev(b));
        System.out.println(result);
	}
}