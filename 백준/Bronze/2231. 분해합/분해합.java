import java.io.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int num = Integer.parseInt(br.readLine());

		for(int i=1; i<=num; i++) {
			String temp = Integer.toString(i);
			int sum = 0;
			
			for(int j=0; j<temp.length(); j++) {
				sum += Character.getNumericValue(temp.charAt(j));
			}
			sum += Integer.parseInt(temp);
			
			if(sum == num) {
				System.out.println(temp);
				break;
			}
			else if(i == num) {
				System.out.println(0);
			}
		}
	}
}