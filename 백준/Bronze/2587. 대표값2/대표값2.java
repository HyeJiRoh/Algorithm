import java.util.*;
import java.math.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		int[] num = new int[5];
		int total = 0;
		
		for(int i=0; i<5; i++) {
			num[i] = sc.nextInt();
			total += num[i];
		}
		
		Arrays.sort(num);
		
		System.out.println(total/5);
		System.out.println(num[2]);
	}
}
