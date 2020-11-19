def bsearch(a,x):

  start = 0
  end = len(a) - 1

  while start <= end:
    mid = (start + end) // 2
    if x == a[mid]:
      return mid
    elif x > a[mid]:
      start = mid + 1
    else:
      end = mid - 1

  return -1


arr = [1,4,6,7,88,34,78,99]

print(bsearch(arr,7))

print(bsearch(arr,99))