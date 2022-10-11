import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int a = num/10;
		int b = num%10;
		int result = a+b;
		int temp = b*10 + result%10;

		int count = 1;
		
		while(true) {
			int x = temp/10;
			int y = temp%10;
			result = x+y;
			temp = y*10 + result%10;
			
			count+=1 ;
			
			if (num == temp) {
				break;
			}
		}
		if(num == 0) {
			count = 1;
		}
		System.out.println(count);
	}
}