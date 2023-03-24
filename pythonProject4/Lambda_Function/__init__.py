"""
lst_comp = [num for num in range(900, 1001, 50) if num % 2 == 0]

print(lst_comp)
"""
"""
set_comp = {num for num in range(5)}
print(set_comp)

set_comp = {num * 10 for num in range(5)}
print(set_comp)
"""
tpl_comp =tuple((num * 10 for num in range(5)))

print(tpl_comp)
