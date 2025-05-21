# number of unique elements

def num_unique_elements(nums: list):
    n = len(nums)
    for i in range(n):
        # print(i)
        for j in range(0, n - i - 1):
            # print(j)
            # print(n - i - 1)
            if nums[j] > nums[j + 1]:
                # Swap the elements in place
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    # this method or just using set
    unique_nums = []
    for i in range(n):
        if i == 0 or nums[i] != nums[i - 1]:
            unique_nums.append(nums[i])
    return unique_nums


print(num_unique_elements([1, 1, 2]))

