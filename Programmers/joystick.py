def solution(name):
    
    terms = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    idx = 0
    answer = 0
    
    while True:
        answer += terms[idx]
        terms[idx] = 0
        if sum(terms) == 0:
            return answer
        
        left, right = 1, 1
        while terms[idx - left] == 0:
            left += 1
        while terms[idx - right] == 0:
            right += 1
        
        answer += left if left < right else right
        idx -= left if left < right else right