import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int total = 0;
		int num = sc.nextInt();
		
		for (int i=1; i<=num; i++) {
			total +=i;
		}
		
		System.out.println(total);
	}
}