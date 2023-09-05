def print_back(n):
    while(n<0):
        return
    print(n)
    print_back(n-1)

print_back(10)