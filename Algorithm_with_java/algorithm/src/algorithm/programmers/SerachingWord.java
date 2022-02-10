package algorithm.programmers;

import java.util.Scanner;

public class SerachingWord {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int answer = 0;
		String input1 = in.next();
		char input2 = in.next().charAt(0);

		input1 = input1.toUpperCase();
		input2 = Character.toUpperCase(input2);

		for (char x : input1.toCharArray()) {
			if (x == input2)
				answer++;
		}
		System.out.println(answer);
	}
}
