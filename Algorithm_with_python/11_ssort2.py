def sel_sort(a):
    n = len(a)
    for i in range(0,n-1):
        min_idx = i
        for j in range(i+1,n):
            if a[j]<a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

arr=[1,2,3,4,5,6]

sel_sort(arr)

print(arr)