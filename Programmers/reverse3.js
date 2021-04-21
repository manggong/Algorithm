function solution(n) {
  let answer;
  answer = n.toString(3).split('').reverse().join('');
  return parseInt(answer, 3);
}
