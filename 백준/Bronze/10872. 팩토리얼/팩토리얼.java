import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int result = 1;
		
		for(int i=0; i<num; i++) {
			result *= i+1;
		}
		System.out.println(result);
	}
}