import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int reward = 0;
		
		if(a==b && b==c) {
			reward = 10000+a*1000;
		}else if (a==b || b==c) {
			reward = 1000+b*100;
		}else if (a==c) {
			reward = 1000+a*100;
		}else {
			if(a>b && a>c) {
				reward = a*100;
			}else if (b>a && b>c) {
				reward = b*100;
			}else if (c>a && c>b)reward = c*100;
		}
		System.out.println(reward);
	}
}