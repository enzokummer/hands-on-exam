def seven():
    numbers = [2, 20, 3, 7, 10, 4, 4, 7, 9, 12, 15, 14, 11, 10, 13, 10, 20, 16, 12, 16]

    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)

    new_list.sort()
    return new_list

question/8


def steps_to_the_right(nums, steps):
    new_list = []
    for i in range(steps+1):
        new_list.append(nums[i])
    for i in range(steps+1):
        nums.remove(nums[0])

    return nums + new_list

nums = [1,2,3,4,5,6,7]
print(steps_to_the_right(nums, 3))

