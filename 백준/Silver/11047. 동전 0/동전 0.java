import java.util.Scanner;
 
public class Main {
 
	public static void main(String[] args) {
 
		Scanner in = new Scanner(System.in);
		
		int num = in.nextInt();
		int price = in.nextInt();
		
		int[] coin = new int[num];
		
		for(int i = 0; i < num; i++) {
			coin[i] = in.nextInt();
		}
		
		int count = 0;
 
		for(int i = num - 1; i >= 0; i--) {
 
			// 현재 동전의 가치가 K보다 작거나 같아야지 구성가능하다.
			if(coin[i] <= price) {
				// 현재 가치의 동전으로 구성할 수 있는 개수를 더해준다.
				count += (price / coin[i]);
				price = price % coin[i];
			}
		}
		System.out.println(count);
	}
 
}