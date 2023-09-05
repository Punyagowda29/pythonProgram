import random
numbers=set()
while len(numbers)<10:
    numbers.add(random.randint(20,55))
count35=0
number_copy=numbers.copy()
for num in number_copy:
    if num<35:
        count35+=1
    elif num>45:
        numbers.remove(num)
print(count35)
print(number_copy)