import java.util.*;
import java.math.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		String str = sc.nextLine().toUpperCase();
		int[] result = new int[26];
		
		for(int i=0; i<result.length; i++) {
			result[i] = 0;
		}
		
		for(int i=0; i<str.length(); i++) {
			char ch = str.charAt(i);	
			result[ch-'A'] += 1;
		}
		
		int max = -1;
		char answer = '?';
		
		for(int i=0; i<26; i++) {
			if(max<result[i]) {
				max = result[i];
				answer = (char)(i+65);
			} else if(max == result[i]) {
				answer = '?';
			}
		}
		System.out.println(answer);
	}
}
