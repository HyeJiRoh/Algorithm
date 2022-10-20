import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		String name = "";
		int height = 0;
		int weight = 0;
		
		while(true) {
			name = sc.next();
			height = sc.nextInt();
			weight = sc.nextInt();
			
			if(name.equals("#") && height == 0 && weight ==0) {
				break;
			}
			
			if(height > 17 || weight >= 80) {
				System.out.println(name + " Senior");
			} 
			else 
				System.out.println(name + " Junior");
		}
	}
}
