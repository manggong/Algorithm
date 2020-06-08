### K번째 수

- 문제 :[42748](https://programmers.co.kr/learn/courses/30/lessons/42748)

~~~javascript
function solution(array, commands) {
    var answer = [];
    
    for(let i=0; i<commands.length; i++){
        let list = array.slice(commands[i][0]-1, commands[i][1]).sort((a,b) => {return a-b})
        answer.push(list[commands[i][2]-1])
    }
    return answer;
}
~~~

