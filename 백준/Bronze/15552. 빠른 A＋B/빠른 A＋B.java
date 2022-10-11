import java.io.*;
public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
		int num = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < num; i++) {
			String string = br.readLine();
			int a = Integer.parseInt(string.split(" ")[0]);
			int b = Integer.parseInt(string.split(" ")[1]);
			bw.write(a+b+"\n");
		}
		bw.flush();
	}
}