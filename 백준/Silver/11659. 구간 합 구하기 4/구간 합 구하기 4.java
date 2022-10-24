import java.util.*;
import java.math.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int repeat = sc.nextInt();
		int[] arr = new int[num+1];
		int[] sum = new int[num+1];
		int a=0;
		int b=0;
		int[] result = new int[repeat+1];
		
		for(int i=1; i<=num; i++) {
			arr[i] = sc.nextInt();
		}
		
		sum[1] = arr[1];
		
		for(int i=2; i<=num; i++) {
			sum[i] = arr[i] + sum[i-1];
		}
		
		for(int i=0; i<repeat; i++) {
			a = sc.nextInt();
			b = sc.nextInt();
			result[i] = sum[b]-sum[a-1];
		}
		
		for(int i=0; i<repeat; i++) {
			System.out.println(result[i]);
		}
	}
}
