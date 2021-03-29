// 길이(i)  0 1 2 3 4 5 6 7 8 9 10
// 가격(Pi) 0 1 5 8 9 10 17 17 20 24 30

let p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30];
function cutRod(p, n) {
  let r = [0];
  for (let j = 1; j <= n; j++) {
    q = -1;
    for (let i = 1; i <= j; i++) {
      q = Math.max(q, p[i] + r[j - i]);
    }
    r[j] = q;
  }
  return r[n];
}
cutRod(p, 2); // 5
cutRod(p, 3); // 8
cutRod(p, 4); // 10
cutRod(p, 7); // 18