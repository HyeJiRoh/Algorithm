import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		
		int total = a*60 + b + c;
		int hour = total / 60;
		int min = total % 60;
		
		if (hour>=24) hour = hour-24;
		
		System.out.println(hour + " " + min);
	}
}