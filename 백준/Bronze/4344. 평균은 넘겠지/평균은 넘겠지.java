import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
	
		int num = sc.nextInt();
		
		for(int i=0; i<num; i++) {
			int student = 0; 
			int total = 0;
			int average = 0;
			int count = 0;
			double rate = 0;
			int[] score = new int[student];
			student = sc.nextInt();
			score = new int[student];
			
			for(int j=0; j<student; j++) {
				score[j] = sc.nextInt(); 
				total += score[j];
			}
			average = total/student;
			
			for(int k=0; k<student; k++) {
				if(score[k]>average) {
					count++;
				}
			}
			
			rate = (double)count*100/student;
			System.out.printf("%.3f%%\n", rate);
		}
	}
}