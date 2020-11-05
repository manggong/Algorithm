def search_list(a,x):
    n = len(a)
    for i in range(0,n):
        if x==a[i]:
            return i 
    return -1 # 없으면 -1



arr = [1,2,3,4,5,6]

print(search_list(arr,5))