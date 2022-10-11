import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
	
		int num = sc.nextInt(); // 입력받을 시험 과목 수
		double[] score = new double[num]; // 입력받을 시험 점수
		double max = score[0];
		double total = 0;
		
		for(int i = 0; i<num; i++) {
			score[i]=sc.nextInt();
		}
		
		for(int j=0; j<num; j++) {
			if(score[j]>=max) {
				max = score[j];
			}
		}
		
		for(int k=0; k<num; k++) {
			total += score[k]/max*100;
		}

		System.out.println((double)total/num);
	}
}