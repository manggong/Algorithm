package algorithm.programmers;

import java.util.Scanner;

public class Uwoo {

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		int n = kb.nextInt();
		int[] a = new int[n];
		int[] b = new int[n];

		for (int i = 0; i < n; i++) {
			a[i] = kb.nextInt();
		}

		for (int i = 0; i < n; i++) {
			b[i] = kb.nextInt();
		}

		for (int i = 0; i < n; i++) {
			if (a[i] == b[i]) {
				System.out.println("D");
			} else if (a[i] == 1 && b[i] == 3) {
				System.out.println("A");
			} else if (a[i] == 2 && b[i] == 1) {
				System.out.println("A");
			} else if (a[i] == 3 && b[i] == 2) {
				System.out.println("A");
			} else {
				System.out.println("B");
			}
		}

	}

}
