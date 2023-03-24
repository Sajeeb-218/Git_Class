def count_vowels_after_consonants(total, string):
    incre = 0

    for index in range(total-1):
        if string[index] not in 'aeiou' and string[index+1] in 'aeiou':
            incre += 1
    return incre



round = int(input("How many times you wants to Execute the loop?: "))
count = 0
while count < round:
    length = int(input("Enter the total length of the string: "))
    word = input("Enter the string: ")
    print(count_vowels_after_consonants(length, word))
    count += 1

