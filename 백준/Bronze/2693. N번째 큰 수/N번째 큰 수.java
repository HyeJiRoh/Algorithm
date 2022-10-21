import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		for(int i=0; i<num; i++) {
			int[] arr = new int[10];
			for(int j=0; j<10; j++) {
				arr[j] = sc.nextInt();
			}
			Arrays.sort(arr);
			System.out.println(arr[7]);
		}
	}
}
