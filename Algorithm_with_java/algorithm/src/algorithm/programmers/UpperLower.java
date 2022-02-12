package algorithm.programmers;

import java.util.Scanner;

public class UpperLower {

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		String str = kb.next();
		String answer = "";

		for (char x : str.toCharArray()) {
			if (Character.isUpperCase(x)) {
				answer += Character.toLowerCase(x);
			} else {
				answer += Character.toUpperCase(x);
			}
		}
		System.out.println(answer);
	}

}
