package algorithm.programmers;

import java.util.Scanner;

public class Zipping {

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		int cnt = 1;
		String answer = "";
		String str = kb.next() + " ";

		for (int i = 0; i < str.length() - 1; i++) {
			if (str.charAt(i) == str.charAt(i + 1)) {
				cnt++;
			} else {
				answer += str.charAt(i);
				if (cnt > 1) {
					answer += String.valueOf(cnt);
					cnt = 1;
				}
			}
		}
		System.out.println(answer);
	}
}
