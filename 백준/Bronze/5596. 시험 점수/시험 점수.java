import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int min = 0;
		int man = 0;
		
		for(int i=0; i<4; i++) {
			min += sc.nextInt();
		}
		
		for(int i=0; i<4; i++) {
			man += sc.nextInt();
		}
		
		if(min>=man) {
			System.out.println(min);
		} else if(min<man) {
			System.out.println(man);
		}
	}
}
