import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int check = 0;
		int total = sc.nextInt();
		int quantity = sc.nextInt();
		
		for (int i=0; i<quantity; i++) {
			int price = sc.nextInt();
			int amount= sc.nextInt();
			
			check += price*amount;
		}
		
		if(total == check) {
			System.out.println("Yes");
		}else System.out.println("No");
	}
}