import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		String input = sc.next();
		
		String[] arr = input.split("");
		
		int total = 0;
		
		for(int i=0; i<num; i++) {
			total += Integer.parseInt(arr[i]);
		}
		
		System.out.println(total);
	}
}