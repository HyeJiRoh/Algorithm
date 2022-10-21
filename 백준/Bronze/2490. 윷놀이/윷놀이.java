import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int[] game = new int[4];
		
		for(int a=0; a<3; a++) {
			int count = 0;
			for(int i=0; i<4; i++) {
				game[i] = sc.nextInt();
				if(game[i] == 0) {
					count ++;
				}
			}
			
			if(count == 4) {
				System.out.println("D");
			} else if(count == 3) {
				System.out.println("C");
			} else if(count == 2) {
				System.out.println("B");
			} else if(count == 1) {
				System.out.println("A");
			} else
				System.out.println("E");	
		}
	}
}
