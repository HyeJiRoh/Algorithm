import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		for(int i=2; i<=num; i++) {
			while(num%i == 0) {
				num /= i;
				System.out.println(i);
			}
		}
	}
}
