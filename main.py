def seven():
    numbers = [2, 20, 3, 7, 10, 4, 4, 7, 9, 12, 15, 14, 11, 10, 13, 10, 20, 16, 12, 16]

    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)

    new_list.sort()
    return new_list

def steps_to_the_right(nums, steps):
    new_list = []
    for i in range(steps+1):
        new_list.append(nums[i])
    for i in range(steps+1):
        nums.remove(nums[0])

    return nums + new_list


def nine():
    cons = [
        { name: 'Peyton Turner', company: 'Walker Inc' },
        { name: 'Isaias Fritsch', company: 'Walker Inc' },
        { name: 'Susana Wilderman', company: 'Nolan Inc' }
    ]
    output = {}
    for consultant in cons:
        company = consultant["company"]
        if company not in output:
            output[company] = []

        output[company].append(consultant)

print(nine())

