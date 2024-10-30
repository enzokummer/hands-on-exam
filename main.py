def seven():
    numbers = [2, 20, 3, 7, 10, 4, 4, 7, 9, 12, 15, 14, 11, 10, 13, 10, 20, 16, 12, 16]

    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)

    new_list.sort()
    return new_list

#print(seven())