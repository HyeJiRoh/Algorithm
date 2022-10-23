import java.util.*;
import java.math.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		String str = sc.nextLine();
		
		char[] ch = str.toCharArray();
		
		int total = 0;
		
		for(int i=0; i<ch.length; i++) {
			if(ch[i]=='A' || ch[i]=='B' || ch[i]=='C') {
				total += 3;
			}
			else if(ch[i]=='D' || ch[i]=='E' || ch[i]=='F') {
				total += 4; 
			}
			else if(ch[i]=='G' || ch[i]=='H' || ch[i]=='I') {
				total += 5; 
			}
			else if(ch[i]=='J' || ch[i]=='K' || ch[i]=='L') {
				total += 6; 
			}
			else if(ch[i]=='M' || ch[i]=='N' || ch[i]=='O') {
				total += 7; 
			}
			else if(ch[i]=='P' || ch[i]=='Q' || ch[i]=='R' || ch[i]== 'S') {
				total += 8; 
			}
			else if(ch[i]=='T' || ch[i]=='U' || ch[i]=='V') {
				total += 9; 
			}
			else if(ch[i]=='W' || ch[i]=='X' || ch[i]=='Y' || ch[i]=='Z') {
				total += 10; 
			}
		}
		System.out.println(total);
	}
}
