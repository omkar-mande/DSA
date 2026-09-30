arr=[1,3,6,8,7,12]
target = 13
left = 0
right = len(arr)-1
while left<right:
    if arr[left]+arr[right]==target:
        print(arr[left], '+', arr[right], "=", target)
        
    elif arr[left] + arr[right] < target:
        left+=1
    else:
        right-=1