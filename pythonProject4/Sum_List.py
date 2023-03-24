"""
def sum_list():
    lst = []
    while True:
        num_input = input("Enter number or ok: ")
        if num_input == 'ok':
            break
        num = int(num_input)
        lst.append(num)
    print("List:", lst)
    total = sum(lst)
    return total


result = sum_list()
print("Sum_of_List:", result)
"""
