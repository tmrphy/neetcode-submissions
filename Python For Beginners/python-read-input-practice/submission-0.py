def add_two_numbers() -> int:
    user_input = input()
    number_string = user_input.split(",")
    nums = []
    for num in number_string:
        nums.append(int(num))
    return nums[0] + nums[1]




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
