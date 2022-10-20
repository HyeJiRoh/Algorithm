import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int[] input = new int[3];
		
		for(int i=0; i<input.length; i++) {
			input[i] = sc.nextInt();
		}
		
		Arrays.sort(input);
		
		for(int i=0; i<input.length; i++) {
			System.out.print(input[i] + " ");
		}
	}
}
