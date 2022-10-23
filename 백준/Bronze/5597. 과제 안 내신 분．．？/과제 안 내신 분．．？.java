import java.util.*;
import java.math.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		int[] num = new int[31];
		
		for(int i=1; i<29; i++) {
			int input = sc.nextInt();
			num[input] = 31;
		}
		
		for(int i=1; i<num.length; i++) {
			if(num[i]!=31) {
				System.out.println(i);
			}
		}
	}
}
