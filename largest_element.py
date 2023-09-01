def largestele(arr,n):
    max=arr[0]
    for i in range(0,n):
        if max < arr[i]:
            max=arr[i]
    return max

arr=[45,29,56,100]
n=len(arr)
print(largestele(arr,n))
