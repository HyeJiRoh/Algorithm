import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		for (int i=0; i<num; i++) {
			String words = "";
			int count = sc.nextInt();
			String[] word = sc.next().split("");
			for(int j=0; j<word.length; j++) {
				words += word[j].repeat(count);
			}
			System.out.println(words);
		}
	}
}