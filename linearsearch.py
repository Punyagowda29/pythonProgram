def linearsearch(arr,n,x):
    for i in range(0,n):
        if(arr[i] == x):
            return i
    return -1

n=int(input("enter n"))
arr=[]
for i in range(0,n):
    inp=int(input())
    arr.append(inp)

x=int(input("enter x"))
res=linearsearch(arr,n,x)
if(res==-1):
    print("nt found")
else:
    print(res)