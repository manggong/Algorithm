package algorithm.chap01;

import java.util.Scanner;

public class SumForPos {

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);

		int n;

		System.out.println("1부터 N까지의 합을 구합니다.");

		do {
			System.out.println("n의 값은: ");
			n = stdIn.nextInt();
		} while (n <= 0);

		int sum = 0;

		for (int i = 1; i <= n; i++) {
			sum += i;
		}

		System.out.println("합은" + sum);
	}

}
