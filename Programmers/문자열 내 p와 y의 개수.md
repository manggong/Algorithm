### 문자열 내 p와 y의 개수

- 문제 : [12916](https://programmers.co.kr/learn/courses/30/lessons/12916)

~~~javascript
function solution(s) {
    return s.toUpperCase().split("P").length ===  s.toUpperCase().split("Y").length;
}
~~~

