package algorithm.programmers;

import java.util.Scanner;

public class BackForwardWord {
	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		String str = kb.next();

		str = str.toUpperCase();

		String str2 = new StringBuilder(str).reverse().toString();

		if (str.equals(str2)) {
			System.out.println("YES");
		} else {
			System.out.println("NO");
		}

	}
}
