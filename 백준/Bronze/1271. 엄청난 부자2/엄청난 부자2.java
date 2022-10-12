import java.util.Scanner;
import java.math.BigInteger;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		BigInteger money = sc.nextBigInteger();
		BigInteger person = sc.nextBigInteger();
		
		System.out.println(money.divide(person));
		System.out.println(money.remainder(person));
	}
}