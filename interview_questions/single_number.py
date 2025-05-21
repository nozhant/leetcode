# class Solution:
#     @staticmethod
#     def single_number(nums):
#
#         nums.sort()
#         for i in nums:
#
#             if nums[i] ==

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example usage
nums = [2,2,1]
print(single_number(nums))  # Output: 4




