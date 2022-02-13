package algorithm.programmers;

import java.util.ArrayList;
import java.util.Scanner;

public class ReverseWord {

	public static void main(String[] args) {
		ArrayList<String> answer = new ArrayList<>();
		Scanner kb = new Scanner(System.in);
		int n = kb.nextInt();
		String[] str = new String[n];

		// 입력 받기 
		for (int i = 0; i < str.length; i++) {
			str[i] = kb.next();
		}

		// 문장 뒤집기 
		for (String x : str) {
			String tmp = new StringBuilder(x).reverse().toString();
			answer.add(tmp);
		}

		// 출력 
		for (String y : answer) {
			System.out.println(y);
		}

	}

}
