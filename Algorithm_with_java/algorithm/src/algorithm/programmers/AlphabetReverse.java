package algorithm.programmers;

import java.util.Scanner;

public class AlphabetReverse {

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		String str = kb.next();
		String answer = "";
		char[] c = str.toCharArray();
		int lt = 0;
		int rt = str.length() - 1;

		while (lt < rt) {
			if (!Character.isAlphabetic(c[lt])) {
				lt++;
			} else if (!Character.isAlphabetic(c[rt])) {
				rt--;
			} else {
				char tmp = c[lt];
				c[lt] = c[rt];
				c[rt] = tmp;
				lt++;
				rt--;
			}
		}
		answer = String.valueOf(c);
		System.out.println(answer);
	}

}
