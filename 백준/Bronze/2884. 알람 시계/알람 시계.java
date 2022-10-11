import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int h = sc.nextInt();
		int m = sc.nextInt();
		
		if (m < 45) {
			if(h==0) {
				h=23;
			} else 
				h-=1;
			m+=15;
		}else
			m-=45;
		
		System.out.println(h + " " + m);
	}
}