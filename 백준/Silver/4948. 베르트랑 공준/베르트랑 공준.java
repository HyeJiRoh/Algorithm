import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true){
            int n = Integer.parseInt(br.readLine());
            if(n==0) break;
            int answer=0;

            for(int i=n+1; i<=2*n; i++){
                if (isPrime(i)) answer++;
            }
            System.out.println(answer);
        }
    }

    public static boolean isPrime(int n) {
        if(n==1) return false;

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}