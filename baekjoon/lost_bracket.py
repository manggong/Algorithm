numbers = input().split('-')
hap = 0 

# 음수의 총 합
for number in numbers[0].split('+'): 
    hap += int(number) 
    
for i in numbers[1:]: 
    for j in i.split('+'): 
        hap -= int(j)
print(hap)
