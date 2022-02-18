package algorithm.programmers;

import java.util.Scanner;

public class Password {

	public static void main(String[] args) {

		Scanner kb = new Scanner(System.in);
		int n = kb.nextInt();
		String str = kb.next();
		String answer = "";

		for (int i = 0; i < n; i++) {
			String tmp = str.substring(0, 7).replace("#", "1").replace("*", "0");
			int num = Integer.parseInt(tmp, 2);
			
			str = str.substring(7);
			answer += (char) num;
		}
		
		System.out.println(answer);
	}
}
