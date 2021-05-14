def getMaxMin(arr):
  n = len(arr)
  
  if n%2 == 0:
    mx = max(arr[0],arr[1])
    mn = min(arr[0],arr[1])
    i = 2
  else:
    mx = mn = arr[0]
    i = 1
  
  while i < n-1:
    if arr[i]<arr[i+1]:
      mx = max(mx,arr[i+1])
      mn = min(mn,arr[i])
    else:  
      mx = max(mx,arr[i])
      mn = min(mn,arr[i+1])
    i = i+1
  return mx,mn  


arr = [11,93,49,34,10,14]

mx,mn = getMaxMin(arr)
print(mx)
print(mn)
