import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int dan = sc.nextInt();
		
		for (int i=1; i<10; i++) {
			System.out.println(dan + " * " + i + " = " + dan*i);
		}
	}
}