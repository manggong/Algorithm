package algorithm.programmers;

import java.util.Scanner;

public class SetString {

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		String str = kb.next();
		String answer = "";
		
		for(int i = 0; i < str.length(); i++) {
			if(answer.indexOf(str.charAt(i)) == -1) {
				answer += str.charAt(i);
			}
		}
		System.out.println(answer);
	}

}
