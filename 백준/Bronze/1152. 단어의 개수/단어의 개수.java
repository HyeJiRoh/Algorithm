import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String word = sc.nextLine();
    int count = 1;

    for (int i = 1; i < word.length() - 1; i++) {
      if (word.charAt(i) == 32) {
        count++;
      }
    }

    if (word.length() == 0 || word.equals(" ")) {
      System.out.println(0);
    } else {
      System.out.println(count);
    }
  }
}