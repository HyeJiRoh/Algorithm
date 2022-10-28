import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int price = sc.nextInt();
		
		int[] coin = new int[num];
		
		
		for(int i=0; i<num; i++) {
			coin[i] = sc.nextInt();
		}
		
		int result = 0;
		
		for(int i= num-1; i>=0; i--) {
			if (price >= coin[i]) {
				result += (price/coin[i]);
				price %= coin[i];
			}
		}
		System.out.println(result);
	}
}