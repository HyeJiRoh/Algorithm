import java.util.*;
import java.math.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int[][] result = new int[a][b];
		int[][] total = new int[a][b];
		
		for(int count=0; count<2; count++) {
			for(int i=0; i<a; i++) {
				for(int j=0; j<b; j++) {
					result[i][j] = sc.nextInt();
					total[i][j] += result[i][j];
				}
			}
		}

		for(int i=0; i<a; i++) {
			for(int j=0; j<b; j++) {
				System.out.printf("%d ", total[i][j]);
			}
			System.out.println("");
		}
	}
}
