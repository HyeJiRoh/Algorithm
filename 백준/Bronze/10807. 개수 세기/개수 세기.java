import java.util.*;
import java.math.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int input = sc.nextInt();
		int[] arr = new int[input];
		int total = 0;
		
		for(int i=0; i<input; i++) {
			arr[i] = sc.nextInt();	
		}
		
		int num = sc.nextInt();
		
		for(int i=0; i<arr.length; i++) {
			if(num == arr[i]) {
				total += 1;
			}
		}
		System.out.println(total);
	}
}
