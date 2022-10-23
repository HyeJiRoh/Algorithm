import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		int resultA = a%10*100 + a%100/10*10 + a/100;
		int resultB = b%10*100 + b%100/10*10 + b/100;
		
		if(resultA > resultB) {
			System.out.println(resultA);
		} else if(resultA < resultB) {
			System.out.println(resultB);
		}
	}
}
