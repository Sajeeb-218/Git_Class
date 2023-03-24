def unique(real):
    org_lst = []
    for index in real:
        if index not in org_lst:
            org_lst.append(index)

    return org_lst

lst = []
while True:
    num = input("Enter number or ok: ")
    if num == "ok":
        break
    lst.append(num)
print("Original list:", lst)

unique_lst = unique(lst)
print("Unique List:", unique_lst)

                                                