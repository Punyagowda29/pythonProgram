def sum_of_digits(n):
    sum = 0
    while(n>0):
        rem=n%10
        sum+=rem
        n//=10
    return sum
for i in range(100,201):
    if (sum_of_digits(i))%2==0:
        print(i)