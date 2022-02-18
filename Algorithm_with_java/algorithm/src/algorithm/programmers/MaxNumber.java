package algorithm.programmers;

import java.util.ArrayList;
import java.util.Scanner;

public class MaxNumber {

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		int n = kb.nextInt();
		int[] arr = new int[n];
		for(int i = 0; i<n; i++) {
			arr[i] = kb.nextInt();
		}
		ArrayList<Integer> answer = new ArrayList<>();
		
		answer.add(arr[0]);
		for(int i = 1; i<n; i++) {
			if(arr[i] > arr[i-1]) {
				answer.add(arr[i]);
			}
		}

		System.out.println(answer);
	}

}
