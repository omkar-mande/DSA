arr = [5, 8, 3, 8, 2, 8]
target = 8
count = 0
current = 0
for i in range(len(arr)):
    if arr[i] == target:
        current = i
print(current)