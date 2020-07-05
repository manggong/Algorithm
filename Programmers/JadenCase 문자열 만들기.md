### JadenCase 문자열 만들기

- 문제 : [12951](https://programmers.co.kr/learn/courses/30/lessons/12951)

~~~python
def solution(s):
    convertList = s.split(' ')
    for i in range(0,len(convertList)):
        convertList[i] = convertList[i].capitalize()
    joinList = ' '.join(convertList)
    return joinList
~~~

