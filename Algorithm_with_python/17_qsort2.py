def qsort2_sub(a,start,end):
  if end - start <=0:
    return
  
  primary = a[end]
  i = start
  for j in range(start,end):

    if a[j] <= primary:
      a[i],a[j] = a[j],a[i]
      i += 1
  a[i],a[end] = a[end],a[i]

  qsort2_sub(a,start,i-1)
  qsort2_sub(a,i+1,end)

def qsort2(a):
  qsort2_sub(a,0,len(a)-1)

arr = [12,4,3,5,6,2,1,67,7,8]

qsort2(arr)

print(arr)