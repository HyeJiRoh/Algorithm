import java.util.*;
import java.math.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int[][] arr = new int[10][10];
		int max = 0;
		int a = 0;
		int b = 0;
		
		for(int i=0; i<9; i++) {
			for(int j=0; j<9; j++) {
				arr[i][j] = sc.nextInt();
				if(max<arr[i][j]) {
					max = arr[i][j];
					a = i;
					b = j;
				}
			}
		}
		System.out.println(max);
		System.out.println((a+1) + " " + (b+1));
	}
}
