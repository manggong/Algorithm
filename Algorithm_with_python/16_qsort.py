def qsort(a):
  n = len(a)
  
  if n <= 1:
    return a
  
  primary = a[-1] # 리스트의 마지막 값이 기준

  g1 = []
  g2 = []

  for i in range(0, n-1):
    if a[i] < primary:
      g1.append(a[i])
    else:
      g2.append(a[i])
  return qsort(g1)+[primary]+qsort(g2)

arr = [2,4,5,6,87,1,3,54]

print(qsort(arr))
