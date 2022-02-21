package algorithm.programmers;

import java.util.Scanner;

public class Student {

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		int n = kb.nextInt();
		int[] numbers = new int[n];
		int answer = 1;
		int max = 0;
		
		for(int i = 0; i<n; i++) {
			numbers[i] = kb.nextInt();
		}
		
		max = numbers[0];
		
		for(int i = 1; i < numbers.length; i++) {
			if(numbers[i] > max) {
				max = numbers[i];
				answer++;
			}
		}

		System.out.println(answer);
	}

}