# #using list slicing
def rot(arr,d,n):
    arr[:]=arr[d:n]+arr[0:d]
    return arr

arr=[1,2,3,4,5,6,7,8]
n=len(arr)
d=int(input("enter d rotation"))
print(rot(arr,d,n))


