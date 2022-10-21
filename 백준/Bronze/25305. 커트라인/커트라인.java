import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int student = sc.nextInt();
		int num = sc.nextInt();
		
		Integer[] grade = new Integer[student];
		
		for(int i=0; i<student; i++) {
			grade[i] = sc.nextInt();
		}
		
		Arrays.sort(grade, Collections.reverseOrder());
		
		System.out.println(grade[num-1]);
	}
}
