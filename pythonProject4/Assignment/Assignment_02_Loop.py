my_list = [1, 2, 3, 4]
i = 0

while i < len(my_list):
    j = 0
    sum = 0
    while j <= i:
        sum += my_list[j]
        j += 1
    my_list[i] = sum
    i += 1

print(my_list)
