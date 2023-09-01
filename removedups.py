def removeDuplicates(arr, n):
    if n == 0 or n == 1:
        return n
    arr.sort()
    j = 1
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            j += 1
    return j