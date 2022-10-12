import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
	
		int count = 1;
		int num[] = new int[10];
		
		for(int i=0; i<10; i++) {
			num[i]=sc.nextInt()%42;
		}
		
		Arrays.sort(num);
		
		for(int j=0; j<9; j++) {
			if(num[j] != num[j+1]) {
				count +=1;
			}
		}
		System.out.println(count);
	}
}