import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int[] a = new int[9];
		int max = a[0];
		int count = 0;
		
		for (int i=0; i<9; i++) {
			a[i] = sc.nextInt();
		}
		
		for(int j=0; j<9; j++) {
			if(max<a[j]) {
				max=a[j];
				count = j+1;
			}
		}
		System.out.println(max);
		System.out.println(count);
	}
}