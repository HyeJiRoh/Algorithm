import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);

		int[] chess = {1, 1, 2, 2, 2, 8};
		int[] user = new int[6];
		
		for (int i=0; i<user.length; i++) {
			user[i] = sc.nextInt();
			System.out.print(chess[i]-user[i]+" ");
		}
	}
}
