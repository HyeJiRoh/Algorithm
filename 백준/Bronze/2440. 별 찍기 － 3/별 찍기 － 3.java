import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int input = sc.nextInt();
		
		for(int i=input; i>=0; i--) {
			for(int j=0; j<i; j++) {
				System.out.print("*");
			}
			System.out.println("");
		}
	}
}
