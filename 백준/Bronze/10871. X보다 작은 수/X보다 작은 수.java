import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int min = sc.nextInt();
		
		int[] a = new int[num]; 
		
		for (int i=0; i<num; i++) {
			a[i] = sc.nextInt();
		}
		
		for (int j=0; j<num; j++) {
			if (a[j]<min) {
				System.out.print(a[j] + " ");
			}
		}
	}
}