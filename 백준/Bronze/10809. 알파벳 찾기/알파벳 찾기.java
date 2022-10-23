import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int[] alpha = new int[26];
		
		for(int i=0; i<alpha.length; i++) {
			alpha[i] = -1;
		}
		
		String str = sc.nextLine();
		
		for(int i=0; i<str.length(); i++) {
			char ch = str.charAt(i);
			
			if(alpha[ch-'a'] == -1) {
				alpha[ch-'a'] = i;
			}
		}
		
		for(int i=0; i<26; i++) {
			System.out.printf("%d ", alpha[i]);
		}
	}
}
