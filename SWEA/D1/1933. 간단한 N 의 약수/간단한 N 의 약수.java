import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		
		int input = sc.nextInt();
		
		for(int i=1; i<=input; i++) {
			if(input%i == 0) {
				System.out.print(i + " ");
			}
		}
	}
}