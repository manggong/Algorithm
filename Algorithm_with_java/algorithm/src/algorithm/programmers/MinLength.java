package algorithm.programmers;

import java.util.Scanner;

public class MinLength {

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		String str = kb.next();
		char c = kb.next().charAt(0);
		int p = 1000;
		int[] answer = new int[str.length()];

		// 앞에서 부터 찾기
		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) == c) {
				p = 0;
				answer[i] = p;
			} else {
				p++;
				answer[i] = p;
			}
		}
		p = 1000;
		// 뒤에서 부터 찾기
		for (int i = str.length() - 1; i >= 0; i--) {
			if (str.charAt(i) == c) {
				p = 0;
			} else {
				p++;
				answer[i] = Math.min(answer[i], p);
			}
		}

		for (int x : answer) {
			System.out.print(x + " ");
		}
	}
}
