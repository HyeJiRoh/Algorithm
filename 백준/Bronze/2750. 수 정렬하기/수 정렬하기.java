import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int[] input = new int[num];
		
		for(int i=0; i<num; i++) {
			input[i] = sc.nextInt();
		}
		
		Arrays.sort(input);
		
		for(int i=0; i<num; i++) {
			System.out.println(input[i]);
		}
	}
}
