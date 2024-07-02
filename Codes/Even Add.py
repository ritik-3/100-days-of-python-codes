a_list = [0]
for num in range(1, 101):
    print(num)
    if num % 2 == 0:
        a_list.append(num)
Sum = sum(a_list)

print(a_list)
print(Sum)