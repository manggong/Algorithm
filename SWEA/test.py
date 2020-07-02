import os
import sys

problem_number = sys.argv[-1]

if len(sys.argv) == 1:
    print("문제 번호를 넣어주세요")
    sys.exit(1)

os.system(f'python {problem_number}.py > {problem_number}_result.txt')
result = os.system(f'cmp {problem_number}_result.txt {problem_number}_output.txt')


if not result:
    print("정답 입니다.")
else:
    print("오답 입니다.")

# os.system(f'rm -rf {problem_number}_result.txt')