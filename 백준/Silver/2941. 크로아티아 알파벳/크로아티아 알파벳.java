import java.util.*;
import java.math.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		String str = sc.nextLine();
		String[] arr = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
		

		for(int i=0; i<arr.length; i++) {
			if(str.contains(arr[i])) {
				str = str.replace(arr[i], "!");
			}
		}
		
		System.out.println(str.length());
	}
}
