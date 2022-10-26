import java.util.*;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		
		for(int i=1; i<=num; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			int result = a+b;
			
			if((a+b)>=24) {
				result = (a+b)%24;
			} 
			System.out.printf("#%d %d\n", i, result);
		}
	}
}