import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
	
		int num = sc.nextInt();
		
		String[] arr = new String[num];
		
		for(int i=0; i<num; i++) {
			int count = 0;
			int sum =0;
			arr[i]=sc.next();
			for(int j=0; j<arr[i].length(); j++) {
				if(arr[i].charAt(j)=='O') {
					count++;
				}else count =0;
				sum+=count;
			}
			System.out.println(sum);
		}
	}
}