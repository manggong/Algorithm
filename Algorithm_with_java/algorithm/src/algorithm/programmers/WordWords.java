package algorithm.programmers;

import java.util.Scanner;

public class WordWords {

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		String str = kb.nextLine();
		String answer = "";
		int m = 0;
		String[] s = str.split(" ");

		for (String x : s) {
			int len = x.length();
			if (len > m) {
				m = len;
				answer = x;
			}
		}
		System.out.println(answer);
	}

}
