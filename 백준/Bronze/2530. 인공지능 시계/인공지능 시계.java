import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int hour = sc.nextInt();
		int minute = sc.nextInt();
		int second = sc.nextInt();
		
		int time = sc.nextInt();
		
		int total = 0;
		int final_hour = 0;
		
		if(hour == 0) {
			hour = 24;
		}
		
		total = hour*3600 + minute*60 + second + time;
		
		if(total/3600 >= 24) {
			final_hour = total/3600%24;
		}else 
			final_hour = total/3600;
		
		System.out.println(final_hour + " " + total%3600/60 + " " + total%60);
	}
}
