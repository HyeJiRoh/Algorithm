import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int[] a = new int[num];
		
		
		for(int i = 0; i<num; i++) {
			a[i] = sc.nextInt();
		}
	
		Arrays.sort(a);
		System.out.println(a[0] + " " + a[num-1]);
	}
}