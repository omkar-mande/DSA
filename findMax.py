def find_max(arr):
    max = arr[0]
    
    for i in arr:
        if i>max:
            max = i
    return max

arr=[10,30,45,5,9]

print(find_max(arr))
        
    


#Output: 25