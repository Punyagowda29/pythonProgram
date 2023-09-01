n = int(input("size"))
lst = []
for i in range(0, n):
    inp = input("enter")
    lst.append(inp)

for i in range(0, len(lst)):
    for j in range(i + 1, len(lst)):
        if (lst[i] == lst[j]):
            print(lst[j])

print(lst)