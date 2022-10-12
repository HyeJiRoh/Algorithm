import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int[] arr = new int[30];
		
		arr[0]=0;
		arr[1]=1;
		
		for(int i=2; i<=num; i++) {
			arr[i]= arr[i-1]+ arr[i-2];	
		}		
		
		System.out.println(arr[num]);
	}
}