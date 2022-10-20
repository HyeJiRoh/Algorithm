import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int value = 0;
		
		for(int i=0; i<5; i++) {
			int input = sc.nextInt();
			
			value += Math.pow(input, 2);
		}
		System.out.println(value%10);
	}
}
