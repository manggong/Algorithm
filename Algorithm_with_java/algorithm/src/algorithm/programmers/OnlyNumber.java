package algorithm.programmers;

import java.util.Scanner;

public class OnlyNumber {
	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		String str = kb.next();
		String answer = "";

		for (char x : str.toCharArray()) {
//			if (x >= 48 && x <= 57) {
//				answer = answer * 10 + (x - 48);
//			}
			
			if(Character.isDigit(x)) {
				answer += x;
			}
		}
		
		System.out.println(Integer.parseInt(answer));
	}
}
