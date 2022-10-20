import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			if(a==0 && b==0) {
				break;
			}
			
			if(a>b) {
				System.out.println("Yes");
			}else 
				System.out.println("No");	
		}
	}
}
